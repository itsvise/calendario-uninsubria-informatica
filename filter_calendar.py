import os
import requests
from ics import Calendar

# ================= CONFIGURAZIONE =================
# Aggiungi qui, tra virgolette, i nomi (o parti del nome) delle materie che NON vuoi.
# Il filtro non fa distinzione tra maiuscole e minuscole.
MATERIE_DA_RIMUOVERE = [
    "MODELLI INNOVATIVI PER LA GESTIONE DEI DATI",
    "PROGRAMMAZIONE PROCEDURALE E AD OGGETTI",
    "BASI DI DATI II"
]

NOME_FILE_OUTPUT = "custom_uni_calendar.ics"
# ==================================================

def main():
    # 1. Recupera l'URL in modo sicuro dalle variabili d'ambiente (GitHub Secrets)
    url_universita = os.environ.get("CALENDAR_URL")

    if not url_universita:
        print("ERRORE: Non ho trovato la variabile 'CALENDAR_URL'.")
        print("Assicurati di aver aggiunto il Secret nelle impostazioni della Repo.")
        exit(1)

    try:
        print("--- Inizio Scaricamento Calendario ---")
        response = requests.get(url_universita)
        response.raise_for_status() # Blocca se il link non funziona (es. errore 404)
        
        # Analizza il calendario originale
        cal_originale = Calendar(response.text)
        cal_pulito = Calendar()
        
        eventi_rimossi = 0
        eventi_tenuti = 0

        print(f"Trovati {len(cal_originale.events)} eventi totali. Inizio filtraggio...")

        for evento in cal_originale.events:
            # Controllo se il nome dell'evento contiene una delle parole vietate
            # .upper() serve a ignorare le differenze tra maiuscole/minuscole
            da_eliminare = False
            for materia_vietata in MATERIE_DA_RIMUOVERE:
                if materia_vietata.upper() in evento.name.upper():
                    da_eliminare = True
                    break
            
            if da_eliminare:
                # print(f"Rimosso: {evento.name}") # Decommenta se vuoi vedere i dettagli nei log
                eventi_rimossi += 1
            else:
                cal_pulito.events.add(evento)
                eventi_tenuti += 1

        # Salva il nuovo file
        with open(NOME_FILE_OUTPUT, "w", encoding="utf-8") as f:
            f.writelines(cal_pulito.serialize_iter())

        print("--- Operazione Completata ---")
        print(f"Eventi mantenuti: {eventi_tenuti}")
        print(f"Eventi rimossi: {eventi_rimossi}")
        print(f"File salvato come: {NOME_FILE_OUTPUT}")

    except Exception as e:
        print(f"Si è verificato un errore imprevisto: {e}")
        exit(1)

if __name__ == "__main__":
    main()