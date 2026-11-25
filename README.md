# Robert Ross Audiophile Produkte GmbH – Website (lokale Überarbeitung)

Statische Website ohne Framework und ohne Build-Schritt. **Nicht veröffentlicht** – Stand ist ein lokaler Entwurf zur Freigabe.

## Struktur
- `index.html` – Einseiter (Start, Produkte, Händler, News & Chronik, Links, Support, Kontakt)
- `impressum.html`, `datenschutz.html` – Rechtstexte (Entwurf, offene Stellen gelb markiert)
- `about.html`, `links.html`, `news.html`, `dealer/`, `products/`, `download/` – Weiterleitungsseiten der alten Adressen
- `css/style.css`, `js/main.js`, `img/` (Logo, `img/marken/` WebP-Bilder), `robots.txt`, `sitemap.xml`
- `docs/server-header.htaccess.txt` – Vorschlag für Sicherheits-Header (Hoster nötig)
- `.claude/` – Agenten, Entscheidungen (`DECISIONS.md`), Fortschritt, Plan

## Lokal ansehen
`python3 -m http.server 8765` im Projektordner, dann http://localhost:8765/ öffnen.

## Tests
Playwright (Chromium) Test- und Audit-Skripte liegen außerhalb des Projekts in der Arbeitsumgebung; Ergebnisse stehen im `TESTBERICHT.md`.

## Pflege
`index.html` wird direkt bearbeitet (der frühere Generator ist nicht mehr maßgeblich). Farben/Abstände zentral in `css/style.css` (`:root`-Variablen).

## Dokumentation
CHANGELOG.md · TESTBERICHT.md · RECHTLICHE_PRUEFUNG.md · BILDRECHTE_PRUEFUNG.md · SEO_BERICHT.md · PERFORMANCE_BERICHT.md · SICHERHEITSBERICHT.md · OFFENE_PUNKTE.md
