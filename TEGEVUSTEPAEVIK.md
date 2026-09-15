# Tegevuste päevik (Tic-Tac-Toe AI)

## Eesmärk
Luua graafilise liidesega (Tkinter) trips-traps-trull, kus mängija vastaseks on tehisintellekt. Kasutada Minimax algoritmi ning hiljem optimeerida seda Alpha-Beta lõikamisega.

## Rakenduse loomise etapid ja viibad
Kogu arendus toimus Antigravity keskkonnas, kus agent pidi järgima rangelt `GEMINI.md` failis defineeritud reegleid.
* **1. etapp (GUI ja loogika):** `Phase 1: Implement a standalone desktop Tic-Tac-Toe game in Python using the built-in 'tkinter' library. Create the core game logic (board state, win/draw conditions) and the graphical grid. Add basic unit tests for the core logic using the 'unittest' module. Do not implement the AI yet. Show the implementation plan and wait for my approval.`
* **2. etapp (AI ja algne profiilimine):** `Phase 2: Add an AI opponent to the game using the standard Minimax algorithm. Use the 'time' and 'tracemalloc' modules to profile and measure the execution time and peak memory usage of the AI's move calculation (especially for the first few moves). Output these exact resource metrics to the terminal. Wait for my approval.`
* **3. etapp (Optimeerimine):** `Phase 3: Optimize the AI by implementing Alpha-Beta pruning. Measure the compute time and memory usage again. Provide a clear, empirical comparison of the resource metrics before and after the optimization. Ensure the tkinter GUI remains responsive during AI calculations.`

## Ressursside optimeerimine
Tehisaru suutis programmi väga edukalt optimeerida. Lisaks lisas AI iseseisvalt taustalõime (`threading`), et graafiline liides (GUI) ei külmuks AI arvutuste ajal.

**Tulemused esimese käigu arvutamisel (tühjal laual):**
* **Enne optimeerimist (tavaline Minimax):** Aeg ~3207.42 ms, mälu ~8.43 KB.
* **Pärast optimeerimist (Alpha-Beta pruning):** Aeg ~82.74 ms, mälu ~8.52 KB.
* **Tulemus:** Arvutusaeg muutus ~38.7 korda kiiremaks! Järgmiste käikude puhul langes arvutusaeg drastiliselt (nt 346 ms -> 7 ms -> 0.6 ms), kuna otsingupuu muutus väiksemaks.

## Mured ja õnnestumised
**Õnnestumised:** Alpha-Beta lõikamine andis oodatust palju parema tulemuse ja muutis mängu täiesti sujuvaks. Tehisaru suutis iseseisvalt kirjutada adekvaatse `benchmark.py` skripti optimeerimise tõestamiseks.
**Mured:** Algse Minimaxi puhul võttis esimese käigu arvutamine liiga kaua aega, mis oleks ilma taustalõimeta (threading) rakenduse hetkeks lukustanud. Lisaks terminal antigravitys ei näinud pythoni aga tavalises powershell terminalis sain pythoni normaalselt käima.