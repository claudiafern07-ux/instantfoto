# Instant Foto — Web oficial

Web estàtica (HTML + CSS + JS pur) de l'estudi fotogràfic **Instant Foto** de Terrassa.
Preparada per a **GitHub Pages** (hosting gratuït).

## 📁 Estructura

```
instantfoto/
├── index.html            Home
├── impressio.html        Impressió de fotos (tarifes completes)
├── emmarcacions.html     Emmarcacions a mida
├── digitalitzacio.html   Digitalització de cintes (tarifes + FAQ)
├── revelat.html          Revelat de carrets
├── restauracio.html      Restauració (comparador abans/després)
├── regals.html           Regals personalitzats (tarifes)
├── botiga.html           Botiga (catàleg amb preus)
├── contacte.html         Contacte, mapa, horari i formulari→WhatsApp
├── css/styles.css        Sistema de disseny compartit
├── js/main.js            Menú mòbil, animacions, comparador, formularis WA
├── assets/               Logos optimitzats + favicon
├── sitemap.xml           Mapa del lloc per a Google
├── robots.txt
└── build.py              (Opcional) Generador de pàgines — per editar-les totes de cop
```

## 🚀 Publicar a GitHub Pages (5 minuts)

1. Crea un compte a [github.com](https://github.com) si no en tens.
2. Crea un repositori nou anomenat `instantfoto` (públic).
3. Puja **tots** els arxius d'aquesta carpeta (Add file → Upload files).
4. Ves a **Settings → Pages → Branch: main → Save**.
5. En 1-2 minuts la web estarà a `https://ELTEUUSUARI.github.io/instantfoto/`

### ⚠️ Després de publicar (important per al SEO)

Cerca i substitueix `USUARI.github.io/instantfoto` pel teu domini real a:
- Totes les pàgines `.html` (etiquetes `canonical` i `og:`)
- `sitemap.xml`
- `robots.txt`

Si edites `build.py` (variable `BASE`) i l'executes amb `python3 build.py`, es regeneren totes les pàgines de cop.

Després, dona d'alta el sitemap a [Google Search Console](https://search.google.com/search-console).

## 🌐 Domini propi (recomanat)

Un domini com `instantfoto.cat` (~12 €/any) millora molt el SEO local i la confiança.
GitHub Pages permet connectar-lo gratis: Settings → Pages → Custom domain.

## 📷 Substituir els placeholders per fotos reals

Els placeholders són `<div class="ph">emoji</div>`. Per posar una foto real:

```html
<!-- Abans -->
<div class="ph">📼</div>
<!-- Després -->
<img class="ph-img" src="assets/fotos/digitalitzacio.jpg" alt="Digitalització de cintes VHS a Terrassa">
```

I afegeix això a `css/styles.css`:
```css
.ph-img { width: 100%; aspect-ratio: 4/3; object-fit: cover; border-radius: 2px; }
```

Consell: fotos en JPG a 1200 px d'ample màxim i comprimides (squoosh.app), amb `alt` descriptiu amb paraula clau + Terrassa.

## ✏️ Canviar preus

Els preus són text pla dins de cada `.html` (taules `price-table` i targetes `price-card`).
Es poden editar amb qualsevol editor, fins i tot des del web de GitHub (icona del llapis).
