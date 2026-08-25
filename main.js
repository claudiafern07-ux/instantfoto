/* INSTANT FOTO — interaccions compartides */
(function () {
  'use strict';

  var WA_NUMBER = '34618642868';

  /* ---------- Menú mòbil ---------- */
  var toggle = document.querySelector('.nav-toggle');
  var nav = document.querySelector('.main-nav');
  if (toggle && nav) {
    toggle.addEventListener('click', function () {
      var open = nav.classList.toggle('open');
      toggle.setAttribute('aria-expanded', open ? 'true' : 'false');
    });
    // Desplegable "Serveis" en mòbil: primer toc obre, segon navega
    var dd = document.querySelector('.nav-dropdown > a');
    if (dd) {
      dd.addEventListener('click', function (e) {
        if (window.matchMedia('(max-width: 860px)').matches) {
          var parent = dd.parentElement;
          if (!parent.classList.contains('open')) {
            e.preventDefault();
            parent.classList.add('open');
          }
        }
      });
    }
  }

  /* ---------- Animació d'entrada en fer scroll ---------- */
  if ('IntersectionObserver' in window) {
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (en) {
        if (en.isIntersecting) {
          en.target.classList.add('visible');
          io.unobserve(en.target);
        }
      });
    }, { threshold: 0.12 });
    document.querySelectorAll('.reveal').forEach(function (el) { io.observe(el); });
  } else {
    document.querySelectorAll('.reveal').forEach(function (el) { el.classList.add('visible'); });
  }

  /* ---------- Comparador abans/després ---------- */
  document.querySelectorAll('.ba-compare').forEach(function (box) {
    var after = box.querySelector('.ba-after');
    var handle = box.querySelector('.ba-handle');
    function setPos(clientX) {
      var r = box.getBoundingClientRect();
      var x = Math.min(Math.max(clientX - r.left, 0), r.width);
      var pct = (x / r.width) * 100;
      after.style.clipPath = 'inset(0 0 0 ' + pct + '%)';
      handle.style.left = pct + '%';
    }
    var dragging = false;
    box.addEventListener('pointerdown', function (e) { dragging = true; box.setPointerCapture(e.pointerId); setPos(e.clientX); });
    box.addEventListener('pointermove', function (e) { if (dragging) setPos(e.clientX); });
    box.addEventListener('pointerup', function () { dragging = false; });
    box.addEventListener('pointercancel', function () { dragging = false; });
  });

  /* ---------- Formularis → WhatsApp ----------
     Qualsevol formulari amb [data-wa-form] construeix un missatge
     amb els camps i obre WhatsApp amb el text predefinit. */
  document.querySelectorAll('form[data-wa-form]').forEach(function (form) {
    form.addEventListener('submit', function (e) {
      e.preventDefault();
      var intro = form.getAttribute('data-wa-intro') || 'Hola! Us escric des de la web.';
      var lines = [intro, ''];
      form.querySelectorAll('input, select, textarea').forEach(function (field) {
        if (!field.name || !field.value.trim()) return;
        var label = form.querySelector('label[for="' + field.id + '"]');
        var name = field.getAttribute('data-label') || (label ? label.childNodes[0].textContent.trim() : field.name);
        lines.push('*' + name + ':* ' + field.value.trim());
      });
      var url = 'https://wa.me/' + WA_NUMBER + '?text=' + encodeURIComponent(lines.join('\n'));
      window.open(url, '_blank', 'noopener');
    });
  });


  /* ---------- Protecció d'imatges ----------
     Dissuasió: bloqueja clic dret, arrossegar i el menú tàctil sobre imatges.
     No és una protecció absoluta (cap web pot impedir una captura de pantalla),
     però evita la descàrrega fàcil amb "Desa la imatge com a...". */
  document.addEventListener('contextmenu', function (e) {
    if (e.target.closest('img, .ph, .product-media, .photo-print, .ba-compare')) {
      e.preventDefault();
    }
  });
  document.addEventListener('dragstart', function (e) {
    if (e.target.tagName === 'IMG') e.preventDefault();
  });

  /* ---------- Bombolla d'avís en obrir la web ---------- */
  var bubble = document.querySelector('.intro-bubble');
  if (bubble) {
    var closed = false;
    try { closed = sessionStorage.getItem('if_bubble_closed') === '1'; } catch (err) {}
    if (!closed) {
      setTimeout(function () { bubble.classList.add('show'); }, 1800);
    }
    var closeBtn = bubble.querySelector('.bubble-close');
    if (closeBtn) {
      closeBtn.addEventListener('click', function () {
        bubble.classList.remove('show');
        try { sessionStorage.setItem('if_bubble_closed', '1'); } catch (err) {}
      });
    }
    // En clicar el botó de WhatsApp també es tanca
    var bubbleCta = bubble.querySelector('.btn');
    if (bubbleCta) {
      bubbleCta.addEventListener('click', function () {
        bubble.classList.remove('show');
        try { sessionStorage.setItem('if_bubble_closed', '1'); } catch (err) {}
      });
    }
  }

  /* ---------- Galeria de miniatures a la botiga ---------- */
  document.querySelectorAll('.product-card').forEach(function (card) {
    var main = card.querySelector('.product-media img');
    var thumbs = card.querySelectorAll('.product-thumbs button');
    if (!main || !thumbs.length) return;
    thumbs.forEach(function (btn) {
      btn.addEventListener('click', function () {
        var img = btn.querySelector('img');
        if (!img) return;
        main.src = img.src;
        main.alt = img.alt;
        thumbs.forEach(function (b) { b.removeAttribute('aria-current'); });
        btn.setAttribute('aria-current', 'true');
      });
    });
  });

  /* ---------- Any actual al peu ---------- */
  var yearEl = document.getElementById('year');
  if (yearEl) yearEl.textContent = new Date().getFullYear();
})();
