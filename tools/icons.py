def svg(inner): return f'<svg class="pico" viewBox="0 0 48 48" aria-hidden="true" focusable="false">{inner}</svg>'
BOX='<rect x="5" y="17" width="38" height="16" rx="3"/>'
ICONS={
 "Aktive Lautsprecher": svg('<rect x="13" y="5" width="22" height="38" rx="3"/><circle cx="24" cy="15" r="3"/><circle cx="24" cy="30" r="7"/><circle cx="24" cy="30" r="2"/><path d="M40 12l-4 7h5l-4 7" />'),
 "Passive Lautsprecher": svg('<rect x="13" y="5" width="22" height="38" rx="3"/><circle cx="24" cy="15" r="3"/><circle cx="24" cy="30" r="7"/><circle cx="24" cy="30" r="2"/>'),
 "Isodynamische Lautsprecher": svg('<rect x="15" y="4" width="18" height="38" rx="2"/><path d="M20 10v26M24 10v26M28 10v26"/><path d="M12 45h24"/>'),
 "Plattenspieler": svg('<rect x="4" y="9" width="40" height="30" rx="3"/><circle cx="19" cy="24" r="10"/><circle cx="19" cy="24" r="3"/><path d="M37 13c0 8-2 11-7 15"/><circle cx="37" cy="13" r="1.6"/>'),
 "Phonovorstufen": svg(BOX+'<circle cx="14" cy="25" r="4"/><circle cx="26" cy="25" r="2"/><path d="M33 25h5"/><path d="M12 10c3-3 6-3 9 0M12 5c6-4 11-4 17 0"/>'),
 "DACs": svg('<path d="M3 30h6v-10h6v14h6V14h6v16h6V22h6"/><path d="M3 41c5-8 9-8 14 0s9 8 14 0 9-8 14 0"/>'),
 "Vorstufen": svg(BOX+'<circle cx="16" cy="25" r="5"/><path d="M16 21v4"/><path d="M28 25h10M28 21h10M28 29h10"/>'),
 "Vollverstärker": svg(BOX+'<circle cx="13" cy="25" r="3.5"/><circle cx="25" cy="25" r="3.5"/><path d="M33 29l4-8 4 8z"/>'),
 "Endstufen": svg('<rect x="5" y="22" width="38" height="16" rx="3"/><path d="M10 14v8M16 12v10M22 12v10M28 12v10M34 14v8"/><circle cx="36" cy="30" r="2"/>'),
 "Kopfhörerverstärker": svg(BOX+'<circle cx="14" cy="25" r="4"/><circle cx="31" cy="25" r="3"/><path d="M38 25h2"/><path d="M14 10a10 10 0 0 1 20 0"/>'),
 "Kopfhörer": svg('<path d="M8 28V24a16 16 0 0 1 32 0v4"/><rect x="5" y="27" width="9" height="14" rx="3"/><rect x="34" y="27" width="9" height="14" rx="3"/>'),
 "Lineare Netzteile": svg(BOX+'<path d="M26 20l-5 6h6l-5 6"/><path d="M14 33v6M34 33v6"/>'),
 "Power Conditioner": svg('<rect x="4" y="16" width="40" height="16" rx="3"/><rect x="9" y="21" width="5" height="6" rx="1"/><rect x="18" y="21" width="5" height="6" rx="1"/><rect x="27" y="21" width="5" height="6" rx="1"/><circle cx="39" cy="24" r="1.6"/><path d="M8 32v4c0 4 4 4 4 8"/>'),
 "Kabel": svg('<rect x="3" y="19" width="7" height="10" rx="1"/><rect x="38" y="19" width="7" height="10" rx="1"/><path d="M10 24c8 0 6-12 14-12s6 24 14 24"/><path d="M10 24h0M38 24h0"/>'),
 "Zubehör": svg('<path d="M24 5l11 30H13z"/><path d="M9 40h30"/><path d="M17 26h14"/>'),
}
GROUPS=[("Quellen",1,["Plattenspieler","Phonovorstufen","DACs"]),
        ("Verstärkung",2,["Vorstufen","Vollverstärker","Endstufen","Kopfhörerverstärker"]),
        ("Wiedergabe",3,["Aktive Lautsprecher","Passive Lautsprecher","Isodynamische Lautsprecher","Kopfhörer"]),
        ("Strom & Verbindung",4,["Lineare Netzteile","Power Conditioner","Kabel","Zubehör"])]
