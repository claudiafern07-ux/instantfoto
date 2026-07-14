# -*- coding: utf-8 -*-
"""Generador de pàgines Instant Foto — HTML estàtic per a GitHub Pages."""
import urllib.parse

WA = "34618642868"
BASE = "https://USUARI.github.io/instantfoto"  # ← actualitzar quan es publiqui

def wa_link(msg):
    return "https://wa.me/" + WA + "?text=" + urllib.parse.quote(msg)

WA_ICON = '<svg viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M12 2a10 10 0 0 0-8.6 15.1L2 22l5.1-1.3A10 10 0 1 0 12 2zm0 18.2c-1.6 0-3.1-.4-4.4-1.2l-.3-.2-3 .8.8-2.9-.2-.3a8.2 8.2 0 1 1 7.1 3.8zm4.6-6.1c-.3-.1-1.5-.7-1.7-.8-.2-.1-.4-.1-.6.1-.2.3-.7.8-.8 1-.1.2-.3.2-.5.1a6.7 6.7 0 0 1-3.4-3c-.3-.4 0-.5.1-.7l.4-.5c.1-.2.1-.3 0-.5l-.8-1.9c-.2-.5-.4-.4-.6-.4h-.5c-.2 0-.5.1-.7.3-.2.3-.9.9-.9 2.2s.9 2.5 1.1 2.7c.1.2 1.9 2.9 4.6 4 .6.3 1.1.4 1.5.6.6.2 1.2.2 1.6.1.5-.1 1.5-.6 1.7-1.2.2-.6.2-1.1.1-1.2 0-.1-.2-.2-.5-.3z"/></svg>'

NAV_SERVICES = [
    ("impressio.html", "Impressió de fotos"),
    ("emmarcacions.html", "Emmarcacions a mida"),
    ("digitalitzacio.html", "Digitalització de cintes"),
    ("revelat.html", "Revelat de carrets"),
    ("restauracio.html", "Restauració de fotos"),
    ("regals.html", "Regals personalitzats"),
]

def header(active):
    def cls(page):
        return ' class="active"' if page == active else ''
    services = "".join('<a href="%s">%s</a>' % (h, t) for h, t in NAV_SERVICES)
    service_pages = [h for h, _ in NAV_SERVICES]
    serv_active = ' class="active"' if active in service_pages else ''
    return f'''<header class="site-header">
  <div class="container header-inner">
    <a class="brand" href="index.html" aria-label="Instant Foto — Inici">
      <img src="assets/logo-horizontal.png" alt="Instant Foto — Estudi Fotogràfic a Terrassa" width="240" height="26">
    </a>
    <button class="nav-toggle" aria-expanded="false" aria-label="Obrir el menú"><span></span></button>
    <nav class="main-nav" aria-label="Navegació principal">
      <a href="index.html"{cls("index.html")}>Inici</a>
      <div class="nav-dropdown">
        <a href="index.html#serveis"{serv_active}>Serveis</a>
        <div class="dropdown-menu">{services}</div>
      </div>
      <a href="botiga.html"{cls("botiga.html")}>Botiga</a>
      <a href="contacte.html"{cls("contacte.html")}>Contacte</a>
      <a href="{wa_link("Hola! Us escric des de la web d'Instant Foto.")}" class="nav-cta" target="_blank" rel="noopener">WhatsApp</a>
    </nav>
  </div>
</header>'''

FOOTER = f'''<footer class="site-footer">
  <div class="container footer-grid">
    <div class="footer-brand">
      <img src="assets/logo-horizontal.png" alt="Instant Foto" width="200" height="22" loading="lazy">
      <p>Especialistes en conservar els teus records a Terrassa. Estudi fotogràfic de proximitat, amb tracte personal.</p>
      <p style="margin-top:12px">⭐ 5,0 a Google · 26 ressenyes<br>🏳️‍🌈 LGBTQ+ friendly · Propietàries dones</p>
    </div>
    <div>
      <h4>Serveis</h4>
      <ul class="footer-list">
        <li><a href="impressio.html">Imprimir fotos a Terrassa</a></li>
        <li><a href="emmarcacions.html">Emmarcacions a Terrassa</a></li>
        <li><a href="digitalitzacio.html">Digitalitzar VHS a Terrassa</a></li>
        <li><a href="revelat.html">Revelat de carrets a Terrassa</a></li>
        <li><a href="restauracio.html">Restauració de fotos antigues</a></li>
        <li><a href="regals.html">Regals personalitzats</a></li>
      </ul>
    </div>
    <div>
      <h4>Visita'ns</h4>
      <ul class="footer-list">
        <li>Pl. Comte Guifré, Local 1<br>08221 Terrassa (Barcelona)</li>
        <li><a href="tel:+34618642868">618 64 28 68</a></li>
        <li><a href="https://instagram.com/instant.foto" target="_blank" rel="noopener">@instant.foto</a></li>
      </ul>
    </div>
    <div>
      <h4>Horari</h4>
      <ul class="footer-list">
        <li>Dl–Dj: 9–14 h i 16–20 h</li>
        <li>Dv: 9–14 h</li>
        <li>Ds–Dg: tancat</li>
      </ul>
    </div>
  </div>
  <div class="container footer-bottom">
    <span>© <span id="year">2026</span> Instant Foto — Estudi Fotogràfic · Terrassa</span>
    <span><a href="contacte.html">Com arribar-hi</a> · <a href="{wa_link("Hola! Us escric des de la web d'Instant Foto.")}" target="_blank" rel="noopener">Escriu-nos per WhatsApp</a></span>
  </div>
</footer>
<a class="wa-float" href="{wa_link("Hola! Us escric des de la web d'Instant Foto.")}" target="_blank" rel="noopener" aria-label="Contactar per WhatsApp">{WA_ICON}</a>
<script src="js/main.js"></script>'''

SCHEMA = '''<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "LocalBusiness",
  "@id": "%(base)s/#negoci",
  "name": "Instant Foto — Estudi Fotogràfic",
  "image": "%(base)s/assets/logo-if.png",
  "url": "%(base)s/",
  "telephone": "+34618642868",
  "priceRange": "€€",
  "address": {
    "@type": "PostalAddress",
    "streetAddress": "Pl. Comte Guifré, Local 1",
    "addressLocality": "Terrassa",
    "postalCode": "08221",
    "addressRegion": "Barcelona",
    "addressCountry": "ES"
  },
  "geo": { "@type": "GeoCoordinates", "latitude": 41.5615, "longitude": 2.0114 },
  "openingHoursSpecification": [
    { "@type": "OpeningHoursSpecification", "dayOfWeek": ["Monday","Tuesday","Wednesday","Thursday"], "opens": "09:00", "closes": "14:00" },
    { "@type": "OpeningHoursSpecification", "dayOfWeek": ["Monday","Tuesday","Wednesday","Thursday"], "opens": "16:00", "closes": "20:00" },
    { "@type": "OpeningHoursSpecification", "dayOfWeek": "Friday", "opens": "09:00", "closes": "14:00" }
  ],
  "aggregateRating": { "@type": "AggregateRating", "ratingValue": "5.0", "reviewCount": "26" },
  "sameAs": ["https://instagram.com/instant.foto"],
  "makesOffer": [
    { "@type": "Offer", "name": "Impressió de fotos a Terrassa" },
    { "@type": "Offer", "name": "Emmarcacions a mida a Terrassa" },
    { "@type": "Offer", "name": "Digitalització de VHS i cintes a Terrassa" },
    { "@type": "Offer", "name": "Revelat de carrets a Terrassa" },
    { "@type": "Offer", "name": "Restauració de fotos antigues a Terrassa" },
    { "@type": "Offer", "name": "Regals personalitzats amb fotos a Terrassa" }
  ]
}
</script>''' % {"base": BASE}

def page(filename, title, description, body, active=None, extra_head=""):
    html = f'''<!DOCTYPE html>
<html lang="ca">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title}</title>
<meta name="description" content="{description}">
<link rel="canonical" href="{BASE}/{filename if filename != "index.html" else ""}">
<meta property="og:type" content="website">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{description}">
<meta property="og:image" content="{BASE}/assets/logo-if.png">
<meta property="og:locale" content="ca_ES">
<link rel="icon" type="image/png" href="assets/favicon.png">
<link rel="apple-touch-icon" href="assets/apple-touch-icon.png">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,600;0,700;1,500&family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="css/styles.css">
{extra_head}
</head>
<body>
{header(active or filename)}
<main>
{body}
</main>
{FOOTER}
</body>
</html>'''
    with open(filename, "w", encoding="utf-8") as f:
        f.write(html)
    print("✓", filename)

# ════════════════════════ Blocs reutilitzables ════════════════════════

def page_hero(eyebrow, h1, lead, wa_msg, wa_label, secondary=None):
    sec = f'\n      <a class="btn btn-light" href="{secondary[0]}">{secondary[1]}</a>' if secondary else ""
    return f'''<section class="page-hero">
  <div class="container">
    <span class="eyebrow">{eyebrow}</span>
    <h1>{h1}</h1>
    <p class="lead">{lead}</p>
    <div class="hero-actions" style="margin-top:30px">
      <a class="btn btn-wa" href="{wa_link(wa_msg)}" target="_blank" rel="noopener">{WA_ICON} {wa_label}</a>{sec}
    </div>
  </div>
</section>
<div class="filmstrip"></div>'''

def cta_band(h2, p, wa_msg, wa_label):
    return f'''<section class="cta-band">
  <div class="container">
    <h2>{h2}</h2>
    <p>{p}</p>
    <a class="btn btn-light" href="{wa_link(wa_msg)}" target="_blank" rel="noopener">{WA_ICON} {wa_label}</a>
  </div>
</section>'''

def price_rows(rows):
    return "".join(f"<tr><td>{r[0]}</td>" + "".join(f'<td class="num">{c}</td>' for c in r[1:]) + "</tr>" for r in rows)

# ════════════════════════ INDEX ════════════════════════

index_body = f'''
<section class="hero">
  <div class="container hero-inner">
    <div>
      <span class="eyebrow">Estudi fotogràfic · Terrassa</span>
      <h1>Especialistes en conservar els teus records</h1>
      <p class="lead">Impressió de fotos, emmarcacions a mida, digitalització de cintes VHS, revelat de carrets i restauració de fotos antigues. A la Pl. Comte Guifré de Terrassa, amb tracte de tota la vida.</p>
      <div class="hero-actions">
        <a class="btn btn-wa" href="{wa_link("Hola! Us escric des de la web d'Instant Foto.")}" target="_blank" rel="noopener">{WA_ICON} Escriu-nos per WhatsApp</a>
        <a class="btn btn-light" href="#serveis">Veure serveis</a>
      </div>
    </div>
    <div class="photo-stack" aria-hidden="true">
      <figure class="photo-print"><div class="ph">📼</div><figcaption>Estiu del 94</figcaption></figure>
      <figure class="photo-print"><div class="ph">📷</div><figcaption>L'àvia Maria</figcaption></figure>
      <figure class="photo-print"><div class="ph">🎞️</div><figcaption>Primer carret</figcaption></figure>
    </div>
  </div>
</section>
<div class="filmstrip"></div>

<div class="trust-strip">
  <div class="container trust-inner">
    <span class="trust-item"><span class="stars">★★★★★</span> <strong>5,0 a Google</strong> · 26 ressenyes</span>
    <span class="trust-item">🏳️‍🌈 LGBTQ+ friendly</span>
    <span class="trust-item">👩‍💼 Propietàries dones</span>
    <span class="trust-item">📍 Pl. Comte Guifré, Terrassa</span>
  </div>
</div>

<section class="section" id="serveis">
  <div class="container">
    <div class="section-head section-head--center reveal">
      <span class="eyebrow">Què fem</span>
      <h2>Tot per als teus records, en un sol lloc</h2>
    </div>
    <div class="services-grid">
      <a class="service-card reveal" href="impressio.html">
        <div class="ph">🖼️</div>
        <h3>Impressió de fotos</h3>
        <p>Tots els formats, acabat brillant o mat. Envia-les per WhatsApp i recull-les en 24–48 h. Des de 0,40 €/foto.</p>
        <span class="card-link">Imprimir fotos a Terrassa</span>
      </a>
      <a class="service-card reveal" href="emmarcacions.html">
        <div class="ph">🪞</div>
        <h3>Emmarcacions a mida</h3>
        <p>Marcs a mida per a fotos, làmines i llenços. També miralls personalitzats. Pressupost gratuït a botiga.</p>
        <span class="card-link">Emmarcacions a Terrassa</span>
      </a>
      <a class="service-card reveal" href="digitalitzacio.html">
        <div class="ph">📼</div>
        <h3>Digitalització de cintes</h3>
        <p>VHS, MiniDV, Hi8, Super 8, Beta, diapositives… Les teves cintes mai surten de la botiga. Des de 13 €/cinta.</p>
        <span class="card-link">Digitalitzar VHS a Terrassa</span>
      </a>
      <a class="service-card reveal" href="revelat.html">
        <div class="ph">🎞️</div>
        <h3>Revelat de carrets</h3>
        <p>Color des de 13,90 € i blanc i negre 18,90 €. Rebràs els arxius per WeTransfer en una setmana.</p>
        <span class="card-link">Revelat de carrets a Terrassa</span>
      </a>
      <a class="service-card reveal" href="restauracio.html">
        <div class="ph">🪄</div>
        <h3>Restauració de fotos antigues</h3>
        <p>Recuperem fotos esquinçades, esvaïdes o tacades. Des de 18 €, amb entrega en una setmana.</p>
        <span class="card-link">Restauració de fotos antigues</span>
      </a>
      <a class="service-card reveal" href="regals.html">
        <div class="ph">🎁</div>
        <h3>Regals personalitzats</h3>
        <p>Tasses, samarretes, imants, fusta, llenç, metacrilat i foam amb les teves fotos. Regals que emocionen.</p>
        <span class="card-link">Regals personalitzats a Terrassa</span>
      </a>
    </div>
  </div>
</section>

<section class="section section--navy">
  <div class="container">
    <div class="section-head section-head--center reveal">
      <span class="eyebrow" style="color:var(--cream-dark)">Així de fàcil</span>
      <h2>Com funciona</h2>
    </div>
    <div class="steps">
      <div class="step reveal">
        <h3>Escriu-nos per WhatsApp</h3>
        <p>Envia'ns les fotos o explica'ns què necessites al 618 64 28 68. Et confirmem preu i termini a l'instant.</p>
      </div>
      <div class="step reveal">
        <h3>Nosaltres ens n'encarreguem</h3>
        <p>Imprimim, emmarquem, digitalitzem o restaurem amb cura artesanal. Tot es fa aquí, a la botiga de Terrassa.</p>
      </div>
      <div class="step reveal">
        <h3>Recull-ho a la botiga</h3>
        <p>T'avisem quan estigui a punt. Paga per Bizum, transferència o a botiga, com et vagi millor.</p>
      </div>
    </div>
  </div>
</section>

<section class="section">
  <div class="container split">
    <div class="reveal">
      <span class="eyebrow">La botiga</span>
      <h2>També tenim carrets, càmeres i portarretrats</h2>
      <p class="lead" style="margin:16px 0 26px">Carrets Kodak i Fujifilm, càmeres analògiques d'un sol ús i reutilitzables, memòries USB i portarretrats de bambú, pedra i més. Reserva per WhatsApp i recull a botiga.</p>
      <a class="btn btn-primary" href="botiga.html">Veure la botiga</a>
    </div>
    <div class="ph ph--wide reveal">🛍️</div>
  </div>
</section>

{cta_band("Vine a veure'ns a la Pl. Comte Guifré",
          "Som a Terrassa, de dilluns a divendres. Si tens dubtes sobre qualsevol servei, escriu-nos i et responem de seguida.",
          "Hola! Tinc un dubte sobre els vostres serveis.",
          "Fes-nos la teva consulta")}
'''

page("index.html",
     "Instant Foto — Estudi Fotogràfic a Terrassa | Impressió, digitalització i emmarcacions",
     "Estudi fotogràfic a Terrassa: imprimir fotos, emmarcacions a mida, digitalitzar VHS, revelat de carrets, restauració de fotos antigues i regals personalitzats. ⭐ 5,0 a Google.",
     index_body, extra_head=SCHEMA)

# ════════════════════════ IMPRESSIÓ ════════════════════════

imp_body = page_hero("Impressió de fotos · Terrassa",
    "Imprimir fotos a Terrassa, fàcil i en 24–48 h",
    "Envia'ns les fotos per WhatsApp, tria mida i acabat (brillant o mat) i recull-les a la botiga en 24–48 hores. Paga per Bizum o transferència. Com més fotos, millor preu.",
    "Hola! Vull imprimir fotos. Us puc enviar els arxius per aquí?",
    "Envia les fotos per WhatsApp") + f'''

<section class="section">
  <div class="container">
    <div class="section-head reveal">
      <span class="eyebrow">Tarifes per unitat</span>
      <h2>Formats clàssics — preu segons quantitat</h2>
      <p class="lead">El preu per foto baixa a mesura que n'imprimeixes més.</p>
    </div>
    <div class="price-table-wrap reveal">
      <table class="price-table">
        <thead><tr><th>Mida</th><th class="num">1–4</th><th class="num">5–10</th><th class="num">11–20</th><th class="num">21–50</th><th class="num">51–99</th><th class="num">+100</th></tr></thead>
        <tbody>
          <tr><td>7×10 cm</td><td class="num">1,00 €</td><td class="num">0,80 €</td><td class="num">0,60 €</td><td class="num">0,45 €</td><td class="num" colspan="2">0,40 €</td></tr>
          <tr><td>9×13 cm</td><td class="num">1,20 €</td><td class="num">0,90 €</td><td class="num">0,65 €</td><td class="num">0,55 €</td><td class="num">0,45 €</td><td class="num">0,35 €</td></tr>
          <tr><td>10×15 cm</td><td class="num">1,20 €</td><td class="num">0,90 €</td><td class="num">0,70 €</td><td class="num">0,65 €</td><td class="num">0,60 €</td><td class="num">0,40 €</td></tr>
          <tr><td>13×18 cm</td><td class="num">1,70 €</td><td class="num">0,90 €</td><td class="num">0,80 €</td><td class="num">0,70 €</td><td class="num">0,60 €</td><td class="num">0,55 €</td></tr>
          <tr><td>15×20 cm</td><td class="num">1,70 €</td><td class="num">1,10 €</td><td class="num">0,80 €</td><td class="num">0,75 €</td><td class="num" colspan="2">0,70 €</td></tr>
        </tbody>
      </table>
    </div>
    <p class="price-note">Acabat brillant o mat, tu tries. Preus amb IVA inclòs.</p>
  </div>
</section>

<section class="section section--alt">
  <div class="container">
    <div class="section-head reveal">
      <span class="eyebrow">Grans formats</span>
      <h2>Ampliacions i pòsters</h2>
    </div>
    <div class="price-table-wrap reveal">
      <table class="price-table">
        <thead><tr><th>Mida</th><th class="num">Preu</th><th>Mida</th><th class="num">Preu</th></tr></thead>
        <tbody>
          <tr><td>18×24 / 18×26</td><td class="num">3,00 €</td><td>35×35</td><td class="num">6,25 €</td></tr>
          <tr><td>20×25</td><td class="num">2,90 €</td><td>35×50</td><td class="num">8,95 €</td></tr>
          <tr><td>20×30</td><td class="num">3,25 €</td><td>40×40</td><td class="num">8,20 €</td></tr>
          <tr><td>24×30</td><td class="num">4,15 €</td><td>40×50</td><td class="num">11,70 €</td></tr>
          <tr><td>24×36</td><td class="num">4,85 €</td><td>40×60</td><td class="num">12,80 €</td></tr>
          <tr><td>30×30</td><td class="num">4,75 €</td><td>50×50</td><td class="num">12,80 €</td></tr>
          <tr><td>30×40</td><td class="num">7,15 €</td><td>50×60</td><td class="num">16,00 €</td></tr>
          <tr><td>30×45</td><td class="num">8,05 €</td><td>50×70</td><td class="num">19,00 €</td></tr>
          <tr><td>30×50</td><td class="num">7,80 €</td><td>50×75</td><td class="num">19,50 €</td></tr>
          <tr><td>30×60</td><td class="num">9,40 €</td><td>50×80</td><td class="num">20,30 €</td></tr>
          <tr><td>30×70</td><td class="num">10,95 €</td><td>50×100</td><td class="num">21,95 €</td></tr>
          <tr><td>30×80</td><td class="num">12,50 €</td><td>60×90</td><td class="num">22,00 €</td></tr>
          <tr><td>30×90</td><td class="num">40,00 €</td><td>70×100</td><td class="num">32,90 €</td></tr>
          <tr><td></td><td class="num"></td><td>75×100</td><td class="num">34,90 €</td></tr>
        </tbody>
      </table>
    </div>
    <p class="price-note">A partir de 10 unitats en formats grans (20×30, 24×30, 30×40, 30×45), preu rebaixat: demana'ns-el per WhatsApp.</p>
  </div>
</section>

<section class="section">
  <div class="container split">
    <div class="ph ph--wide reveal">📲</div>
    <div class="reveal">
      <h2>Com fer la comanda</h2>
      <ul class="feature-list" style="margin-top:24px">
        <li>Envia les fotos per WhatsApp al <strong>618 64 28 68</strong></li>
        <li>Indica mida, quantitat i acabat (brillant o mat)</li>
        <li>Paga per Bizum o transferència</li>
        <li>Recull-les a la botiga en <strong>24–48 hores</strong></li>
      </ul>
    </div>
  </div>
</section>

{cta_band("Tens les fotos al mòbil? Ja gairebé les tens a les mans",
          "Envia-les ara per WhatsApp i demà o demà passat les reculls impreses a Terrassa.",
          "Hola! Vull imprimir fotos. Us puc enviar els arxius per aquí?",
          "Començar la comanda")}
'''

page("impressio.html",
     "Imprimir fotos a Terrassa | Recollida en 24–48 h — Instant Foto",
     "Imprimir fotos a Terrassa des de 0,35 €. Tots els formats, brillant o mat. Comanda per WhatsApp, pagament per Bizum i recollida a botiga en 24–48 h.",
     imp_body)

# ════════════════════════ EMMARCACIONS ════════════════════════

emm_body = page_hero("Emmarcacions a mida · Terrassa",
    "Emmarcacions a mida que fan justícia als teus records",
    "Marcs a mida per a fotografies, làmines, llenços, diplomes i objectes especials. També fem miralls personalitzats. Porta la peça a la botiga i t'assessorem amb un pressupost gratuït.",
    "Hola! Voldria un pressupost per emmarcar una peça. Quan puc passar per la botiga?",
    "Demana pressupost gratuït") + f'''

<section class="section">
  <div class="container split">
    <div class="reveal">
      <span class="eyebrow">Fet amb cura</span>
      <h2>Cada peça mereix el seu marc</h2>
      <p class="lead" style="margin:16px 0 26px">Treballem amb una àmplia gamma de motllures, paspartús i vidres per trobar la combinació que millor protegeixi i llueixi la teva peça.</p>
      <ul class="feature-list">
        <li>Marcs a mida per a qualsevol format</li>
        <li>Miralls personalitzats amb la motllura que triïs</li>
        <li>Paspartú i vidre a escollir</li>
        <li>Assessorament personal a la botiga</li>
        <li>Pressupost gratuït i sense compromís</li>
      </ul>
    </div>
    <div class="ph ph--tall reveal">🖼️</div>
  </div>
</section>

<section class="section section--alt">
  <div class="container">
    <div class="section-head section-head--center reveal">
      <span class="eyebrow">Procés</span>
      <h2>Com funciona</h2>
    </div>
    <div class="steps">
      <div class="step reveal"><h3>Porta la peça</h3><p>Vine a la botiga amb la foto, làmina o objecte que vulguis emmarcar. Si ho prefereixes, envia'ns una foto per WhatsApp per avançar feina.</p></div>
      <div class="step reveal"><h3>Tria amb nosaltres</h3><p>Et mostrem motllures i acabats i et donem un pressupost gratuït al moment.</p></div>
      <div class="step reveal"><h3>Recull la teva obra</h3><p>T'avisem quan el marc estigui llest. El resultat, com fet per a tu — perquè ho està.</p></div>
    </div>
  </div>
</section>

{cta_band("Tens una peça especial esperant marc?",
          "Envia'ns una foto per WhatsApp o passa per la botiga. El pressupost és gratuït.",
          "Hola! Voldria un pressupost per emmarcar una peça.",
          "Demanar pressupost")}
'''

page("emmarcacions.html",
     "Emmarcacions a mida a Terrassa | Miralls personalitzats — Instant Foto",
     "Emmarcacions a Terrassa: marcs a mida per a fotos, làmines i llenços, i miralls personalitzats. Pressupost gratuït a botiga. Pl. Comte Guifré, Terrassa.",
     emm_body)

# ════════════════════════ DIGITALITZACIÓ ════════════════════════

dig_body = page_hero("Digitalització · Terrassa",
    "Digitalitzar VHS a Terrassa: rescata els vídeos de casa",
    "Convertim les teves cintes VHS, VHS-C, MiniDV, Hi8, Video8, Super 8, Beta i Video 2000 a format digital, i també diapositives. Les cintes mai surten de la botiga: tot el procés es fa aquí, a Terrassa.",
    "Hola! Vull digitalitzar unes cintes. Us explico què tinc?",
    "Explica'ns què tens",
    secondary=("#tarifes", "Veure tarifes")) + f'''

<section class="section">
  <div class="container split">
    <div class="ph ph--wide reveal">📼</div>
    <div class="reveal">
      <span class="eyebrow">La nostra promesa</span>
      <h2>Les teves cintes mai surten de la botiga</h2>
      <p class="lead" style="margin:16px 0 26px">Molts serveis envien les cintes a laboratoris externs. Nosaltres no: digitalitzem aquí mateix, amb el màxim de cura, perquè aquells records són irreemplaçables.</p>
      <ul class="feature-list">
        <li>Tot el procés es fa a la botiga de Terrassa</li>
        <li>Formats: VHS, VHS-C, MiniDV, Hi8, Video8, Super 8, Beta i Video 2000</li>
        <li>També digitalitzem diapositives</li>
        <li>Entrega en USB o targeta de memòria (disponible a botiga)</li>
        <li>Servei d'edició de vídeo disponible (10 €)</li>
      </ul>
    </div>
  </div>
</section>

<section class="section section--alt" id="tarifes">
  <div class="container">
    <div class="section-head reveal">
      <span class="eyebrow">Tarifes</span>
      <h2>Preus de digitalització</h2>
      <p class="lead">Com més cintes portes, més barata surt cadascuna.</p>
    </div>
    <div class="price-table-wrap reveal">
      <table class="price-table">
        <thead><tr><th>Format</th><th class="num">Preu</th></tr></thead>
        <tbody>
          <tr><td>Cinta VHS, VHS-C, MiniDV, Hi8 o Video8 → USB</td><td class="num">15,00 € / cinta</td></tr>
          <tr><td>&nbsp;&nbsp;· A partir de 5 cintes</td><td class="num">14,00 € / cinta</td></tr>
          <tr><td>&nbsp;&nbsp;· A partir de 10 cintes</td><td class="num">13,00 € / cinta</td></tr>
          <tr><td>Cinta Beta o Video 2000 → USB</td><td class="num">20,00 € / cinta</td></tr>
          <tr><td>Super 8</td><td class="num">0,95 € / metre</td></tr>
          <tr><td>&nbsp;&nbsp;· A partir de 40 m</td><td class="num">0,90 € / metre</td></tr>
          <tr><td>&nbsp;&nbsp;· A partir de 80 m</td><td class="num">0,80 € / metre</td></tr>
          <tr><td>Diapositives</td><td class="num">0,40 € / unitat</td></tr>
          <tr><td>Edició de vídeo</td><td class="num">10,00 €</td></tr>
        </tbody>
      </table>
    </div>
    <p class="price-note">Necessites USB o targeta? En tenim a la <a href="botiga.html">botiga</a>: USB des de 9,50 € i targetes des de 7,50 €.</p>
  </div>
</section>

<section class="section">
  <div class="container">
    <div class="section-head section-head--center reveal"><span class="eyebrow">Dubtes freqüents</span><h2>Preguntes sobre digitalització</h2></div>
    <div class="faq reveal">
      <details><summary>No sé quants metres té la meva bobina de Super 8, com ho calculo?</summary><p>No et preocupis: porta-la a la botiga i la mesurem nosaltres al moment, sense compromís. Així sabràs el preu exacte abans de decidir.</p></details>
      <details><summary>Les cintes estan en mal estat, les podeu recuperar?</summary><p>Porta-les i les revisem. En molts casos, cintes amb fongs o trencades es poden recuperar parcialment o totalment. T'ho diem abans de començar.</p></details>
      <details><summary>En quin format rebo els vídeos?</summary><p>En arxius de vídeo digitals gravats en un USB o targeta de memòria. Si no en tens, a la botiga en venem des de 7,50 €.</p></details>
      <details><summary>Quant triga el servei?</summary><p>Depèn del volum de cintes. Quan ens les portis et donem un termini concret — i el complim.</p></details>
    </div>
  </div>
</section>

{cta_band("Aquelles cintes del calaix no s'esperaran per sempre",
          "El material magnètic es degrada amb els anys. Digitalitza els teus records abans que sigui tard — sense que surtin mai de Terrassa.",
          "Hola! Vull digitalitzar unes cintes. Us explico què tinc?",
          "Digitalitzar les meves cintes")}
'''

page("digitalitzacio.html",
     "Digitalitzar VHS a Terrassa | Cintes, Super 8 i diapositives — Instant Foto",
     "Digitalitzar VHS a Terrassa des de 13 €/cinta. VHS, MiniDV, Hi8, Super 8, Beta i diapositives. Les cintes mai surten de la botiga. Pl. Comte Guifré, Terrassa.",
     dig_body)

# ════════════════════════ REVELAT ════════════════════════

rev_body = page_hero("Revelat de carrets · Terrassa",
    "Revelat de carrets a Terrassa, amb ànima analògica",
    "Revelem els teus carrets de color i blanc i negre. En una setmana rebràs els arxius digitalitzats per WeTransfer, a punt per compartir o imprimir.",
    "Hola! Tinc un carret per revelar.",
    "Porta'ns el teu carret") + f'''

<section class="section">
  <div class="container">
    <div class="price-cards" style="grid-template-columns: repeat(2, 1fr); max-width: 720px; margin: 0 auto;">
      <div class="price-card reveal">
        <h3>Revelat color</h3>
        <div class="amount">13,90 <span>€</span></div>
        <p>Revelat digital del teu carret de color + arxius per WeTransfer en 1 setmana.</p>
      </div>
      <div class="price-card reveal">
        <h3>Revelat blanc i negre</h3>
        <div class="amount">18,90 <span>€</span></div>
        <p>Revelat B/N amb tota la cura que mereix + arxius per WeTransfer en 1 setmana.</p>
      </div>
    </div>
  </div>
</section>

<section class="section section--alt">
  <div class="container split">
    <div class="reveal">
      <span class="eyebrow">Com funciona</span>
      <h2>Del carret al núvol en una setmana</h2>
      <ul class="feature-list" style="margin-top:24px">
        <li>Porta el carret a la botiga (Pl. Comte Guifré, Terrassa)</li>
        <li>El revelem i escanegem amb cura</li>
        <li>En <strong>1 setmana</strong> reps l'enllaç de WeTransfer amb totes les fotos</li>
        <li>Si vols còpies en paper, les <a href="impressio.html">imprimim</a> des de 0,35 €</li>
      </ul>
    </div>
    <div class="ph ph--tall reveal">🎞️</div>
  </div>
</section>

<section class="section">
  <div class="container split">
    <div class="ph ph--wide reveal">📷</div>
    <div class="reveal">
      <span class="eyebrow">Tot per a l'analògic</span>
      <h2>Sense carret? En venem</h2>
      <p class="lead" style="margin:16px 0 26px">A la botiga trobaràs carrets Kodak Gold, Ultramax i Fujifilm, i càmeres analògiques d'un sol ús i reutilitzables. El cercle analògic complet, a Terrassa.</p>
      <a class="btn btn-primary" href="botiga.html">Veure carrets i càmeres</a>
    </div>
  </div>
</section>

{cta_band("El teu carret té ganes de veure la llum",
          "Passa per la botiga aquesta setmana i en una setmana tindràs les fotos al mòbil.",
          "Hola! Tinc un carret per revelar. Quan us el puc portar?",
          "Avisa que véns")}
'''

page("revelat.html",
     "Revelat de carrets a Terrassa | Color 13,90 € · B/N 18,90 € — Instant Foto",
     "Revelat de carrets a Terrassa: color 13,90 € i blanc i negre 18,90 €. Arxius digitals per WeTransfer en 1 setmana. També venem carrets i càmeres analògiques.",
     rev_body)

# ════════════════════════ RESTAURACIÓ ════════════════════════

res_body = page_hero("Restauració · Terrassa",
    "Restauració de fotos antigues: tornem la vida als records",
    "Fotos esquinçades, esvaïdes, tacades o amb parts perdudes. Les restaurem digitalment amb detall artesanal i te les entreguem en una setmana, a punt per imprimir o emmarcar.",
    "Hola! Voldria restaurar una foto antiga. Us envio una foto per valorar-la?",
    "Envia la foto per valorar-la") + f'''

<section class="section">
  <div class="container split">
    <div class="reveal">
      <span class="eyebrow">Mira-ho tu mateix</span>
      <h2>Abans i després</h2>
      <p class="lead" style="margin:16px 0 26px">Arrossega el control per veure la diferència. Cada restauració es treballa a mà, píxel a píxel, respectant l'essència de la foto original.</p>
      <ul class="feature-list">
        <li>Esquinços, plecs i taques</li>
        <li>Colors esvaïts o virats</li>
        <li>Reconstrucció de parts perdudes</li>
        <li>Entrega en <strong>1 setmana</strong></li>
      </ul>
    </div>
    <div class="ba-compare reveal" aria-label="Comparador d'abans i després de la restauració">
      <div class="ba-before">🕰️</div>
      <div class="ba-after">✨</div>
      <div class="ba-handle"></div>
      <span class="ba-label ba-label--before">Abans</span>
      <span class="ba-label ba-label--after">Després</span>
    </div>
  </div>
</section>

<section class="section section--alt">
  <div class="container">
    <div class="section-head section-head--center reveal">
      <span class="eyebrow">Tarifes</span>
      <h2>Segons la complexitat</h2>
      <p class="lead">Envia'ns una foto de la imatge per WhatsApp i et diem quin nivell és, sense compromís.</p>
    </div>
    <div class="price-cards">
      <div class="price-card reveal">
        <h3>Restauració fàcil</h3>
        <div class="amount">18 <span>€</span></div>
        <p>Petits desperfectes: taques lleus, ratllades superficials, ajust de contrast i color.</p>
      </div>
      <div class="price-card reveal">
        <h3>Restauració intermèdia</h3>
        <div class="amount">25 <span>€</span></div>
        <p>Esquinços, plecs marcats, zones esvaïdes o danys que afecten parts de la imatge.</p>
      </div>
      <div class="price-card reveal">
        <h3>Restauració complicada</h3>
        <div class="amount">40 <span>€</span></div>
        <p>Danys greus: parts perdudes, reconstrucció de rostres o fons, fotos molt deteriorades.</p>
      </div>
    </div>
  </div>
</section>

{cta_band("Aquella foto de l'àvia mereix una segona vida",
          "Fes-li una foto amb el mòbil i envia-nos-la. Et diem el preu exacte abans de començar.",
          "Hola! Voldria restaurar una foto antiga. Us envio una foto per valorar-la?",
          "Valorar la meva foto")}
'''

page("restauracio.html",
     "Restauració de fotos antigues a Terrassa | Des de 18 € — Instant Foto",
     "Restauració de fotos antigues a Terrassa: esquinços, taques i colors esvaïts. Des de 18 € i entrega en 1 setmana. Valoració gratuïta per WhatsApp.",
     res_body)

# ════════════════════════ REGALS ════════════════════════

reg_body = page_hero("Regals personalitzats · Terrassa",
    "Regals personalitzats amb les teves fotos",
    "Tasses, samarretes, imants, fusta, llenç, metacrilat i foam. Converteix la teva foto preferida en un regal que emociona. Fet a Terrassa, amb la qualitat d'un estudi fotogràfic.",
    "Hola! M'interessa un regal personalitzat. Us explico la idea?",
    "Explica'ns la teva idea") + f'''

<section class="section">
  <div class="container">
    <div class="section-head reveal">
      <span class="eyebrow">Els imprescindibles</span>
      <h2>Idees que sempre encerten</h2>
    </div>
    <div class="services-grid">
      <div class="service-card reveal">
        <div class="ph">☕</div>
        <h3>Tasses</h3>
        <p>La teva foto o disseny en una tassa. <strong>15 €</strong> — i a partir de 5 unitats, <strong>12 €</strong> cadascuna.</p>
      </div>
      <div class="service-card reveal">
        <div class="ph">👕</div>
        <h3>Samarretes i totebags</h3>
        <p>Estampació fotogràfica DTF: samarreta des de <strong>17,95 €</strong>, totebag des de <strong>16,90 €</strong>. Estampació petita, 5 €.</p>
      </div>
      <div class="service-card reveal">
        <div class="ph">🧲</div>
        <h3>Imants</h3>
        <p>Pack de 5 imants de 5 cm amb les teves fotos per <strong>20 €</strong>. Perfectes per a la nevera de casa dels avis.</p>
      </div>
    </div>
  </div>
</section>

<section class="section section--alt">
  <div class="container">
    <div class="section-head reveal">
      <span class="eyebrow">Per a les parets</span>
      <h2>Fotos en fusta, llenç, metacrilat i foam</h2>
      <p class="lead">Preus segons mida — aquí en tens una mostra. Consulta'ns qualsevol altra mida per WhatsApp.</p>
    </div>
    <div class="price-table-wrap reveal">
      <table class="price-table">
        <thead><tr><th>Mida</th><th class="num">Foam 10 mm</th><th class="num">Fusta</th><th class="num">Llenç</th><th class="num">Metacrilat 5 mm</th></tr></thead>
        <tbody>
          <tr><td>10×15</td><td class="num">6,50 €</td><td class="num">—</td><td class="num">—</td><td class="num">—</td></tr>
          <tr><td>15×20</td><td class="num">8,50 €</td><td class="num">20,50 €</td><td class="num">—</td><td class="num">—</td></tr>
          <tr><td>20×20</td><td class="num">—</td><td class="num">23,50 €</td><td class="num">34,50 €</td><td class="num">29,90 €</td></tr>
          <tr><td>20×30</td><td class="num">16,50 €</td><td class="num">29,50 €</td><td class="num">39,50 €</td><td class="num">35,90 €</td></tr>
          <tr><td>30×40</td><td class="num">36,50 €</td><td class="num">35,50 €</td><td class="num">47,50 €</td><td class="num">39,90 €</td></tr>
          <tr><td>40×60</td><td class="num">45,50 €</td><td class="num">55,50 €</td><td class="num">63,50 €</td><td class="num">54,90 €</td></tr>
          <tr><td>50×75</td><td class="num">65,50 €</td><td class="num">65,50 €</td><td class="num">75,50 €</td><td class="num">74,90 €</td></tr>
          <tr><td>70×100 / 75×100</td><td class="num">109,50 €</td><td class="num">115,00 €</td><td class="num">115,50 €</td><td class="num">120,90 €</td></tr>
        </tbody>
      </table>
    </div>
    <p class="price-note">També disponibles: llenç fins a 80×120 (135,50 €), fusta 60×90 (95 €), foto-cristall 10×15 (30,70 €) i 15×20 (57,34 €), i moltes mides intermèdies. Pregunta'ns!</p>
  </div>
</section>

<section class="section">
  <div class="container split">
    <div class="ph ph--wide reveal">🎁</div>
    <div class="reveal">
      <h2>Regals amb història</h2>
      <p class="lead" style="margin:16px 0 26px">Un regal personalitzat amb una foto ben triada val més que mil objectes comprats amb pressa. T'ajudem a triar el material i el format perquè quedi perfecte.</p>
      <a class="btn btn-wa" href="{wa_link("Hola! M'interessa un regal personalitzat. Us explico la idea?")}" target="_blank" rel="noopener">{WA_ICON} Demana consell per WhatsApp</a>
    </div>
  </div>
</section>

{cta_band("Un aniversari a la vista?",
          "Envia'ns la foto i et diem quin format hi quedarà millor. La majoria de regals estan a punt en pocs dies.",
          "Hola! M'interessa un regal personalitzat. Us explico la idea?",
          "Començar el meu regal")}
'''

page("regals.html",
     "Regals personalitzats amb fotos a Terrassa | Tasses, fusta, llenç — Instant Foto",
     "Regals personalitzats a Terrassa: tasses des de 12 €, samarretes, imants, foto en fusta, llenç, metacrilat i foam. Estudi fotogràfic a Pl. Comte Guifré, Terrassa.",
     reg_body)

# ════════════════════════ BOTIGA ════════════════════════

bot_body = page_hero("Botiga · Terrassa",
    "Carrets, càmeres i portarretrats",
    "Tot el que necessites per a la teva afició analògica i per lluir les teves fotos. Sense enviaments: reserva per WhatsApp i recull a la botiga de Terrassa.",
    "Hola! Voldria reservar un producte de la botiga.",
    "Reserva per WhatsApp") + f'''

<section class="section">
  <div class="container">
    <div class="section-head reveal"><span class="eyebrow">Analògic</span><h2>Carrets fotogràfics</h2></div>
    <div class="price-table-wrap reveal">
      <table class="price-table">
        <thead><tr><th>Producte</th><th class="num">Preu</th></tr></thead>
        <tbody>
          <tr><td>Kodak Gold 200 — 24 exposicions</td><td class="num">13,90 €</td></tr>
          <tr><td>Kodak Ultramax 400 — 24 exposicions</td><td class="num">14,90 €</td></tr>
          <tr><td>Fujifilm 200 — 36 exposicions</td><td class="num">15,90 €</td></tr>
          <tr><td>Kodak Gold 200 — 24 exp. · Bipack (2 carrets)</td><td class="num">21,90 €</td></tr>
          <tr><td>Kodak Ultramax 400 — 36 exp. · Tripack (3 carrets)</td><td class="num">39,90 €</td></tr>
        </tbody>
      </table>
    </div>
    <p class="price-note">Quan l'acabis, te'l <a href="revelat.html">revelem aquí mateix</a> per 13,90 €.</p>
  </div>
</section>

<section class="section section--alt">
  <div class="container">
    <div class="section-head reveal"><span class="eyebrow">Per disparar</span><h2>Càmeres</h2></div>
    <div class="price-cards" style="grid-template-columns: repeat(2, 1fr); max-width: 720px;">
      <div class="price-card reveal">
        <h3>Kodak d'un sol ús</h3>
        <div class="amount">24,90 <span>€</span></div>
        <p>27+12 exposicions. La companya perfecta per a festes, viatges i casaments.</p>
      </div>
      <div class="price-card reveal">
        <h3>Analògica reutilitzable</h3>
        <div class="amount">39,90 <span>€</span></div>
        <p>Càmera de carret reutilitzable: dispara, revela, recarrega i torna-hi.</p>
      </div>
    </div>
  </div>
</section>

<section class="section">
  <div class="container">
    <div class="section-head reveal"><span class="eyebrow">Per lluir-les</span><h2>Portarretrats</h2></div>
    <div class="price-table-wrap reveal">
      <table class="price-table">
        <thead><tr><th>Model</th><th class="num">Mida</th><th class="num">Preu</th></tr></thead>
        <tbody>
          <tr><td>Bambú</td><td class="num">10×15</td><td class="num">4,90 €</td></tr>
          <tr><td>Pedra</td><td class="num">10×15</td><td class="num">4,90 €</td></tr>
          <tr><td>Blanc PP</td><td class="num">10×15</td><td class="num">4,90 €</td></tr>
          <tr><td>Bambú</td><td class="num">13×18</td><td class="num">5,90 €</td></tr>
          <tr><td>Negre PP</td><td class="num">13×18</td><td class="num">5,90 €</td></tr>
          <tr><td>Curva</td><td class="num">13×18</td><td class="num">5,90 €</td></tr>
          <tr><td>Ondas</td><td class="num">15×20</td><td class="num">6,90 €</td></tr>
        </tbody>
      </table>
    </div>
  </div>
</section>

<section class="section section--alt">
  <div class="container">
    <div class="section-head reveal"><span class="eyebrow">Memòria digital</span><h2>USB i targetes</h2></div>
    <div class="price-table-wrap reveal">
      <table class="price-table">
        <thead><tr><th>Producte</th><th class="num">Preu</th></tr></thead>
        <tbody>
          <tr><td>Targeta 32 GB</td><td class="num">7,50 €</td></tr>
          <tr><td>Targeta 64 GB</td><td class="num">9,40 €</td></tr>
          <tr><td>USB 16 GB</td><td class="num">9,50 €</td></tr>
          <tr><td>USB 32 GB</td><td class="num">10,50 €</td></tr>
          <tr><td>USB 64 GB</td><td class="num">12,50 €</td></tr>
        </tbody>
      </table>
    </div>
    <p class="price-note">Ideals per emportar-te les teves <a href="digitalitzacio.html">cintes digitalitzades</a>.</p>
  </div>
</section>

{cta_band("Reserva-ho i passa a buscar-ho",
          "No fem enviaments: som una botiga de barri i ens agrada veure't la cara. Reserva el producte per WhatsApp i el tindràs a punt.",
          "Hola! Voldria reservar un producte de la botiga.",
          "Reservar producte")}
'''

page("botiga.html",
     "Botiga a Terrassa: carrets, càmeres analògiques i portarretrats — Instant Foto",
     "Botiga fotogràfica a Terrassa: carrets Kodak i Fujifilm, càmeres analògiques, portarretrats i USB. Reserva per WhatsApp i recull a Pl. Comte Guifré.",
     bot_body)

# ════════════════════════ CONTACTE ════════════════════════

con_body = f'''<section class="page-hero">
  <div class="container">
    <span class="eyebrow">Contacte · Terrassa</span>
    <h1>Vine a veure'ns o escriu-nos</h1>
    <p class="lead">Som a la Pl. Comte Guifré de Terrassa. Per a qualsevol dubte, pressupost o comanda, WhatsApp és el camí més ràpid.</p>
  </div>
</section>
<div class="filmstrip"></div>

<section class="section">
  <div class="container contact-grid">
    <div>
      <div class="contact-card reveal">
        <h3>On som</h3>
        <p><strong>Instant Foto — Estudi Fotogràfic</strong><br>Pl. Comte Guifré, Local 1<br>08221 Terrassa (Barcelona)</p>
        <p style="margin-top:14px">
          📞 <a href="tel:+34618642868">618 64 28 68</a><br>
          📸 <a href="https://instagram.com/instant.foto" target="_blank" rel="noopener">@instant.foto</a>
        </p>
        <a class="btn btn-wa" style="margin-top:18px" href="{wa_link("Hola! Us escric des de la web d'Instant Foto.")}" target="_blank" rel="noopener">{WA_ICON} Obrir WhatsApp</a>
      </div>
      <div class="contact-card reveal">
        <h3>Horari</h3>
        <table class="hours-table">
          <tr><td>Dilluns – Dijous</td><td>9–14 h · 16–20 h</td></tr>
          <tr><td>Divendres</td><td>9–14 h</td></tr>
          <tr><td>Dissabte i diumenge</td><td>Tancat</td></tr>
        </table>
      </div>
      <div class="contact-card reveal">
        <h3>Pagament</h3>
        <p>Bizum, transferència o pagament a botiga. Tu tries.</p>
      </div>
    </div>
    <div class="map-embed reveal">
      <iframe
        src="https://www.google.com/maps?q=Pla%C3%A7a+Comte+Guifr%C3%A9%2C+Local+1%2C+08221+Terrassa&output=embed"
        title="Mapa: Instant Foto a Pl. Comte Guifré, Terrassa"
        loading="lazy" referrerpolicy="no-referrer-when-downgrade" allowfullscreen></iframe>
    </div>
  </div>
</section>

<section class="section section--alt">
  <div class="container" style="max-width:720px">
    <div class="section-head section-head--center reveal">
      <span class="eyebrow">Pressupost ràpid</span>
      <h2>Explica'ns què necessites</h2>
      <p class="lead">Omple el formulari i s'obrirà WhatsApp amb el missatge preparat. Només hauràs de prémer "Enviar".</p>
    </div>
    <form class="wa-form contact-card reveal" data-wa-form data-wa-intro="Hola! Us escric des de la web per demanar un pressupost.">
      <label for="f-nom">Nom
        <input type="text" id="f-nom" name="nom" data-label="Nom" required autocomplete="name">
      </label>
      <label for="f-servei">Servei
        <select id="f-servei" name="servei" data-label="Servei" required>
          <option value="">Tria un servei…</option>
          <option>Impressió de fotos</option>
          <option>Emmarcació a mida</option>
          <option>Digitalització de cintes</option>
          <option>Revelat de carrets</option>
          <option>Restauració de fotos antigues</option>
          <option>Regal personalitzat</option>
          <option>Producte de botiga</option>
          <option>Altres</option>
        </select>
      </label>
      <label for="f-msg">Missatge
        <textarea id="f-msg" name="missatge" data-label="Missatge" placeholder="Explica'ns què necessites: quantes fotos, quines cintes, quina mida…" required></textarea>
      </label>
      <button type="submit" class="btn btn-wa" style="justify-content:center">{WA_ICON} Enviar per WhatsApp</button>
      <p class="price-note" style="text-align:center;margin-top:2px">S'obrirà WhatsApp amb el teu missatge a punt per enviar. No guardem cap dada.</p>
    </form>
  </div>
</section>
'''

page("contacte.html",
     "Contacte i ubicació | Instant Foto Terrassa — Pl. Comte Guifré",
     "Contacta amb Instant Foto a Terrassa: Pl. Comte Guifré, Local 1. WhatsApp 618 64 28 68. Horari: Dl–Dj 9–14 h i 16–20 h, Dv 9–14 h. Mapa i formulari de pressupost.",
     con_body, extra_head=SCHEMA)

print("Totes les pàgines generades.")
