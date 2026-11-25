# News einfügen (Ein-Seiten-Version)
News und Firmengeschichte stehen zusammen in `index.html` im Abschnitt `<section id="news">` („News & Chronik“), gruppiert nach Jahr in Klapptexten (`<details>`), neueste zuerst. Meldungen tragen das Etikett `<span class="tag">Meldung</span>` hinter der Datumszeile, Firmengeschichte `<span class="tag hist">Firmengeschichte</span>`.
1. Neue Meldung im Jahr-Block des aktuellen Jahres ganz oben in die Liste `<ol class="timeline">` einfügen. Gibt es das Jahr noch nicht, einen neuen `<details>`-Block (mit `open`) über den bisherigen setzen und bei dem bisher offenen `open` entfernen.
2. Vorlage für eine Meldung:
```html
<li><time>TT.MM.JJJJ</time><span class="tag">Meldung</span>
<h3>Überschrift (optional)</h3>
<p>Text der Meldung. <a href="https://…" rel="noopener">Link (optional)</a></p>
<img src="img/bild.jpg" alt="Beschreibung des Bildes" loading="lazy"> <!-- optional -->
</li>
```
3. Speichern und hochladen (bzw. über turbopress AI Launch neu veröffentlichen). Bilder in `img/` ablegen, immer mit alt-Text.
