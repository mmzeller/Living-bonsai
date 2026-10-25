/* Living Bonsai service worker: keeps the app working offline. */
const CACHE = 'living-bonsai-0.9.0';
const ASSETS = ['./', './index.html', './manifest.webmanifest', './firebase-config.js', './icons/favicon.svg', './icons/icon-192.png', './icons/icon-512.png', './icons/apple-touch-icon.png'];
self.addEventListener('install', (e) => {
  // cache: 'reload' skips the browser's own cache so an update never installs stale files
  e.waitUntil(caches.open(CACHE).then((c) => c.addAll(ASSETS.map((u) => new Request(u, { cache: 'reload' })))).then(() => self.skipWaiting()));
});
self.addEventListener('activate', (e) => {
  e.waitUntil(caches.keys().then((keys) => Promise.all(keys.filter((k) => k !== CACHE).map((k) => caches.delete(k)))).then(() => self.clients.claim()));
});
const keep = (req) => fetch(req).then((res) => { if (res && (res.ok || res.type === 'opaque')) { const copy = res.clone(); caches.open(CACHE).then((c) => c.put(req, copy)); } return res; });
self.addEventListener('fetch', (e) => {
  const req = e.request;
  if (req.method !== 'GET') return;
  const url = new URL(req.url);
  // the sync library and the fonts: keep a copy so the app starts offline
  if (url.href.startsWith('https://www.gstatic.com/firebasejs/') || url.hostname === 'fonts.googleapis.com' || url.hostname === 'fonts.gstatic.com') {
    e.respondWith(caches.match(req).then((hit) => hit || keep(req)));
    return;
  }
  if (url.origin !== self.location.origin) return;
  if (url.pathname.endsWith('/version.json')) return; // always ask the network
  if (req.mode === 'navigate') {
    // a fresh copy when online, so updates arrive; the cached one when offline
    e.respondWith(fetch(req.url, { cache: 'no-cache', credentials: 'same-origin' }).then((res) => { const copy = res.clone(); caches.open(CACHE).then((c) => c.put('./index.html', copy)); return res; }).catch(() => caches.match('./index.html')));
    return;
  }
  // the config file: fresh when online, so turning sync on reaches everyone
  if (url.pathname.endsWith('/firebase-config.js')) { e.respondWith(keep(req).catch(() => caches.match(req))); return; }
  e.respondWith(caches.match(req).then((hit) => hit || keep(req)));
});
