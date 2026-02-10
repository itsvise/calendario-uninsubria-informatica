import requests
from ics import Calendar

# CONFIGURAZIONE
URL_ORIGINALE = "https://unins.prod.up.cineca.it:443/api/FiltriICal/impegniICal?id=698b099bea21ca002dcc69d6"
MATERIE_DA_RIMUOVERE = [
    "MODELLI INNOVATIVI PER LA GESTIONE DEI DATI",
    "PROGRAMMAZIONE PROCEDURALE E AD OGGETTI",
    "BASI DI DATI II",
    # Aggiungi o modifica qui le materie da rimuovere, in maiuscolo
]
NOME_FILE_OUTPUT = "custom_uni_calendar.ics"

def main():
    try:
        # Scarica il calendario
        print("Scaricamento calendario...")
        response = requests.get(URL_ORIGINALE)
        response.raise_for_status() # Blocca se c'è errore di rete
        
        cal = Calendar(response.text)
        nuovo_cal = Calendar()

        conteggio_rimossi = 0
        
        for evento in cal.events:
            # Controlla se il nome contiene una delle materie vietate
            # Usa .upper() per evitare problemi con maiuscole/minuscole
            da_rimuovere = any(materia in evento.name.upper() for materia in MATERIE_DA_RIMUOVERE)
            
            if not da_rimuovere:
                nuovo_cal.events.add(evento)
            else:
                conteggio_rimossi += 1

        # Salva il file
        with open(NOME_FILE_OUTPUT, "w") as f:
            f.writelines(nuovo_cal.serialize_iter())
            
        print(f"Fatto! Rimossi {conteggio_rimossi} eventi indesiderati.")
        
    except Exception as e:
        print(f"Errore: {e}")
        exit(1)

if __name__ == "__main__":
    main()