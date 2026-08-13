#!/usr/bin/env python3
"""Render a two-host episode for every analysis page.

Each analysis page carries its script in the `#pod` paragraph, marked up with
`Host A:` / `Host B:` turns. This renders each turn in its own voice, drops a
short beat between them, and stitches the result — the same shape as the
hand-built The_Machine_Singapore_Built_E1.mp3, but reproducible.

    set ELEVENLABS_API_KEY=...
    python build_podcasts.py --dry-run      # what would render, calls nothing
    python build_podcasts.py                # render everything missing
    python build_podcasts.py --only P1 G3   # just these
    python build_podcasts.py --force        # re-render existing
    python build_podcasts.py --wire         # add the <audio> player to pages
    python build_podcasts.py --manifest     # rebuild analysis/pods.json only

Voices default to two premade ElevenLabs voices chosen to sit close to the
NotebookLM pairing - a warm, measured female lead and a relaxed male
counterpart. Override with ELEVENLABS_VOICE_A / ELEVENLABS_VOICE_B.

Missing configuration is a hard stop, never a silent skip: a half-rendered
library that looks complete is worse than one that refuses to start.
"""

import argparse
import json
import os
import re
import shutil
import subprocess
import sys
import urllib.error
import urllib.request

ROOT = os.path.dirname(os.path.abspath(__file__))
ANALYSIS = os.path.join(ROOT, 'analysis')
AUDIO = os.path.join(ROOT, 'audio')
SEGMENTS = os.path.join(ROOT, 'podcast', 'segments')
API = 'https://api.elevenlabs.io/v1/text-to-speech/{voice}?output_format=mp3_44100_128'

# Sarah - mature, reassuring, confident.  Roger - laid-back, casual, resonant.
DEFAULT_A = 'EXAVITQu4vr4xnSDxMaL'
DEFAULT_B = 'CwhRBWXzGAHq8TQ4Fs17'

POD_RE = re.compile(r'<p class="src" id="pod"[^>]*>(.*?)</p>', re.S)
TAG_RE = re.compile(r'<[^>]+>')
TURN_RE = re.compile(r'Host\s+([AB])\s*:\s*', re.I)
BEAT = 0.38  # seconds of silence between turns


def die(msg, code=2):
    print('build_podcasts: ' + msg, file=sys.stderr)
    sys.exit(code)


def find_ffmpeg():
    exe = shutil.which('ffmpeg')
    if exe:
        return exe
    tools = os.path.join(os.path.expanduser('~'), 'tools')
    if os.path.isdir(tools):
        for dirpath, _dirs, files in os.walk(tools):
            if 'ffmpeg.exe' in files:
                return os.path.join(dirpath, 'ffmpeg.exe')
    return None


def unescape(s):
    for a, b in (('&amp;', '&'), ('&lt;', '<'), ('&gt;', '>'), ('&quot;', '"'),
                 ('&#39;', "'"), ('&middot;', '.'), ('&nbsp;', ' '),
                 ('&mdash;', '-'), ('&ndash;', '-')):
        s = s.replace(a, b)
    return s


def script_for(path):
    html = open(path, encoding='utf-8').read()
    m = POD_RE.search(html)
    if not m:
        return None
    return re.sub(r'\s+', ' ', unescape(TAG_RE.sub(' ', m.group(1)))).strip()


def split_turns(script):
    """[(speaker, text), ...]. Any lead-in before the first marker goes to A."""
    parts = TURN_RE.split(script)
    lead = parts[0].strip()
    turns = []
    if lead:
        turns.append(('A', lead))
    for i in range(1, len(parts) - 1, 2):
        who = parts[i].upper()
        text = parts[i + 1].strip()
        if text:
            # A lead-in already assigned to A shouldn't be spoken twice over.
            if turns and turns[-1][0] == who:
                turns[-1] = (who, turns[-1][1] + ' ' + text)
            else:
                turns.append((who, text))
    return turns


def synthesise(text, key, voice, model, stability, similarity):
    body = json.dumps({
        'text': text,
        'model_id': model,
        'voice_settings': {'stability': stability, 'similarity_boost': similarity},
    }).encode('utf-8')
    req = urllib.request.Request(
        API.format(voice=voice), data=body,
        headers={'xi-api-key': key, 'content-type': 'application/json',
                 'accept': 'audio/mpeg'})
    try:
        with urllib.request.urlopen(req, timeout=300) as r:
            return r.read()
    except urllib.error.HTTPError as e:
        detail = e.read().decode('utf-8', 'replace')[:300]
        if e.code == 401:
            die('ElevenLabs rejected the key for text-to-speech (401). Reads may '
                'still work: this is usually a key created without the '
                'Text to Speech permission. %s' % detail)
        die('ElevenLabs returned %s: %s' % (e.code, detail))
    except urllib.error.URLError as e:
        die('cannot reach ElevenLabs: %s' % e.reason)


def make_silence(ff, path):
    if os.path.exists(path):
        return
    subprocess.run([ff, '-y', '-loglevel', 'error', '-f', 'lavfi',
                    '-i', 'anullsrc=r=44100:cl=mono', '-t', str(BEAT),
                    '-c:a', 'libmp3lame', '-b:a', '128k', path], check=True)


def stitch(ff, pieces, out, normalise):
    listing = out + '.txt'
    with open(listing, 'w', encoding='utf-8', newline='\n') as fh:
        for p in pieces:
            fh.write("file '%s'\n" % p.replace('\\', '/').replace("'", "'\\''"))
    tmp = out + '.part'
    cmd = [ff, '-y', '-loglevel', 'error', '-f', 'concat', '-safe', '0',
           '-i', listing]
    if normalise:
        cmd += ['-af', 'loudnorm=I=-16:TP=-1.5:LRA=11']
    cmd += ['-c:a', 'libmp3lame', '-b:a', '128k', tmp]
    subprocess.run(cmd, check=True)
    os.replace(tmp, out)
    os.remove(listing)


def write_manifest():
    out = {}
    for page in sorted(os.listdir(ANALYSIS)):
        if not page.endswith('.html') or page in ('index.html', 'entity-graph.html'):
            continue
        text = script_for(os.path.join(ANALYSIS, page))
        if not text:
            continue
        html = open(os.path.join(ANALYSIS, page), encoding='utf-8').read()
        title = re.search(r'<title>([^<]*)</title>', html)
        stem = os.path.splitext(page)[0]
        mp3 = os.path.join(AUDIO, '%s_analysis.mp3' % stem)
        out[stem] = {
            'title': unescape(title.group(1)).strip() if title else stem,
            'script': text,
            'turns': len(split_turns(text)),
            'mp3': ('audio/%s_analysis.mp3' % stem) if os.path.exists(mp3) else None,
        }
    with open(os.path.join(ANALYSIS, 'pods.json'), 'w',
              encoding='utf-8', newline='\n') as fh:
        json.dump(out, fh, ensure_ascii=False, indent=1, sort_keys=True)
    print('pods.json: %d scripts, %d characters, %d with a recorded mp3'
          % (len(out), sum(len(v['script']) for v in out.values()),
             sum(1 for v in out.values() if v['mp3'])))
    return 0


def wire_player(path, stem):
    html = open(path, encoding='utf-8').read()
    if '%s_analysis.mp3' % stem in html:
        return False
    marker = 'Play analysis</button>'
    if marker not in html:
        return False
    player = (marker + '\n<audio controls preload="none" '
              'style="width:100%;max-width:560px;margin-top:12px;display:block">'
              '<source src="../audio/{s}_analysis.mp3" type="audio/mpeg"></audio>'
              ).format(s=stem)
    open(path, 'w', encoding='utf-8', newline='\n').write(
        html.replace(marker, player, 1))
    return True


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--only', nargs='*', metavar='STEM')
    ap.add_argument('--force', action='store_true')
    ap.add_argument('--wire', action='store_true')
    ap.add_argument('--manifest', action='store_true')
    ap.add_argument('--no-normalise', action='store_true',
                    help='skip loudness normalisation')
    ap.add_argument('--model', default='eleven_multilingual_v2')
    ap.add_argument('--stability', type=float, default=0.50)
    ap.add_argument('--similarity', type=float, default=0.75)
    ap.add_argument('--dry-run', action='store_true')
    args = ap.parse_args()

    if not os.path.isdir(ANALYSIS):
        die('no analysis/ directory beside this script - run it from the repo')
    if args.manifest:
        return write_manifest()

    pages = sorted(f for f in os.listdir(ANALYSIS)
                   if f.endswith('.html')
                   and f not in ('index.html', 'entity-graph.html'))
    if args.only:
        want = {s.lower() for s in args.only}
        pages = [p for p in pages if os.path.splitext(p)[0].lower() in want]
        if not pages:
            die('none of %s matched a page in analysis/' % ', '.join(args.only))

    jobs, single = [], []
    for page in pages:
        stem = os.path.splitext(page)[0]
        text = script_for(os.path.join(ANALYSIS, page))
        if not text:
            print('  skip %-5s no #pod script' % stem)
            continue
        out = os.path.join(AUDIO, '%s_analysis.mp3' % stem)
        if os.path.exists(out) and not args.force:
            print('  have %-5s %s' % (stem, os.path.basename(out)))
            continue
        turns = split_turns(text)
        if len({w for w, _t in turns}) < 2:
            single.append(stem)
        jobs.append((stem, turns, out))

    if single:
        print('  ! single-voice (no Host A/B markers): %s' % ', '.join(single))

    if not jobs:
        print('nothing to render.')
        return

    total = sum(len(t) for _s, turns, _o in jobs for t in [turns])
    chars = sum(len(t) for _s, turns, _o in jobs for _w, t in turns)
    print('%d episode(s), %d turns, %d characters' % (len(jobs), total, chars))

    if args.dry_run:
        for stem, turns, _out in jobs:
            print('  %-5s %2d turns  %5d chars' % (
                stem, len(turns), sum(len(t) for _w, t in turns)))
        return

    key = os.environ.get('ELEVENLABS_API_KEY')
    if not key:
        die('ELEVENLABS_API_KEY is not set')
    va = os.environ.get('ELEVENLABS_VOICE_A', DEFAULT_A)
    vb = os.environ.get('ELEVENLABS_VOICE_B', DEFAULT_B)

    ff = find_ffmpeg()
    if not ff:
        die('ffmpeg not found on PATH or under ~/tools - needed to join the turns')

    os.makedirs(AUDIO, exist_ok=True)
    os.makedirs(SEGMENTS, exist_ok=True)
    silence = os.path.join(SEGMENTS, '_beat.mp3')
    make_silence(ff, silence)

    for stem, turns, out in jobs:
        print('  %-5s %2d turns ' % (stem, len(turns)), end='', flush=True)
        segdir = os.path.join(SEGMENTS, stem)
        os.makedirs(segdir, exist_ok=True)
        pieces = []
        for i, (who, text) in enumerate(turns):
            seg = os.path.join(segdir, '%03d_%s.mp3' % (i, who))
            if not (os.path.exists(seg) and os.path.getsize(seg) > 0):
                data = synthesise(text, key, va if who == 'A' else vb,
                                  args.model, args.stability, args.similarity)
                tmp = seg + '.part'
                with open(tmp, 'wb') as fh:
                    fh.write(data)
                os.replace(tmp, seg)
            if pieces:
                pieces.append(silence)
            pieces.append(seg)
            print('.', end='', flush=True)
        stitch(ff, pieces, out, not args.no_normalise)
        print(' %.2f MB' % (os.path.getsize(out) / 1048576))

    if args.wire:
        wired = 0
        for page in pages:
            stem = os.path.splitext(page)[0]
            if os.path.exists(os.path.join(AUDIO, '%s_analysis.mp3' % stem)):
                if wire_player(os.path.join(ANALYSIS, page), stem):
                    wired += 1
        print('wired the player into %d page(s)' % wired)
    write_manifest()


if __name__ == '__main__':
    main()
