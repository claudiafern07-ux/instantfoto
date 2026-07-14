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

  /* ---------- Any actual al peu ---------- */
  var yearEl = document.getElementById('year');
  if (yearEl) yearEl.textContent = new Date().getFullYear();
})();
