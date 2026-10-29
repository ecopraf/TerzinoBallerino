# Il Terzino Ballerino 🕺⚽

Arcade web dedicato a **Luciano**, il Terzino Ballerino: schiva palloni e avversari,
raccogli gli **outfit improbabili** per caricare l'**ENERGIA**, e quando la barra è piena
entra in **BALLA MODE** e respinge tutto ballando. Attento al **Vater** (Claudio), il
moralista del pallone che entra in campo e bacchetta.

Gioco **single-file, zero dipendenze**: apri `index.html` e gioca. Funziona da telefono
e da desktop.

## 🎮 Come si gioca

| Azione | Comando |
|---|---|
| Salta (doppio salto) | `Spazio` / `↑` / tocco schermo |
| Muoviti (minigioco) | `◀ ▶` o frecce |

- 🏃 **Avversari** e 🔶 **coni**: ostacoli a terra.
- ⚽ **Palloni**: arrivano anche in alto.
- 🎩 **Outfit**: +25 punti e **+1 ENERGIA**. L'energia si accumula e non si consuma da sola.
- 🪩 **BALLA MODE**: a energia piena Luciano balla e respinge tutto. Ogni respinta consuma
  1 di energia.
- 🧓 **Vater**: tre bacchettate e sei richiamato in panchina.

## 🧓 Lezione del Vater (minigioco)

Claudio si pianta nel cerchio e carica la bacchetta: spostati tra tre corsie e salta per
finire fuori portata. Gli attacchi cambiano (centro, lato, tutto il campo) e la difficoltà
sale col punteggio. Record salvato in locale.

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
index.html              gioco completo (HTML + CSS + JS, nessuna dipendenza)
assets/player.png       Luciano  (foto ottimizzata, sfondo trasparente)
assets/coach.png        Claudio  (foto ottimizzata, sfondo trasparente)
LucianoBallerino.png    foto originale di Luciano
Claudio.png             foto originale di Claudio
```

Le foto originali restano come sorgente; in `assets/` ci sono le versioni ottimizzate
(ritagliate al contenuto e ridimensionate) usate dal gioco.

## 🏆 Classifica

I punteggi degli amici si salvano in `localStorage` sul dispositivo: passatevi il telefono
e sfidatevi.

## 🚀 Pubblicazione

Il workflow `pages.yml` pubblica il gioco su **GitHub Pages** ad ogni push su `main`.
In alternativa apri `index.html` in locale: non serve nessun server.
