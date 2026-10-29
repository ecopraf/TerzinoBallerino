#!/usr/bin/env python3
"""Genera gioco.html: copia di index.html con le immagini di assets/ incorporate
come data URI, cosi' il gioco e' un unico file da mandare agli amici.

Uso:  python3 build_gioco.py
Va rilanciato ogni volta che si modifica index.html o si aggiunge un asset.
"""
import base64, os, re, sys

ROOT = os.path.dirname(os.path.abspath(__file__))
os.chdir(ROOT)

html = open('index.html', encoding='utf-8').read()

# tutti i riferimenti ad asset/*.png usati nel gioco
refs = sorted(set(re.findall(r"assets/[A-Za-z0-9_\-]+\.png", html)))

missing, embedded = [], 0
for ref in refs:
    if not os.path.exists(ref):
        missing.append(ref)
        continue
    b64 = base64.b64encode(open(ref, 'rb').read()).decode('ascii')
    html = html.replace(ref, f"data:image/png;base64,{b64}")
    embedded += 1

open('gioco.html', 'w', encoding='utf-8').write(html)

print(f"gioco.html generato: {embedded} immagini incorporate, "
      f"{os.path.getsize('gioco.html')//1024} KB")
if missing:
    print("asset non trovati (restano come percorso, il gioco usa il fallback):")
    for m in missing:
        print("  -", m)
