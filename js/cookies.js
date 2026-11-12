/* Instant Foto — mapa sota petició i avís de cookies.
   Google Analytics NOMÉS es carrega si hi ha un ID a IF_GA_ID i la persona accepta. */
(function () {
  'use strict';
  var GA_ID = (window.IF_GA_ID || '').trim();   /* es defineix a js/config.js */
  var KEY = 'if_cookie_consent';                /* 'granted' | 'denied' */

  function read() { try { return localStorage.getItem(KEY); } catch (e) { return null; } }
  function write(v) { try { localStorage.setItem(KEY, v); } catch (e) {} }

  /* ---------- Mapa sota petició ---------- */
  document.querySelectorAll('[data-map-src]').forEach(function (box) {
    var btn = box.querySelector('[data-map-load]');
    if (!btn) return;
    btn.addEventListener('click', function () {
      var f = document.createElement('iframe');
      f.src = box.getAttribute('data-map-src');
      f.title = 'Mapa: Instant Foto a Pl. Comte Guifré, Terrassa';
      f.referrerPolicy = 'no-referrer-when-downgrade';
      f.setAttribute('allowfullscreen', '');
      box.innerHTML = '';
      box.appendChild(f);
    });
  });

  /* ---------- Google Analytics (només amb consentiment) ---------- */
  function loadGA() {
    if (!GA_ID || window.__ifGA) return;
    window.__ifGA = true;
    var s = document.createElement('script');
    s.async = true;
    s.src = 'https://www.googletagmanager.com/gtag/js?id=' + encodeURIComponent(GA_ID);
    document.head.appendChild(s);
    window.dataLayer = window.dataLayer || [];
    window.gtag = function () { window.dataLayer.push(arguments); };
    window.gtag('js', new Date());
    window.gtag('config', GA_ID, { anonymize_ip: true });
  }

  function removeGACookies() {
    var host = location.hostname.replace(/^www\./, '');
    document.cookie.split(';').forEach(function (c) {
      var n = c.split('=')[0].trim();
      if (n === '_ga' || n.indexOf('_ga_') === 0 || n === '_gid') {
        ['', '.' + host].forEach(function (d) {
          document.cookie = n + '=; expires=Thu, 01 Jan 1970 00:00:00 GMT; path=/' + (d ? '; domain=' + d : '');
        });
      }
    });
  }

  function showBanner() {
    var b = document.createElement('div');
    b.className = 'cookie-banner';
    b.setAttribute('role', 'dialog');
    b.setAttribute('aria-label', 'Avís de cookies');
    b.innerHTML =
      '<p>Fem servir cookies de Google Analytics, només si ho acceptes, per saber quanta gent visita la web i millorar-la. ' +
      'Sense la teva acceptació no se\'n instal·la cap. <a href="cookies.html" style="text-decoration:underline">Més informació</a>.</p>' +
      '<div class="cookie-actions">' +
      '<button type="button" class="btn btn-outline" data-c="denied">Rebutjar</button>' +
      '<button type="button" class="btn btn-primary" data-c="granted">Acceptar</button></div>';
    document.body.appendChild(b);
    b.addEventListener('click', function (e) {
      var v = e.target && e.target.getAttribute && e.target.getAttribute('data-c');
      if (!v) return;
      write(v);
      if (v === 'granted') loadGA(); else removeGACookies();
      b.remove();
    });
  }

  if (GA_ID) {
    var c = read();
    if (c === 'granted') loadGA();
    else if (c !== 'denied') showBanner();
    /* enllaç «Gestionar cookies» (a la pàgina de cookies i al peu) */
    document.addEventListener('click', function (e) {
      var a = e.target.closest && e.target.closest('[data-cookie-settings]');
      if (!a) return;
      e.preventDefault();
      try { localStorage.removeItem(KEY); } catch (err) {}
      removeGACookies();
      if (!document.querySelector('.cookie-banner')) showBanner();
    });
  } else {
    document.querySelectorAll('[data-cookie-settings]').forEach(function (el) { el.hidden = true; });
  }
})();
