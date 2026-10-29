# Il Terzino Ballerino — note di progetto

Gioco web arcade in **un singolo file**: `index.html` (HTML + CSS + JS, **zero dipendenze**).
Deve restare apribile con doppio clic / servito staticamente.
`gioco.html` è la copia **tutto-in-uno** (foto incorporate come data URI) per condividerlo
come file singolo. **Va rigenerato ogni volta che si tocca `index.html` o gli asset.**

## Personaggi (da non confondere)
- **Luciano** — il protagonista, con **due versioni** selezionabili dal menu:
  - *Ballerino* → `assets/player.png` (da `LucianoOK.png`, guarda a destra)
  - *Playboy* → `assets/player_playboy.png` (da `LucianoPlayboy.png`, sfondo rimosso)
- **Claudio** — la persona reale. Foto: `Claudio.png` → `assets/coach.png`.
- **Vater** — il *ruolo* di Claudio nel gioco (il moralista che bacchetta).
  Variante casuale (~40%): **versione arbitro** → `assets/referee.png`.
- **Marco** — il portiere → `assets/keeper.png`. Ostacolo che **oscilla in verticale**
  (tipo "tuffo"), esce dai pali dopo i 12 s di gioco.
- **Dario** — primo avversario → `assets/rival_dario.png`. Ruota con `assets/rival.png`
  tramite `rivalKeys()`: **quando arrivano nuove foto basta generarne gli asset e
  aggiungere la chiave a `MEDIA` + `rivalKeys()`**, ruotano da sole.

## Asset
Le foto originali nel repo sono il sorgente; `assets/` contiene le versioni ottimizzate
(ritagliate al contenuto con alpha, ridimensionate a max 256 px, PNG ottimizzato).
Generazione: flood-fill dello sfondo dai bordi (solo per foto a sfondo pieno, es. Playboy)
→ alpha → `MinFilter(3)` per togliere l'alone → crop al bbox → resize LANCZOS.
Richiede `pillow` e `numpy`.

Per le immagini **composte** (es. `ClaudioArbitroMinchione.png` e `MarcoPortiere.png`
contengono una figura grande + una piccola, il "minchione"): si prende solo la
**componente connessa più grande** (`main_bbox`), scartando il resto.

## Rendering (`drawSticker`)
- `round=true` → clip circolare + bordo bianco (palloni, bonus).
- `round=false` → nessun clip, solo ombra morbida; **figure intere a figura intera**,
  ancorate ai piedi (`player.y-58`, `groundY-56`).
- L'aspect ratio è preservato con `Math.min(size/iw, size/ih)`.

## Trappole note
- `loadImg(m, src, cb)` ha una callback: `applyProfileToMedia` la usa per richiamare
  `refreshHero()` quando la foto di Luciano è pronta (altrimenti il menu resta sull'emoji).
- **Varianti di Luciano**: `MEDIA.player` serve sia il menu sia il gioco. La versione
  scelta è in `PROFILE.variant` (`tb_variant` in localStorage). Se l'utente carica una
  **foto personalizzata** (`customPlayerSrc()`), le due versioni si disabilitano e vince
  sempre la foto caricata.
- Il minigioco usa nodi DOM (`#mgPlayer`, `#mgVater`): `mgPaintFaces()` inietta le foto
  all'apertura e rispetta la variante arbitro (`MG.ref`). CSS `object-fit:contain`.
- Collisioni: il giocatore è un punto ai piedi (`player.y-26`), coerente con l'ancoraggio.
- Il portiere ha `o.y` **animato in `update()`** (non solo disegnato): la collisione usa
  `o.y` corrente, quindi anche l'hitbox segue il tuffo.

## Test
Harness in `/tmp`: `runner.js` + `game_testA.js` (17 test), `edtest.js` (editor),
`harness3.js` + `t_new.js` (25 test su varianti/avversari/portiere/arbitro/share).
Estrarre lo script da `index.html` e lanciare `node --check` per la sintassi.
Gli harness mockano il DOM: se si aggiungono elementi con `id`, **vanno aggiunti alla
lista `IDS`** degli harness, altrimenti `$(id).onclick` esplode.

## Pubblicazione
GitHub Pages è **ATTIVO** sul repo `ecopraf/TerzinoBallerino`:
- Sorgente: branch `main`, percorso `/` (build_type legacy)
- URL stabile: **https://ecopraf.github.io/TerzinoBallerino/**
- L'abilitazione di Pages **non** è possibile via API con il token di OpenHands
  (l'app non ha il permesso "Pages": 403 Resource not accessible by integration).
  Va fatta a mano: Settings → Pages → Source. Il workflow `pages.yml` pubblica solo
  se Pages è già attivo (`if: github.event.repository.has_pages`).

Ogni push su `main` aggiorna il sito entro ~1 minuto.

### Anteprima social
`index.html` ha i meta `og:*` e `twitter:*` che puntano a `og-image.png` (1200×630).
**Le immagini di anteprima richiedono URL assoluti**: se cambia dominio/repo vanno
aggiornati anche i meta e `share()` (che ha l'URL del link cablato).
