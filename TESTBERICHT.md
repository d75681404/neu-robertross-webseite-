# Testbericht (Stand 2026-11-17)

| Prüfung | Ergebnis | Status |
|---|---|---|
| Funktionstest `test4` (Chromium: Desktop 1280, Tablet, Mobil 390; Hell/Dunkel; Menü, Aufklapper, Theme-Umschalter, Anzahl Abschnitte) | „ALL OK“ | Technisch getestet |
| Seitenfehler (JS) Chromium | 0 | Technisch getestet |
| Lokale Bilder (`img/…`) laden | alle vollständig | Technisch getestet |
| Kontrast-/Name-/Überlauf-Audit (eigenes Skript, Mobil 390 px, Hell + Dunkel) | 0 Kontrastfehler, 0 Elemente ohne Namen, kein horizontaler Überlauf | Technisch getestet (kein axe-core) |
| Überschriftenfolge, Alt-Texte, Skip-Link, Fokus-Stil | vorhanden | Technisch getestet |
| Screenshots (Desktop/Tablet/Mobil, Hell/Dunkel) | in `screenshots/` | erstellt |
| Firefox, WebKit/Safari | Browser in der Umgebung nicht installiert | **Nicht getestet** |
| Lighthouse, axe-core, Chrome-DevTools-MCP | nicht installierbar (kein Netzzugang) | **Nicht getestet** |
| Externe Links / Downloads (PDFs von robertross.de) | Umgebung hat keinen Zugriff auf fremde Seiten | **Nicht getestet** |
| Kontaktformular: echter Versand | Endpunkt `/_tp/form.php` existiert erst auf dem Zielserver; Fallback: E-Mail-Programm (`mailto:`) | **Nicht getestet – Funktion nicht bestätigt** |
| Zoom 200 %, Screenreader (VoiceOver/NVDA) | – | **Nicht getestet** |
| Bilder von robertross.de (Altbilder) | in der Sandbox blockiert; auf der echten Seite abhängig von der alten Domain | **Nicht getestet** |
