# Performance-Bericht

**Gemessen (Dateigrößen, unkomprimiert / gzip):** index.html 54,9 KB / 14,9 KB · style.css 37,2 KB / 9,5 KB · main.js 8,8 KB / 3,3 KB. Bilder lokal (`img/`): 432 KB gesamt, WebP, jeweils ≤ 1200 px, einzelne Dateien 20–113 KB. Keine Frameworks, keine Webfonts von Drittanbietern, keine Drittanbieter-Skripte. Lazy Loading und `decoding="async"` bei Inhaltsbildern.

**Nicht gemessen:** Lighthouse-Werte, LCP, CLS, INP (Werkzeug in der Umgebung nicht verfügbar). Die Ziele 90+/95+ sind Qualitätsziele, **keine bestätigten Ergebnisse**.

**Bekannte Punkte**
- Sieben Altbilder werden noch von robertross.de geladen (fremder Server, nicht optimiert) – besser lokal als WebP speichern (Dateien erforderlich).
- Caching und Kompression hängen vom Hosting ab.
