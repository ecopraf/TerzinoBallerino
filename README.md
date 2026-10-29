# Il Terzino Ballerino 🕺⚽

Arcade web dedicato a **Luciano**, il Terzino Ballerino: schiva palloni e avversari,
raccogli gli **outfit improbabili** per caricare l'**ENERGIA**, e quando la barra è piena
entra in **BALLA MODE** e respinge tutto ballando. Attento al **Vater** (Claudio), il
moralista del pallone che entra in campo e bacchetta.

Gioco **single-file, zero dipendenze**: apri `index.html` e gioca. Funziona da telefono
e da desktop.

## 👥 I personaggi

| Chi | Ruolo nel gioco |
|---|---|
| **Luciano** | il protagonista, in **due versioni**: *Ballerino* 🕺 e *Playboy* 😎 (si scelgono dal menu) |
| **Claudio** | la persona reale; in campo è il **Vater**, che entra e bacchetta |
| **Vater arbitro** | ogni tanto Claudio entra con il **completo da arbitro** 🟨 |
| **Marco** | il **portiere** 🧤: esce dai pali e para in tuffo, muovendosi su e giù (in scala coi rivali) |
| **Gli avversari** | 19 rivali 🏃 a figura intera, in scala con Luciano (Dario, Silvio, AnneX, John…) |
| **BonusAnnex** | il **bonus** 🎁 che *regala* energia: +2 (o 120 punti a barra piena) |

Le foto nuove si aggiungono come **sticker** da *Le mie foto*; per gli avversari basta
generare l'asset `assets/rival_<nome>.png`, aggiungere la riga in `MEDIA` e la rotazione
parte da sola.

## 🎮 Come si gioca

| Azione | Comando |
|---|---|
| Salta (doppio salto) | `Spazio` / `↑` / tocco schermo |
| Muoviti (minigioco) | `◀ ▶` o frecce |

- 🏃 **Avversari** e 🔶 **coni**: ostacoli a terra.
- ⚽ **Palloni**: arrivano anche in alto.
- 🧤 **Marco il portiere**: esce dai pali e para in tuffo — dagli il tempo giusto.
- 🎩 **Outfit**: +25 punti e **+1 ENERGIA**. L'energia si accumula e non si consuma da sola.
- 🎁 **BonusAnnex**: bonus raro che compare in alto e **regala +2 ENERGIA** (o 120 punti a
  barra piena). Non si schiva: si prende.
- 💥 **La barra è la tua vita**: ogni colpo toglie **1 ENERGIA**, poi hai un attimo di
  invulnerabilità. Si va avanti finché la barra è carica: a **zero** il prossimo colpo è
  fatale. Puoi sbagliare, ma non troppo.
- 🪩 **BALLA MODE**: a energia piena Luciano balla e respinge tutto. Ogni respinta consuma
  1 di energia.
- 🧓 **Vater**: tre bacchettate e sei richiamato in panchina.

## 🧓 Lezione del Vater (minigioco)

Claudio **non sta più fermo**: si sposta tra tre corsie, **ti segue** e continua a parlare
mentre cammina (battute sempre diverse). La bacchetta colpisce **solo la corsia dove si
trova lui**: spostati quando carica altrove, **salta** se ti sta addosso. La corsia in
rosso è quella che sta per colpire. Più il livello sale, più spesso ti insegue. Record
salvato in locale.

## 🗣️ Frasi dinamiche

Il Vater cambia tono su quattro fasce di punteggio: *scaldandosi*, *in fiducia*,
*in allarme*, *moralista furioso* (vedi `SCORE_TIERS` in `index.html`).

## 🖼️ Le tue foto

Menu → **Le mie foto**: carichi le immagini dal dispositivo (restano solo nel browser).
Meglio **PNG con sfondo trasparente**.

Se la foto ha lo sfondo pieno, usa **✂️ Ripulisci sfondo**:

1. **🪄 Auto angoli** — rimuove lo sfondo partendo dai quattro angoli (sfondi uniformi).
2. Oppure **tocca un punto** per prelevare quel colore, regola la tolleranza e premi
   **🧽 Rimuovi colore**. Ripeti per gli altri colori.
3. **↺ Ripristina** annulla, **✓ Usa questa** salva il PNG con la trasparenza.

## 📁 Struttura

```
index.html                        gioco completo (HTML + CSS + JS, nessuna dipendenza)
gioco.html                        versione tutto-in-uno (foto come data URI)
og-image.png                      anteprima social 1200x630
assets/player.png                 Luciano versione Ballerino
assets/player_playboy.png         Luciano versione Playboy
assets/coach.png                  Claudio / Vater
assets/referee.png                Vater versione arbitro
assets/keeper.png                 Marco il portiere
assets/rival_dario.png            Dario, avversario (uno dei 19 rivali)
assets/rival_silvio.png           Silvio, avversario
assets/rival_*.png                gli altri avversari (Ago, Angelo, AnneX, …)
assets/bonus_annex.png            BonusAnnex, il bonus che regala energia
LucianoOK.png                     foto originali (sorgente)
LucianoPlayboy.png
Claudio.png
ClaudioArbitroMinchione.png
MarcoPortiere.png
AvversarioDario.png
AvversarioSilvio.png
AvversarioAnneX.png
BonusAnnex.png
```

Il file **`gioco.html`** è la versione **tutto-in-uno** (immagini incorporate): si
rigenera con `python3 build_gioco.py` dopo ogni modifica a `index.html` o agli asset.

Le foto originali restano come sorgente; in `assets/` ci sono le versioni ottimizzate
(ritagliate al contenuto e ridimensionate) usate dal gioco.

## 🏆 Classifica

I punteggi degli amici si salvano in `localStorage` sul dispositivo: passatevi il telefono
e sfidatevi.

## 🚀 Giocare online

**Link ufficiale da condividere:**

👉 **https://ecopraf.github.io/TerzinoBallerino/**

È servito da **GitHub Pages** e si aggiorna da solo ad ogni push su `main` (entro ~1 minuto).

Incollando il link in chat appare l'**anteprima social** con titolo e immagine (`og-image.png`).

**Versione tutto-in-uno** (`gioco.html`): le foto sono incorporate come data URI, quindi è
un solo file senza dipendenze esterne — comodo da mandare come file singolo:

👉 https://htmlpreview.github.io/?https://raw.githubusercontent.com/ecopraf/TerzinoBallerino/main/gioco.html

**In locale:** apri `index.html` (o `gioco.html`) con doppio clic, nessun server necessario.

## 📤 Sfida l'amico

Dopo una partita premi **📤 Sfida l'amico**: il gioco prepara un messaggio con il tuo
punteggio e il link, e lo **copia negli appunti** (o apre il menu di condivisione nativo
sul telefono). Incollalo in chat e la sfida è lanciata.
