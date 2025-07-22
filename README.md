# PYTHON-DICE-ROLL

## 🧠 Obiettivo
Creare un'applicazione grafica in Python che simuli il lancio di uno o più dadi, permettendo all'utente di:

- Specificare quanti dadi vuole lanciare
- Visualizzare animazioni e risultati
- Tenere traccia dello storico
- Visualizzare statistiche (media e distribuzione)

## 🖥️ Interfaccia Grafica
L'interfaccia è sviluppata con `tkinter`, la libreria GUI standard di Python.  
È user-friendly e mostra:

- Un campo per l'inserimento del numero di dadi
- Un pulsante per lanciare i dadi
- Una sezione con i risultati correnti
- Uno storico dei lanci
- Statistiche aggiornate automaticamente

## 🧪 Funzionalità Principali

- ⚙️ **Lancio animato** dei dadi (con effetto di attesa)
- 🕓 **Storico visivo** dei lanci
- 📊 **Statistiche** in tempo reale:
  - Media dei risultati
  - Distribuzione da 1 a 6
- 🔁 **Reset dello storico** con un click

## 📝 Come funziona

1. L'utente inserisce il numero di dadi da lanciare
2. Il programma anima un lancio con numeri casuali (1-6)
3. Mostra il risultato finale
4. Aggiorna lo storico e calcola:
   - 📈 Media totale dei valori lanciati
   - 📌 Quanti "1", "2", "3"... sono stati lanciati

## 📦 Librerie Utilizzate

- `random`: per generare numeri casuali da 1 a 6
- `tkinter`: per creare l'interfaccia grafica
- `collections.Counter`: per contare la frequenza dei risultati

## ▶️ Come eseguire

Assicurati di avere Python 3 installato.  
Poi esegui:

```bash
python launch_dice.py



