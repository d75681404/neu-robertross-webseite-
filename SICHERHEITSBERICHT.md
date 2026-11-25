# Sicherheitsbericht

**Im Projekt umgesetzt**
- Keine Drittanbieter-Skripte, keine Zugangsdaten oder API-Schlüssel im Quellcode.
- Externe Links mit `rel="noopener"`.
- Formular: clientseitige Validierung, Einwilligungs-Checkbox; Texte werden nie als HTML eingefügt (`textContent`).
- Nur ein Browser-Speicherzugriff: `localStorage` „theme“ (Hell/Dunkel).

**Nur am Server möglich (nicht umgesetzt, nicht getestet)**
- HTTPS-Erzwingung, HSTS, Content-Security-Policy, X-Content-Type-Options, Referrer-Policy, Permissions-Policy: Vorschlag in `docs/server-header.htaccess.txt`. Hoster und Server-Typ sind nicht bestätigt.
- **Serverseitige** Validierung, Spam-Schutz (z. B. Honeypot/Rate-Limit) und Mailversand des Formulars: Endpunkt `/_tp/form.php` (turbopress) wurde nicht von mir erstellt und nicht geprüft. Bis zu einem erfolgreichen Echttest gilt das Formular nicht als funktionsfähig; der `mailto:`-Fallback öffnet nur das E-Mail-Programm.

**Hinweis:** Die Inline-Skripte/-Styles erfordern in einer CSP vorerst `'unsafe-inline'`; strenger wäre ein Auslagern in Dateien.
