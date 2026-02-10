import os
import requests
from ics import Calendar

# ================= CONFIGURAZIONE =================
# Aggiungi qui, tra virgolette, i nomi (o parti del nome) delle materie che NON vuoi.
MATERIE_DA_RIMUOVERE = [
    "MODELLI INNOVATIVI PER LA GESTIONE DEI DATI",
    "PROGRAMMAZIONE PROCEDURALE E AD OGGETTI",
    "BASI DI DATI II"
]

NOME_FILE_OUTPUT = "custom_uni_calendar.ics"
# ==================================================

def main():
    url_universita = os.environ.get("CALENDAR_URL")

    if not url_universita:
        print("ERRORE: Non ho trovato la variabile 'CALENDAR_URL'.")
        exit(1)

    # --- TRUCCO ANTI-BLOCCO ---
    # Creiamo una falsa identità: diciamo al server che siamo un Mac con Chrome
    headers_fake_browser = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36",
        "Accept": "text/calendar, text/html, application/xhtml+xml, application/xml;q=0.9, */*;q=0.8",
        "Accept-Language": "it-IT,it;q=0.9,en-US;q=0.8,en;q=0.7",
        "Connection": "keep-alive"
    }

    try:
        print("--- Inizio Scaricamento Calendario ---")
        
        # Aggiungiamo 'headers' alla richiesta e un timeout di 60 secondi
        response = requests.get(url_universita, headers=headers_fake_browser, timeout=60)
        response.raise_for_status()
        
        cal_originale = Calendar(response.text)
        cal_pulito = Calendar()
        
        eventi_rimossi = 0
        eventi_tenuti = 0

        print(f"Trovati {len(cal_originale.events)} eventi totali. Inizio filtraggio...")

        for evento in cal_originale.events:
            da_eliminare = False
            for materia_vietata in MATERIE_DA_RIMUOVERE:
                if materia_vietata.upper() in evento.name.upper():
                    da_eliminare = True
                    break
            
            if da_eliminare:
                eventi_rimossi += 1
            else:
                cal_pulito.events.add(evento)
                eventi_tenuti += 1

        with open(NOME_FILE_OUTPUT, "w", encoding="utf-8") as f:
            f.writelines(cal_pulito.serialize_iter())

        print("--- Operazione Completata ---")
        print(f"Eventi mantenuti: {eventi_tenuti}")
        print(f"Eventi rimossi: {eventi_rimossi}")
        print(f"File salvato come: {NOME_FILE_OUTPUT}")

    except requests.exceptions.Timeout:
        print("ERRORE: Il server dell'università ha bloccato la connessione (Timeout).")
        print("Probabilmente stanno bloccando gli indirizzi IP di GitHub.")
        exit(1)
    except Exception as e:
        print(f"Si è verificato un errore imprevisto: {e}")
        exit(1)

if __name__ == "__main__":
    main()