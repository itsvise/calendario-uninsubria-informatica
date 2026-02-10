#!/bin/bash

# ================= CONFIGURAZIONE =================
# INCOLLA QUI IL TUO LINK iCal DELL'UNIVERSITÀ (tra le virgolette)
export CALENDAR_URL="https://unins.prod.up.cineca.it:443/api/FiltriICal/impegniICal?id=698b157358512a005f53a302"

# 1. Spostati nella cartella dove si trova questo script
cd "$(dirname "$0")"

# 2. Impostiamo il Python "LOCALE" (quello che abbiamo appena creato)
#    Invece di usare quello di sistema, usiamo quello nella cartella venv
PYTHON_CMD="./venv/bin/python"

# ==================================================

echo "--- Inizio aggiornamento: $(date) ---"

# 3. Esegui lo script Python usando il Python locale
if [ -f "$PYTHON_CMD" ]; then
    echo "Uso ambiente virtuale..."
    "$PYTHON_CMD" filter_calendar.py
else
    echo "ERRORE: Non trovo l'ambiente virtuale."
    echo "Esegui nel terminale: python3 -m venv venv && ./venv/bin/pip install -r requirements.txt"
    exit 1
fi

# 4. Carica su GitHub
echo "Caricamento su GitHub..."
git add custom_uni_calendar.ics
git commit -m "Aggiornamento automatico orario" || echo "Nessuna modifica rilevata"
git push

echo "--- Terminato con successo ---"