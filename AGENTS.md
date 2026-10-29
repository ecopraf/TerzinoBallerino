# Il Terzino Ballerino — note di progetto

Gioco web arcade in **un singolo file**: `index.html` (HTML + CSS + JS, **zero dipendenze**).
Deve restare apribile con doppio clic / servito staticamente.

## Personaggi (da non confondere)
- **Luciano** — il protagonista. Foto: `LucianoOK.jpg` → `assets/player.png` (guarda a destra).
- **Claudio** — la persona reale. Foto: `Claudio.png` → `assets/coach.png`.
- **Vater** — il *ruolo* di Claudio nel gioco (il moralista che bacchetta).

## Asset
Le foto originali nel repo sono il sorgente; `assets/` contiene le versioni ottimizzate
(ritagliate al contenuto con alpha, ridimensionate a max 256 px, PNG ottimizzato).
Generazione: flood-fill del bianco dai bordi → alpha → `MinFilter(5)` per togliere l'alone
JPEG → crop al bbox → resize LANCZOS. Richiede `pillow` e `numpy`.

## Rendering (`drawSticker`)
- `round=true` → clip circolare + bordo bianco (palloni, bonus).
- `round=false` → nessun clip, solo ombra morbida; **figure intere a figura intera**,
  ancorate ai piedi (`player.y-58`, `groundY-56`).
- L'aspect ratio è preservato con `Math.min(size/iw, size/ih)`.

## Trappole note
- `loadImg(m, src, cb)` ha una callback: `applyProfileToMedia` la usa per richiamare
  `refreshHero()` quando la foto di Luciano è pronta (altrimenti il menu resta sull'emoji).
- Il minigioco usa nodi DOM (`#mgPlayer`, `#mgVater`): `mgPaintFaces()` inietta le foto
  all'apertura. Il CSS usa `object-fit:contain`, non `cover`.
- Collisioni: il giocatore è un punto ai piedi (`player.y-26`), coerente con l'ancoraggio.

## Test
Harness in `/tmp`: `runner.js` + `game_testA.js` (17 test) ed `edtest.js` (editor).
Estrarre lo script da `index.html` e lanciare `node --check` per la sintassi.

## Pubblicazione
`ecopraf/TerzinoBallerino` (branch `main`) è il repo pubblico. Il workflow
`.github/workflows/pages.yml` pubblica su GitHub Pages **solo se** Pages è già abilitato
(`if: github.event.repository.has_pages`): il token dell'integrazione non può crearlo.

## Pubblicazione (aggiornato)

GitHub Pages e ATTIVO sul repo `ecopraf/TerzinoBallerino`:
- Sorgente: branch `main`, percorso `/` (build_type legacy)
- URL stabile: https://ecopraf.github.io/TerzinoBallerino/
- L'abilitazione di Pages NON e possibile via API con il token di OpenHands
  (l'app non ha il permesso "Pages": 403 Resource not accessible by integration).
  Va fatta a mano: Settings -> Pages -> Source.

`gioco.html` = versione tutto-in-uno con le foto incorporate come data URI
(assets/player.png e assets/coach.png). Utile per condividere il gioco come
singolo file, es. via htmlpreview.github.io.
