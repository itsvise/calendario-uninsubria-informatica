# Calendario Uninsubria Informatica - Filtro Personalizzato

Questo repository ospita il calendario filtrato delle lezioni di Informatica (Uninsubria), mantenuto aggiornato tramite un'automazione locale.

## Come funziona

A causa dei blocchi firewall dell'università verso i server cloud, l'aggiornamento non avviene più tramite GitHub Actions ma segue questo flusso:
1. **Mac Locale**: Uno script (`aggiorna.sh`) viene eseguito automaticamente ogni mattina tramite `cron`.
2. **Download & Filtro**: Lo script scarica il calendario ufficiale, rimuove le materie non seguite (es. Basi di Dati II, Modelli Innovativi) mantenendo solo quelle attive.
3. **Push**: Il file `.ics` pulito viene caricato su questo repository.
4. **Dispositivi**: iPhone e Mac leggono il file aggiornato direttamente da GitHub.

## Link al Calendario

Per iscriversi al calendario aggiornato:
`https://raw.githubusercontent.com/itsvise/calendario-uninsubria-informatica/main/custom_uni_calendar.ics`

## Configurazione

Il filtraggio è gestito da `filter_calendar.py`.
Materie attualmente rimosse:
- MODELLI INNOVATIVI PER LA GESTIONE DEI DATI
- PROGRAMMAZIONE PROCEDURALE E AD OGGETTI
- BASI DI DATI II

## Requisiti Tecnici
- Python 3.9+
- Librerie: `ics`, `requests`, `urllib3<2.0`