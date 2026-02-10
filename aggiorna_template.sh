#!/bin/bash

# ================= CONFIGURAZIONE =================
# INCOLLA QUI SOTTO IL TUO LINK iCal DELL'UNIVERSITÀ
export CALENDAR_URL="INSERISCI_QUI_IL_TUO_LINK_ICAL"

# Percorso Python (di solito va bene questo, altrimenti verifica con 'which python3')
PYTHON_CMD="./venv/bin/python"
# ==================================================

cd "$(dirname "$0")"

# Attiva l'ambiente virtuale ed esegue
if [ -f "$PYTHON_CMD" ]; then
    echo "--- Inizio aggiornamento: $(date) ---"
    "$PYTHON_CMD" filter_calendar.py
    
    # Git Push
    git add custom_uni_calendar.ics
    git commit -m "Aggiornamento automatico orario" || echo "Nessuna modifica"
    git push
else
    echo "ERRORE: Ambiente virtuale non trovato. Esegui prima l'installazione."
fi