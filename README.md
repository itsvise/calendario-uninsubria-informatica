# Calendario Uninsubria Informatica - Filtro Personalizzato

Questo repository contiene uno script Python automatizzato per filtrare il calendario delle lezioni del corso di laurea in Informatica (Università degli Studi dell'Insubria, Varese).

Lo script scarica il calendario ufficiale in formato iCal, rimuove gli insegnamenti non frequentati o non presenti nel piano di studi e genera un nuovo file `.ics` pulito, pronto per essere importato su Google Calendar, Apple Calendar o Outlook.

## Funzionalita

- **Download automatico**: Recupera l'orario aggiornato direttamente dai server Cineca University Planner.
- **Filtraggio personalizzato**: Rimuove gli eventi basandosi su una lista di materie escluse definita dall'utente.
- **Automazione**: Utilizza GitHub Actions per aggiornare il calendario ogni 6 ore, garantendo che eventuali cambiamenti di orario o aula siano riflessi automaticamente.

## Configurazione

Il filtraggio avviene nel file `filter_calendar.py`. La lista delle materie da escludere è definita nella variabile `MATERIE_DA_RIMUOVERE`.

Esempio di configurazione attuale:
- MODELLI INNOVATIVI PER LA GESTIONE DEI DATI
- PROGRAMMAZIONE PROCEDURALE E AD OGGETTI
- BASI DI DATI II

Le materie non presenti in questa lista (es. Logica, Programmazione di Dispositivi Mobili) verranno mantenute nel calendario finale.

## Requisiti

Il progetto richiede Python 3.9 o superiore e le seguenti librerie, elencate in `requirements.txt`:
- `ics`
- `requests`

## Installazione e Uso

### 1. Configurazione del Secret
Per motivi di sicurezza, l'URL del calendario originale non è incluso nel codice sorgente. È necessario configurare un GitHub Secret:

1. Andare su **Settings** > **Secrets and variables** > **Actions**.
2. Creare un nuovo repository secret denominato `CALENDAR_URL`.
3. Inserire come valore l'URL iCal pubblico fornito dal portale studenti.

### 2. Output
L'automazione genera un file denominato `custom_uni_calendar.ics` nella root del repository.

Per sottoscrivere il calendario sul proprio dispositivo, utilizzare il link Raw del file generato:
`https://raw.githubusercontent.com/NOME_UTENTE/NOME_REPOSITORY/main/custom_uni_calendar.ics`

(Sostituire `NOME_UTENTE` e `NOME_REPOSITORY` con i dati corretti).

## Licenza

Questo progetto è distribuito sotto licenza MIT. Vedere il file LICENSE per i dettagli completi.