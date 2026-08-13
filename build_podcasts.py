#!/usr/bin/env python3
"""Render a recorded episode for every analysis page.

Each analysis page already carries its script in the `#pod` paragraph, which the
browser reads aloud with speech synthesis. This turns those same scripts into
real audio files so the pages can offer a recorded episode the way the landing
page does with The_Machine_Singapore_Built_E1.mp3.

    set ELEVENLABS_API_KEY=...
    set ELEVENLABS_VOICE_ID=...
    python build_podcasts.py                  # render everything that is missing
    python build_podcasts.py --only P1 G3     # render just these
    python build_podcasts.py --force          # re-render even if the mp3 exists
    python build_podcasts.py --wire           # add the <audio> player to the pages

Nothing is guessed. Missing configuration is a hard stop, not a silent skip:
a half-rendered library that looks complete is worse than one that refuses to
start.
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
API = 'https://api.elevenlabs.io/v1/text-to-speech/{voice}'

# Matches the paragraph the pages already use for the browser read-aloud.
POD_RE = re.compile(r'<p class="src" id="pod"[^>]*>(.*?)</p>', re.S)
TAG_RE = re.compile(r'<[^>]+>')


def die(msg, code=2):
    print('build_podcasts: ' + msg, file=sys.stderr)
    sys.exit(code)


def find_ffmpeg():
    """ffmpeg is optional - only needed for --normalise."""
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
    for a, b in (('&amp;', '&'), ('&lt;', '<'), ('&gt;', '>'),
                 ('&quot;', '"'), ('&#39;', "'"), ('&middot;', '.'),
                 ('&nbsp;', ' '), ('&mdash;', '-'), ('&ndash;', '-')):
        s = s.replace(a, b)
    return s


def script_for(path):
    """Pull the spoken script out of a page, or None if it has no podcast."""
    html = open(path, encoding='utf-8').read()
    m = POD_RE.search(html)
    if not m:
        return None
    text = unescape(TAG_RE.sub(' ', m.group(1)))
    return re.sub(r'\s+', ' ', text).strip()


def synthesise(text, key, voice, model, stability, similarity):
    body = json.dumps({
        'text': text,
        'model_id': model,
        'voice_settings': {
            'stability': stability,
            'similarity_boost': similarity,
        },
    }).encode('utf-8')
    req = urllib.request.Request(
        API.format(voice=voice),
        data=body,
        headers={
            'xi-api-key': key,
            'content-type': 'application/json',
            'accept': 'audio/mpeg',
        },
    )
    try:
        with urllib.request.urlopen(req, timeout=300) as r:
            return r.read()
    except urllib.error.HTTPError as e:
        detail = e.read().decode('utf-8', 'replace')[:400]
        die('ElevenLabs returned %s: %s' % (e.code, detail))
    except urllib.error.URLError as e:
        die('cannot reach ElevenLabs: %s' % e.reason)


def wire_player(path, stem):
    """Add an <audio> element next to the existing read-aloud button."""
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


def write_manifest():
    """Collect every page's script into analysis/pods.json.

    The listing pages need the text to read it aloud, and re-deriving it in the
    browser would mean fetching 25 pages. Generated from the same #pod
    paragraphs the pages render, so it cannot drift from what is on screen.
    """
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
        out[stem] = {
            'title': unescape(title.group(1)).strip() if title else stem,
            'script': text,
            'mp3': ('audio/%s_analysis.mp3' % stem
                    if os.path.exists(os.path.join(AUDIO, '%s_analysis.mp3' % stem))
                    else None),
        }
    path = os.path.join(ANALYSIS, 'pods.json')
    with open(path, 'w', encoding='utf-8', newline='\n') as fh:
        json.dump(out, fh, ensure_ascii=False, indent=1, sort_keys=True)
    chars = sum(len(v['script']) for v in out.values())
    recorded = sum(1 for v in out.values() if v['mp3'])
    print('pods.json: %d scripts, %d characters, %d with a recorded mp3'
          % (len(out), chars, recorded))
    return 0


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--only', nargs='*', metavar='STEM',
                    help='page stems to render, e.g. P1 G3 X2')
    ap.add_argument('--force', action='store_true',
                    help='re-render even when the mp3 already exists')
    ap.add_argument('--wire', action='store_true',
                    help='add the <audio> player to pages that have an mp3')
    ap.add_argument('--normalise', action='store_true',
                    help='loudness-normalise with ffmpeg after rendering')
    ap.add_argument('--model', default='eleven_multilingual_v2')
    ap.add_argument('--stability', type=float, default=0.50)
    ap.add_argument('--similarity', type=float, default=0.75)
    ap.add_argument('--dry-run', action='store_true',
                    help='list what would be rendered, call nothing')
    ap.add_argument('--manifest', action='store_true',
                    help='write analysis/pods.json and exit, so listing pages '
                         'can offer play without opening each analysis')
    args = ap.parse_args()

    if args.manifest:
        return write_manifest()

    if not os.path.isdir(ANALYSIS):
        die('no analysis/ directory beside this script - run it from the repo')

    pages = sorted(
        f for f in os.listdir(ANALYSIS)
        if f.endswith('.html') and f not in ('index.html', 'entity-graph.html'))
    if args.only:
        want = {s.lower() for s in args.only}
        pages = [p for p in pages if os.path.splitext(p)[0].lower() in want]
        if not pages:
            die('none of %s matched a page in analysis/' % ', '.join(args.only))

    jobs = []
    for page in pages:
        stem = os.path.splitext(page)[0]
        text = script_for(os.path.join(ANALYSIS, page))
        if not text:
            print('  skip %-6s no #pod script on the page' % stem)
            continue
        out = os.path.join(AUDIO, '%s_analysis.mp3' % stem)
        if os.path.exists(out) and not args.force:
            print('  have %-6s %s' % (stem, os.path.basename(out)))
            continue
        jobs.append((stem, text, out))

    if not jobs:
        print('nothing to render.')
        return

    print('%d episode(s) to render, %d characters total'
          % (len(jobs), sum(len(t) for _s, t, _o in jobs)))

    if args.dry_run:
        for stem, text, _out in jobs:
            print('  %-6s %5d chars  %s...' % (stem, len(text), text[:70]))
        return

    key = os.environ.get('ELEVENLABS_API_KEY')
    voice = os.environ.get('ELEVENLABS_VOICE_ID')
    if not key:
        die('ELEVENLABS_API_KEY is not set')
    if not voice:
        die('ELEVENLABS_VOICE_ID is not set - pick the voice deliberately '
            'rather than letting the API choose a default')

    ff = find_ffmpeg() if args.normalise else None
    if args.normalise and not ff:
        die('--normalise needs ffmpeg on PATH or under ~/tools')

    os.makedirs(AUDIO, exist_ok=True)
    for stem, text, out in jobs:
        print('  render %-6s %5d chars ...' % (stem, len(text)), end='', flush=True)
        data = synthesise(text, key, voice, args.model,
                          args.stability, args.similarity)
        tmp = out + '.part'
        with open(tmp, 'wb') as fh:
            fh.write(data)
        if ff:
            norm = out + '.norm.mp3'
            subprocess.run([ff, '-y', '-loglevel', 'error', '-i', tmp,
                            '-af', 'loudnorm=I=-16:TP=-1.5:LRA=11',
                            '-c:a', 'libmp3lame', '-b:a', '128k', norm],
                           check=True)
            os.replace(norm, out)
            os.remove(tmp)
        else:
            os.replace(tmp, out)
        print(' %.2f MB' % (os.path.getsize(out) / 1048576))

    if args.wire:
        wired = 0
        for page in pages:
            stem = os.path.splitext(page)[0]
            if os.path.exists(os.path.join(AUDIO, '%s_analysis.mp3' % stem)):
                if wire_player(os.path.join(ANALYSIS, page), stem):
                    wired += 1
        print('wired the player into %d page(s)' % wired)


if __name__ == '__main__':
    main()
