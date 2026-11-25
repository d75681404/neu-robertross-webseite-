# DECISIONS
- Statisches HTML/CSS/JS (früher festgelegt, kein Build, turbopress). Kein React/Tailwind.
- Originalpfade der Seiten beibehalten; keces_dl/sw_dl in download/download.html zusammengeführt.
- Texte: Das Abrufwerkzeug liefert nur Zitate, keine Volltexte. Wörtlich übernommen, was zitiert wurde; Lücken im Impressum-Haftungsausschluss sind gelb markiert („…“ + Hinweis), nichts wurde ergänzt oder erfunden.
- Chronik/News: historische Telefonnummer 08466-905030 (Aragon-Meldung 2003) unverändert aus dem Original.
- Impressum: USt-IdNr. DE812882927 und EAR-Nr. DE84907860 stammen aus dem Abruf der Originalseite, nicht von mir erfunden, aber per Werkzeug-Abruf gewonnen → mit dem Original abgleichen. „§ 10 Absatz 3 MDStV“ ist Originalwortlaut, rechtlich veraltet → prüfen lassen.
- Kontaktformular: Originalseite hatte KEIN Formular (nur Adresse, Telefon, E-Mail). Formular auf Ihren früheren Wunsch mit action=/_tp/form.php; Fallback per mailto. Datenschutz-Abschnitt dazu als „Neu“ markiert.
- Footer „© 2022 by Audiophile Produkte“ und Keces-Preisliste „Stand Januar 2022“ (Dateiname 8_2023) unverändert.
## Offene Punkte
1 Bilder manuell sichern. 2 Impressum/Datenschutz abgleichen (gelb). 3 Formular-Datenschutztext. 4 /_tp/form.php nach AI-Launch-Veröffentlichung testen. 5 Lighthouse + Externe Links prüfen.

## Änderungen 2026-11-10
- Produkte: nur Oberbegriffe (keine Modellbezeichnungen), alle 8 Kategorien als Kartenraster; Kategorien stammen aus dem Original. „Vorstufen/Streamer“ gibt es im Original nicht und wurden nicht erfunden.
- Bilder als Hintergrund (Hero, Kontakt-Band, Kategoriekarten) – nur Originalbilder per URL; ohne Bild bleibt ein dunkler Grund. Weitere Hintergrundbilder brauchen weitere Originaldateien.
- Akzentfarbe: NICHT geändert. Das Firmenlogo war nicht abrufbar (Original-Kopfbereich nutzt nur Button-Grafiken). Bitte Logo schicken oder Hex-Wert nennen; Anpassung in css/style.css, --accent und --accent-2.
- Startseite: Zeile „Unsere Marken“ vor „Produkte“ entfernt (Annahme: das war gemeint).
- Copyright: „© <aktuelles Jahr> Robert Ross Audiophile Produkte GmbH“, Jahr automatisch per JS (Fallback 2026). Rechtlich ist ein Jahr im Copyright-Hinweis nicht vorgeschrieben.
- SEO: Titel/Beschreibungen mit Suchbegriffen, canonical + og:url (https://www.robertross.de/…), JSON-LD Organisation (nur bekannte Daten), robots.txt, sitemap.xml, Alt-Texte. Keine unsichtbaren Keyword-Listen.
- News: Anleitung in .claude/NEWS_ANLEITUNG.md, Einfügemarke in news.html.
- 2026-11-10 Akzentfarbe jetzt Logo-Teal #327677 (aus dem gelieferten Logo gemessen), helle Variante #5fb0b1 für dunkle Flächen. Logo (freigestellt) als img/logo.png in der Navigation; vom Nutzer geliefert.
- 2026-11-10 Startseite: Abschnitt vor „Produkte“ (Absatz mit Kategorien + Bildkarten Eden Acoustics/oBravo HAMT-1) entfernt – das war mit „nimm das vor Produkte weg“ gemeint. SEO läuft weiter über Titel, Beschreibungen, JSON-LD und die Produktseite.

## Umbau 2026-11-10 (Ein-Seiten-Version)
- Alles auf die Startseite (index.html): Produkte, News, Über uns, Händler, Links, Support, Kontakt als Abschnitte mit Anker-Navigation. Impressum/Datenschutz bleiben eigene Seiten (rechtlich üblich).
- Alte Unterseiten (news.html, about.html, links.html, products/…, dealer/…, download/…) sind jetzt Weiterleitungen auf die passenden Anker (noindex, canonical auf Startseite), damit alte Links/Suchtreffer weiter funktionieren.
- Händler als Klapptexte: Kategorie „Keces Audio“ (47 Händler, nach PLZ sortiert) und Kategorie „Weitere Marken“ (oBravo, Straight Wire mit Links). Die Keces-Liste stammt von kecesaudio.de (Abruf 10.11.2026), nicht aus Ihrem alten Händlerbereich. Eingriffe: nur ein Satzzeichen („14. 42579“ → „14, 42579“); bei einem Händler wurde der Ansprechpartner (Personenname) weggelassen. Offensichtlich fehlerhafte Schreibweisen („PaInselstr.“) unverändert. oBravo/Straight-Wire-Listen waren für mich nicht abrufbar, nur Links. Regelmäßig abgleichen, die Liste veraltet.
- „Jetzt neu“-Plakette entfernt.
- Design: kein weißer Grund mehr (getöntes Teal-Grau bzw. dunkel), Glas-Karten, Logo-Wasserzeichen, Faktenband (Seit 1987 / 5 Marken / Ostseebad Prerow – nur belegbare Angaben), Originalbilder als Hintergründe.
- Dunkelmodus: folgt dem System, Umschalter in der Navigation, Wahl wird im Browser gespeichert.
- Offen: Direktlinks im Bereich „Links“ (Sonos, Slim Devices, Hantz und Partner, PSB, RMP4, VirtualDub) fehlen noch, im Text gelb markiert.
- Korrektur früherer Angabe: Es sind 24 News-Meldungen (nicht 25).
- 2026-11-10 Darstellung: standardmäßig automatisch nach Gerät; Umschalter wechselt Automatisch → Hell → Dunkel (Wahl wird gespeichert, 'Automatisch' löscht sie).
- 2026-11-10 Produktarten: 15 Kategorien-Karten, alle im gleichen Teal (Originalbilder nur dezent dahinter). Keces-Produktarten (Endstufen, Lineare DC-Netzteile, Balanced Isolation Power Conditioner, DAC/Kopfhörerverstärker/Vorstufe, Vollverstärker, Phonovorstufen, Zubehör) stammen von kecesaudio.de (Abruf 10.11.2026), nur Oberbegriffe. Für Eden Acoustics, oBravo, Pear Audio, Straight Wire waren die Herstellerseiten nicht abrufbar: dort nur die Arten aus Ihrer bisherigen Produktseite. Falls diese Marken mehr Arten haben: bitte ergänzen lassen.
- 2026-11-10 „Neuigkeiten“ und „Chronik“ zu einem Abschnitt „News & Chronik“ zusammengeführt (eine Zeitleiste, Klapptexte pro Jahr, 2012 bis 1987, neueste zuerst, 42 Einträge = 24 Meldungen + 18 Chronik). Doppelte Ereignisse (2003, 2006, 2007) bewusst beide behalten, jeweils mit Etikett „Meldung“ bzw. „Firmengeschichte“. Menüpunkt „Über uns“ entfällt; Anker #ueber-uns und about.html leiten auf den Abschnitt.
- 2026-11-10 Fließende Übergänge: Verläufe an Hero-Unterkante, hellen Bändern und Kontaktbereich, sanfter Moduswechsel (0,4 s).
- 2026-11-10 Überschrift „Kategorie Weitere Marken“ im Händlerbereich entfernt (Kommentar „entferne“).
- 2026-11-10 Links: Direktlinks zu Sonos, Slim Devices, Hantz und Partner, PSB, RMP4, VirtualDub aus der Originalseite robertross.de/links.html übernommen; Platzhalter entfernt. Offene Punkte „Links“ damit erledigt.
- 2026-11-10 Kopfzeile: vollständiger Firmenname „Robert Ross Audiophile Produkte GmbH“ (Zusatzzeile unter dem Logo-Schriftzug).
- 2026-11-10 Dekor: eigene Linienzeichnungen als Inline-SVG (Schallplatte mit Tonarm, Schallwellen, Kabel, Equalizer, Wellenringe, Punktraster) in allen Abschnitten; keine Fotos/KI-Bilder, folgen den Farb-Tokens (hell/dunkel), Plattendrehung nur ohne reduzierte Bewegung. Erzeugt durch gen/deco.py.
- 2026-11-11 Produkte: Logos/Bilder aus den Kacheln entfernt, Symbole je Kategorie (gen/icons.py), neu nach Signalweg sortiert (Quellen, Verstärkung, Wiedergabe, Strom & Verbindung) mit vier Farbfamilien; Scroll-Einblendung einheitlich (gleiche Dauer, ohne Versatz, läuft bei jedem Scrollen); weicherer Übergang vor Kontakt.
- 2026-11-11 Farben zurückgenommen: wieder nur Logo-Türkis (Farbfamilien-Tokens --c1..--c4 gleich); Symbole und Sortierung der Produkte bleiben.
- 2026-11-11 Animationen: Lesefortschrittsbalken, Parallaxe der Zeichnungen, atmende Schallwellen, tanzende Equalizer-Balken, pulsierende Wellenringe, wandernde Kabel-Signale, funkelndes Punktraster, schwebendes Logo, Glanz auf Buttons, Lichtkegel/Lift auf Produktkacheln, Schimmer auf Kennzahlen, pulsierende Zeitleistenpunkte. Alles nur ohne „Bewegung reduzieren“.
- 2026-11-11 Kennzahlen-Kästchen vor „Musik“: Textabstände vereinheitlicht (Flex, gleiche Zeilenhöhe, mittig).
- 2026-11-11 Hero: Plattenspieler im Hintergrund (Platte wird aufgelegt, Tonarm schwenkt ein, Platte dreht sich, Noten steigen auf; nur Zeichnung, kein Ton); Logo animiert (Eintritt, Schwingen, Schallringe). Reihenfolge: Händler vor News & Chronik (Menü, Footer, Abschnitte).
- 2026-11-11 Startbereich: Plattenspieler im Hintergrund (Platte wird aufgelegt, Tonarm schwenkt ein, Platte dreht sich, Noten steigen am Tonarm auf); Logo spielt: Noten steigen aus dem Horn, Schallbögen pulsieren. Nur Bildanimation, kein Ton (keine Audiodatei vorhanden). Bei „Bewegung reduzieren“ statisch.
- 2026-11-11 Entfernt: Ringe um das Logo, Schallbögen am Horn und die Wellenlinien im Startbereich und unter „Musik“.
- 2026-11-11 News & Chronik: alle Jahresblöcke standardmäßig zugeklappt; Auf-/Zuklappen aller Klapptexte (News, Händler) animiert (Höhe + Einblenden, 0,45 s), ohne Animation bei „Bewegung reduzieren“.
- 2026-11-11 News: alle 14 Jahresblöcke stecken in einem Gesamt-Klapptext „Alle News & Chronik anzeigen“ (zu, animiert); Jahre darin wieder einzeln aufklappbar.
- 2026-11-11 Rechtliches: Datenschutz um Kontaktformular/Anfrage (Entwurf), Cookies & lokaler Speicher, Externe Links, Hosting ergänzt; Formular-Checkbox mit Einwilligungstext; Impressum um Prüfhinweis (MDStV → MStV, § 5 DDG). Die Seite setzt keine Cookies, kein Tracking und keine Drittdienste → kein Cookie-Banner nötig (nur localStorage „theme“, § 25 Abs. 2 Nr. 2 TDDDG). Alle neuen Rechtstexte sind gelb als „bitte rechtlich prüfen“ markiert; Hosting/AV-Vertrag/Speicherdauer offen. Keine Rechtsberatung.
- 2026-11-11 Hover-Animationen (Menü, Karten, Händler, Links, Downloads, Klapptexte, Zeitleiste, Buttons), schwebende Hintergrundzeichen (Noten, Kopfhörer, Lautsprecher, Platte, Stecker u. a.), Maus-Parallaxe und Lichtkegel.
- 2026-11-12 Aufbau-Animation: Elemente fliegen beim Scrollen aus wechselnden Richtungen (links/rechts/unten/Zoom) mit kleinem Versatz an ihren Platz (gleiche Dauer 0,7 s); Kopfzeile und Menü fallen beim Laden ein; Zeichnungen und Hintergrundzeichen bauen sich je Abschnitt beim ersten Erscheinen auf. Nicht bei „Bewegung reduzieren“.
- 2026-11-12 Ruhige Ausführung nach neuem Auftrag („elegant, dezent, keine verspielten Effekte“): schwebende Hintergrundzeichen, Lichtkegel, Maus-Parallaxe, Kachel-Spotlight, Glanz/Schimmer, Wackeln und Drehen beim Hover entfernt; Plattenspieler im Startbereich, spielendes Logo, Fortschrittsbalken und Klapp-Animation bleiben; Einblenden einheitlich von unten (gleiche Dauer). Die entfernten Effekte stehen in der Git-Historie (Commit „Rechtliches: Datenschutz erweitert …“).
- 2026-11-12 Analyse/Verbesserung: Kontrast im hellen Modus (Eyebrow, Gruppenüberschriften, „ROSS“) auf ≥4,5:1 angehoben; 2 Bildlinks mit aria-label; Checkbox 22 px. Audit: keine Überläufe, Überschriften geordnet, alle Bilder mit alt.
- 2026-11-12 Bilder: Eden Acoustics und oBravo HAMT-1 (Originale von robertross.de, per Link) als Markenbilder im Produktbereich. Farben: Messing-Akzent (Linien, Eyebrow-Strich, Kartenkante), tieferes Dunkel mit Verlauf; Kontraste geprüft. Weitere Originalbilder (Kategorie-GIFs, 082002test.jpg) bewusst nicht genutzt (klein/veraltet).
- 2026-11-12 Farben: Grün nur noch als Akzent. Hintergründe neutral (hell warmgrau #ebeae7/#dedcd7, dunkel #0d0e0f/#151718), Karten und Linien neutral, Teal nur für Icons, Labels, Links, Buttons und feine Verläufe; Messing als Zweitakzent.
- 2026-11-12 Grün exakt wie Original-Logo: Akzent #327677 (aus dem Logo gemessen) für Buttons, Icons, Linien; Text-Grün im Hellen minimal dunkler (#2b6a6b) und im Dunklen heller (#4a9ea1, Logo im Dunkelmodus ebenso) nur wegen Lesbarkeit (WCAG AA). Alle früheren Mint-/Hellgrüntöne entfernt.
- 2026-11-13 Markenbereich: KECES-Bildergalerie (5 Bilder) mit technischen Daten aus der Broschüre 2019 (Tabellen im Aufklapper), Eden- und oBravo-Bild lokal als WebP. Hinweis: Broschüre nennt abweichende Vertriebsadresse (Denkendorf) – nicht übernommen, Prüfung offen. build2.py enthält diese Änderungen NICHT; index.html ab jetzt direkt pflegen.
- 2026-11-17 Anschrift Prerow vom Betreiber bestätigt (Denkendorf in KECES-Broschüre nicht übernommen). Alte robertross.de ist in der aktuellen Sitzung nicht abrufbar (Allowlist) – Haftungsabschnitte warten auf eingefügten Wortlaut.
- 2026-11-17 Kommentare: Markenlogos (KECES, Eden, oBravo) in Markenkarten; P6, S300+, P14 auf schwarzen Hintergrund (Freistellung/Levels), S300+ vollständig sichtbar (contain); Eden/oBravo nur nativ 620 px; Abstände Händler-Summary und Faktenband; Impressum-Haftungsabschnitte aus Standardvorlage ergänzt (gelb markiert).
- 2026-11-17 P6: Hintergrund nun per Maske (glatt, bläulich, vom Rand verbunden) schwarz, Gerät unverändert (vorherige Levels-Variante dunkelte das Gerät ab).
- 2026-11-17 KECES-Galerie: alle Bilder gleich groß (S300+ und P14 nicht mehr doppelt breit).
- 2026-11-17 KECES-Galerie: Layout zurück (S300+ doppelt breit), alle KECES-Bilder gleiche Höhe (300 px, mobil 240 px); Eden/oBravo unverändert.
- 2026-11-17 Logos Pear Audio, Straight Wire (nur Goldschrift, freigestellt, auf dunkler Fläche), Ferienhäuser Ostsee ergänzt; oBravo-Logo freigestellt (helle/dunkle Variante je Modus).
- 2026-11-18 Logos: bei allen Markenlogos Hintergrund entfernt (transparent); je eine Variante für hellen und dunklen Modus (Eden rot, Straight Wire Gold/abgedunkelt, Pear/Darss/KECES/oBravo Schrift hell bzw. dunkel).
- 2026-11-18 Straight-Wire-Logo aufgewertet: 4-fach hochgerechnet, Konturen geglättet, Gold als sauberer Verlauf (Form unverändert).
- 2026-11-18 Straight-Wire-Logo neu freigestellt: Buchstaben vollständig (Glanzstellen einbezogen, kleine Löcher gefüllt), echte Innenräume erhalten.
- 2026-11-23 Hintergrundbilder von Startseite (Eden, mit Text „NEU & exklusiv“) und Kontakt (HAMT-1) entfernt; Flächen bleiben dunkel mit sanftem Verlauf. Weniger Fremd-Bildabrufe.
- 2026-11-24: Einheitlicher Hintergrund (hell überall #fbfaf8, dunkel überall #0d0e0f); Produktfotos mit weißem Hintergrund im hellen Modus (S300+, P14, P6, Ephono+; S4/oBravo bleiben dunkel, Hintergrund nicht sauber freistellbar).
- 2026-11-24: Dezenter Hinweis im Footer „Alle Bilder sind Originale, keine KI-generierten Inhalte“ (freiwillig; Aussage muss zur Bildrechte-Klärung passen).
- 2026-11-24: Weiße Produktfoto-Varianten wieder entfernt; Fotos im hellen Modus wie Original (schwarz), Maße unverändert.
