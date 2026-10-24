#!/usr/bin/env python3
"""Build the GitHub Pages copy of Living Bonsai.

source/app.html is the whole app as one page (the same page that runs inside Claude).
This wraps it in a full HTML document for the web: home-screen app tags, the manifest,
the Firebase config for sync, and the offline service worker. Run from the repo root:

    python3 source/build.py
"""
import json, pathlib, re

ROOT = pathlib.Path(__file__).resolve().parent.parent
src = (ROOT / 'source' / 'app.html').read_text(encoding='utf-8')

title = re.search(r'<title>(.*?)</title>', src, re.S).group(1).strip()
style_start = src.index('<style>')
style_end = src.index('</style>', style_start) + len('</style>')
head_links = '\n'.join(l for l in src[:style_start].splitlines() if l.strip().startswith('<link'))
style = src[style_start:style_end]
body = src[style_end:].strip()

assert '/*WEB_BUILD*/false' in body, 'platform flag not found in source/app.html'
body = body.replace('/*WEB_BUILD*/false', '/*WEB_BUILD*/true', 1)
version = re.search(r"const VERSION = '([^']+)'", body).group(1)

page = f'''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>{title}</title>
<meta name="description" content="A bonsai that lives on the real calendar. Wire, prune, pinch and defoliate a trident maple toward fine ramification.">
<meta name="theme-color" content="#F6F8F4" media="(prefers-color-scheme: light)">
<meta name="theme-color" content="#17201B" media="(prefers-color-scheme: dark)">
<meta name="apple-mobile-web-app-capable" content="yes">
<meta name="mobile-web-app-capable" content="yes">
<meta name="apple-mobile-web-app-title" content="Bonsai">
<meta name="apple-mobile-web-app-status-bar-style" content="default">
<link rel="manifest" href="manifest.webmanifest">
<link rel="icon" href="icons/favicon.svg" type="image/svg+xml">
<link rel="apple-touch-icon" href="icons/apple-touch-icon.png">
{head_links}
<style>
/* page frame (the Claude viewer supplies this for the copy that runs there) */
:root {{ color-scheme: light; box-sizing: border-box; height: 100%; padding-top: env(safe-area-inset-top, 0px); padding-bottom: env(safe-area-inset-bottom, 0px); }}
body {{ margin: 0; font: 14px system-ui, -apple-system, "Segoe UI", sans-serif; }}
img {{ max-width: 100%; }}
button {{ touch-action: manipulation; }}
[hidden] {{ display: none !important; }}
</style>
{style}
<script src="firebase-config.js"></script>
</head>
<body>
{body}
<script>
if ('serviceWorker' in navigator) addEventListener('load', () => navigator.serviceWorker.register('sw.js').catch(() => {{}}));
</script>
</body>
</html>
'''
(ROOT / 'index.html').write_text(page, encoding='utf-8')

sw = (ROOT / 'sw.js').read_text(encoding='utf-8')
sw = re.sub(r"const CACHE = 'living-bonsai-[^']*';", f"const CACHE = 'living-bonsai-{version}';", sw)
(ROOT / 'sw.js').write_text(sw, encoding='utf-8')
(ROOT / 'version.json').write_text(json.dumps({'version': version}) + '\n', encoding='utf-8')
print(f'Built index.html (version {version}, {len(page) // 1024} KB)')
