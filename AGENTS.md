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
  (tipo "tuffo"), esce dai pali dopo i 12 s di gioco. La foto è un tuffo (ratio ~2.2:1),
  quindi è "largo e basso" di natura: `w=rand(90,114)`, `h=w*0.5`, disegnato
  `drawSticker(..., o.w*1.15)` → **~107x54..135x68px**. Prima era 66-84 (~76x35):
  troppo piccolo, sembrava un nano accanto ai rivali.
- **Dario** — primo avversario → `assets/rival_dario.png`.
- **Gli avversari** — tutte le foto `Avversario*.png` → `assets/rival_*.png`.
  Ruotano da sole tramite `rivalKeys()` (legge automaticamente tutte le chiavi
  `MEDIA` che iniziano con `rival_`): **quando arrivano nuove foto basta generarne
  l'asset `assets/rival_<nome>.png` e aggiungere la riga in `MEDIA`**, nessun altro
  intervento. Attualmente **19 avversari** (Ago, Angelo, AnneX, Claudione, Cori,
  Daniele, Dario, Gae, John, Luca, Luciano, Ludo, Marino, Nonny, Pietro, Raffaele,
  Sarra, Silvio, Speranzini). Sono disegnati con `drawStickerH(m, x, feetY, o.h)`:
  **l'altezza disegnata è esattamente `o.h`** (niente moltiplicatori nascosti, così
  hitbox e figura coincidono). `o.h = rand(112,132)`, cioè **in scala col
  protagonista** (disegnato a 120px): i rivali devono *sembrare persone*, non nani.
  Il salto ha apice ~156px, quindi restano superabili anche al massimo.
- **BonusAnnex** → `assets/bonus_annex.png`. **Non è un avversario**: è un bonus
  che *regala* energia. Vedi "Bonus Annex" qui sotto.

## Asset
Le foto originali nel repo sono il sorgente; `assets/` contiene le versioni ottimizzate
(ritagliate al contenuto con alpha, ridimensionate a max 256 px, PNG ottimizzato).
Generazione: flood-fill dello sfondo dai bordi (solo per foto a sfondo pieno, es. Playboy)
→ alpha → `MinFilter(3)` per togliere l'alone → crop al bbox → resize LANCZOS.
Richiede `pillow` e `numpy`.

Per le immagini **composte** (es. `ClaudioArbitroMinchione.png` e `MarcoPortiere.png`
contengono una figura grande + una piccola, il "minchione"): si prende solo la
**componente connessa più grande** (`main_bbox`), scartando il resto.

## Modello di danno: **l'energia è la vita**
Un colpo non uccide più: `takeHit(o)` toglie **1 di energia** e dà un attimo di
invulnerabilità (`G.invuln`). Si va avanti **finché la barra ha energia**; a zero il
prossimo colpo è fatale. Le bacchettate del Vater si contano a parte in `G.coachHits`
(tre = richiamato). Non reintrodurre la morte istantanea al primo urto.

## Bonus Annex
`BonusAnnex.png` → `assets/bonus_annex.png`, registrato in `MEDIA.annex`. Non è un
avversario: è un **bonus che regala energia**. Spawna raro (`G.annexTimer`, ogni 16–28 s)
**in alto** (`groundY-120..200`), dove non arrivano gli ostacoli di terra, così prenderlo
è una scelta e non un premio gratis. Alla raccolta (in `update()`, blocco `items`):
- **+2 energia** (o **+120 punti** se la barra è già piena, per non sprecarla);
- funziona **anche in BALLA MODE** (a differenza degli outfit, che lì non ricaricano);
- non fa mai danno. `it.annex` distingue bonus speciale e outfit normale.

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

## Menu e schermi piccoli (mobile)
Gli schermi `.screen` sono colonne flex con `overflow-y:auto`. **Non** usare
`justify-content:center` da solo su un contenitore che scorre: su schermi bassi il
contenuto in alto finisce *sopra* il bordo visibile e non è più raggiungibile (bug
"riquadro personaggio tagliato"). Soluzione adottata: `justify-content:flex-start` come
base + `@supports { justify-content: safe center }` per centrare solo quando c'è spazio.
Gli `.sticker` hanno `flex:none`, altrimenti la colonna flex li schiaccia a pochi pixel.
Regola generale: **se aggiungi contenuto in alto al menu, verifica a 320×480.**

## Test
Harness in `/tmp`: `runner.js` + `game_testA.js` (17 test), `edtest.js` (editor +
minigioco), `harness3.js` + `t_new.js` (26 test su varianti/avversari/portiere/arbitro/share),
`harness3.js` + `t_dmg.js` (modello di danno, Bonus Annex, rotazione avversari).
Estrarre lo script da `index.html` e lanciare `node --check` per la sintassi.
Gli harness mockano il DOM: se si aggiungono elementi con `id`, **vanno aggiunti alla
lista `IDS`** degli harness, altrimenti `$(id).onclick` esplode. La lista `IDS` si può
rigenerare con: `id="..."` + `$('...')` estratti da `index.html`.

### Rigenerare gli hook di test
Gli harness caricano `game_hooks.js`: copia dello script con, **subito prima della
chiusura della IIFE** (`s.rfind('})();')`), l'oggetto `globalThis.__test={...}`.
Se i test falliscono con `T.<qualcosa> is not a function`, quasi sempre manca quella
voce nell'elenco degli hook — non è un bug del gioco.

## Build del file unico
`python3 build_gioco.py` genera `gioco.html` incorporando **tutti** gli `assets/*.png`
citati in `index.html` come data URI. Non serve altro: aggiunge da sé le nuove immagini.
Se un asset citato non esiste, lo segnala e lascia il percorso (il gioco usa l'emoji di
fallback). `ball/item/logo` sono citati ma **non esistono di proposito** (emoji).

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
