import math
def vinyl():
    g="".join(f'<circle cx="200" cy="200" r="{r}"/>' for r in range(44,196,7))
    return ('<svg class="deco vinyl" viewBox="0 0 400 400" aria-hidden="true" focusable="false">'
            f'<g class="rec">{g}<path d="M200 60 A140 140 0 0 1 340 200" class="gloss"/><circle cx="200" cy="200" r="30" class="fill"/></g><circle cx="200" cy="200" r="3" class="solid"/>'
            '<path class="arm" d="M372 40 C 372 120 330 190 262 236"/>'
            '<circle cx="372" cy="40" r="9"/><rect class="solid" x="252" y="228" width="22" height="12" rx="2" transform="rotate(34 263 234)"/></svg>')

def turntable():
    g="".join(f'<circle cx="250" cy="220" r="{r}"/>' for r in range(46,176,7))
    return ('<svg class="deco tt tt-hero" viewBox="0 0 600 440" aria-hidden="true" focusable="false">'
      '<rect x="8" y="8" width="584" height="424" rx="20"/><circle cx="250" cy="220" r="186"/>'
      '<circle cx="62" cy="378" r="10"/><circle cx="62" cy="62" r="6"/><rect x="430" y="360" width="120" height="40" rx="8"/><circle cx="452" cy="380" r="9"/><path d="M480 380h54"/>'
      f'<g class="rec-drop"><g class="rec">{g}<path d="M250 70 A150 150 0 0 1 400 220" class="gloss"/><circle cx="250" cy="220" r="40" class="fill"/></g></g>'
      '<circle cx="250" cy="220" r="4" class="solid"/>'
      '<circle cx="520" cy="80" r="26"/><circle cx="520" cy="80" r="8" class="solid"/>'
      '<g class="tonearm"><path class="arm" d="M520 80 L322 292"/><path class="arm" d="M520 80 L548 46"/><rect class="solid" x="306" y="282" width="30" height="14" rx="3" transform="rotate(-47 322 292)"/></g>'
      '<text class="note n1" x="318" y="270">♪</text><text class="note n2" x="300" y="280">♫</text></svg>')
def wave(h=120, w=1200, amp=34, k=3, phase=0, n=3):
    paths=""
    for j in range(n):
        pts=[]
        for i in range(0, w+1, 10):
            y=h/2+ (amp-j*8)*math.sin((i/w)*math.pi*2*k+phase+j*0.7)*math.sin((i/w)*math.pi)
            pts.append(f"{i},{y:.1f}")
        paths+=f'<polyline points="{" ".join(pts)}"/>'
    return f'<svg class="deco wave" viewBox="0 0 {w} {h}" preserveAspectRatio="none" aria-hidden="true" focusable="false">{paths}</svg>'
def eq():
    hs=[30,62,44,90,70,110,58,84,38,66,98,50,76,34,60]
    bars="".join(f'<rect class="solid" x="{i*16}" y="{120-h}" width="9" height="{h}" rx="2"/>' for i,h in enumerate(hs))
    return f'<svg class="deco eq" viewBox="0 0 240 120" aria-hidden="true" focusable="false">{bars}</svg>'
def ripples():
    g="".join(f'<circle cx="300" cy="300" r="{r}"/>' for r in range(30,300,26))
    return f'<svg class="deco ripples" viewBox="0 0 300 300" aria-hidden="true" focusable="false">{g}</svg>'
def dots():
    return ('<svg class="deco dots" viewBox="0 0 220 220" aria-hidden="true" focusable="false">'
            + "".join(f'<circle class="solid" cx="{x*20+10}" cy="{y*20+10}" r="2"/>' for x in range(11) for y in range(11)) + '</svg>')
def cable():
    return ('<svg class="deco cable" viewBox="0 0 1200 220" preserveAspectRatio="none" aria-hidden="true" focusable="false">'
            '<path d="M0 150 C 200 20, 380 230, 600 120 S 1000 10, 1200 110"/>'
            '<path d="M0 165 C 200 35, 380 245, 600 135 S 1000 25, 1200 125"/>'
            '<path d="M0 180 C 200 50, 380 260, 600 150 S 1000 40, 1200 140"/></svg>')
PLACE={
 'id="top"': [turntable()],
}

import random
SYM={
 "n1":'<path d="M10 19V4c2 3.5 7 3.5 7 8"/><circle cx="7" cy="19" r="3.2" fill="currentColor"/>',
 "n2":'<path d="M9 18V5l10-2v13M9 9l10-2"/><circle cx="6.5" cy="18" r="3" fill="currentColor"/><circle cx="16.5" cy="16" r="3" fill="currentColor"/>',
 "hp":'<path d="M4 15v-3a8 8 0 0 1 16 0v3"/><rect x="3" y="14" width="5" height="7" rx="2"/><rect x="16" y="14" width="5" height="7" rx="2"/>',
 "sp":'<rect x="6" y="2" width="12" height="20" rx="2"/><circle cx="12" cy="7.5" r="2"/><circle cx="12" cy="15" r="4"/>',
 "vi":'<circle cx="12" cy="12" r="10"/><circle cx="12" cy="12" r="6.5"/><circle cx="12" cy="12" r="2" fill="currentColor"/>',
 "pl":'<path d="M8 3v5M16 3v5M6 8h12v3a6 6 0 0 1-12 0zM12 17v4"/>',
 "bs":'<path d="M5 20v-6M10 20V6M15 20v-10M20 20v-4"/>',
 "tt":'<rect x="2" y="5" width="20" height="14" rx="2"/><circle cx="9" cy="12" r="4"/><path d="M18 8l-3 5"/>',
}
def floaters(n, seed):
    r=random.Random(seed); keys=list(SYM); out=""
    for i in range(n):
        k=keys[(i+seed)%len(keys)]
        left=round(r.uniform(2,96),1); top=round(r.uniform(4,92),1); size=r.choice([26,32,40,52]); d=r.choice([-30,-18,-10,10,18,30])
        dur=round(r.uniform(9,18),1); dl=round(-r.uniform(0,dur),1); rot=r.choice([-14,-8,8,14,20])
        out+=(f'<span class="fl" style="--i:{i};left:{left}%;top:{top}%;--s:{size}px;--d:{d};--dur:{dur}s;--dl:{dl}s;--rot:{rot}deg">'
              f'<svg viewBox="0 0 24 24" aria-hidden="true" focusable="false">{SYM[k]}</svg></span>')
    return f'<div class="floaters" aria-hidden="true">{out}</div>'

def apply(html):
    import re
    for key, svgs in PLACE.items():
        m=re.search(r'<section[^>]*'+re.escape(key)+r'[^>]*>', html)
        assert m, key
        n = 7 if 'id="top"' in key else 8
        html=html[:m.end()]+"".join(svgs)+html[m.end():]
    return html
