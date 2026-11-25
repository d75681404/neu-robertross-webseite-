# PROGRESS (Stand 2026-11-09)
## Fertig (Stand 2026-11-10: Ein-Seiten-Version, Dunkelmodus, Händler-Klapptexte, Teal-Design; Tests ALL OK)
- 9 Seiten, einheitliche Navigation/Fußzeile, responsive (Playwright: Desktop 1440, Tablet 820, Mobil 390; kein Overflow, keine JS-Fehler, 1×H1, 7 Navigationspunkte, 4 Fußspalten, alle internen Links vorhanden, Mobilmenü öffnet).
- Originalwortlaut übernommen: Startseite (vollständig), News (alle 25 Meldungen, Sätze aus Zitaten), Chronik (Datum + Zitatfragmente), Datenschutz (Abschnitte 1–3 weitgehend wörtlich), Impressum-Kopf.
- Formular getestet: Server-Endpunkt nicht erreichbar → E-Mail-Programm öffnet sich mit vorausgefüllter Nachricht; bei Antwort 200 (gemockt) → Erfolgsmeldung.
- Screenshots: screenshots/ (desktop-, tablet-, mobile-*).
## Offen (braucht Sie)
Siehe DECISIONS.md → „Offene Punkte“.
## Nicht geprüft
Lighthouse; externe Links (Netz gesperrt); echte Anzeige der Originalbilder; /_tp/form.php auf turbopress.
