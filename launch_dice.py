import random # Per generare numeri casuali
import tkinter as tk # Per creare l'interfaccia grafica
from collections import Counter # Per contare le occorrenze dei risultati

storico = []  # Lista per tenere tutti i valori numerici lanciati

# Funzione per animare il lancio dei dadi
def anima_dadi(contatore=0):
    if contatore < 10:
        try:
            numero = int(casella_input.get()) # chiedo all'utente il numero di dadi da lanciare
            risultati = [random.randint(1, 6) for _ in range(numero)]
            etichetta_risultato.config(text="🎲 Lancio in corso: " + ", ".join(str(x) for x in risultati))
            finestra.after(100, anima_dadi, contatore + 1) # il tempo di attesa tra i lanci 
        except ValueError:
            etichetta_risultato.config(text="❌ Inserisci un numero valido.")
    else:
        mostra_risultato_finale()

# Funzione per mostrare il risultato finale dopo l'animazione
def mostra_risultato_finale():
    try:
        numero = int(casella_input.get())
        if numero <= 1:
            etichetta_risultato.config(text="⚠ Inserisci un numero maggiore di 1.") # l'utente deve inserire un numero maggiore di 1
            return

        risultati = [random.randint(1, 6) for _ in range(numero)] # lancio dei dadi
        testo_risultato = "✅ Risultato finale: " + ", ".join(str(x) for x in risultati) # testo che mostra i risultati finali
        etichetta_risultato.config(text=testo_risultato)

        # salvo i risultati numerici
        storico.extend(risultati)

        # aggiungo allo storico i risultati
        lista_storico.insert(tk.END, testo_risultato)

        # Aggiorno le statistiche
        aggiorna_statistiche()

    except ValueError:
        etichetta_risultato.config(text="❌ Inserisci un numero valido.")

# Funzione per aggiornare le statistiche
def aggiorna_statistiche():
    if not storico:
        etichetta_media.config(text="• Media: -")
        etichetta_distribuzione.config(text="• Distribuzione: -")
        return

    media = sum(storico) / len(storico) # calcolo della media dei risultati
    conta = Counter(storico) # conteggio delle occorrenze dei risultati
    distribuzione = " | ".join(f"{num}: {conta.get(num, 0)}x" for num in range(1, 7)) # distribuzione dei risultati
    etichetta_media.config(text=f"• Media: {media:.2f}")
    etichetta_distribuzione.config(text=f"• Distribuzione: {distribuzione}")

# Funzione per resettare lo storico
def resetta_storico():
    storico.clear() # pulisco la lista dei risultati
    lista_storico.delete(0, tk.END) # pulisco la lista dello storico
    etichetta_risultato.config(text="📄 Storico cancellato.")
    aggiorna_statistiche() # aggiorno le statistiche dopo il reset

# Da qui inizia l'interfaccia grafica con la libreria tkinter 

# === Interfaccia ===
finestra = tk.Tk()
finestra.title("Simulatore Lancio di Dadi") # Titolo
finestra.geometry("630x600") # Dimensioni
finestra.config(bg="#f0f0f0") # Colore sfondo 

# Titolo
titolo = tk.Label(finestra, text="LANCIO DEI DADI 🎲", font=("Helvetica", 18, "bold"), bg="#f0f0f0") # stile CSS 
titolo.pack(pady=10) # Spaziatura verticale (padding)

# Input
casella_input = tk.Entry(finestra, font=("Helvetica", 14), justify="center")
casella_input.insert(0, "2") # Numero di default
casella_input.pack()

# Pulsante lancio
pulsante = tk.Button(finestra, text="🎯 Lancia!", font=("Helvetica", 14), bg="#27ae60", fg="white", activebackground="#1e8449", command=anima_dadi)
pulsante.pack(pady=10)

# Risultato corrente
etichetta_risultato = tk.Label(finestra, text="", font=("Helvetica", 14), bg="#f0f0f0")
etichetta_risultato.pack(pady=5)

# Sezione storico
etichetta_storico = tk.Label(finestra, text="🕓 Storico dei lanci:", font=("Helvetica", 12, "bold"), bg="#f0f0f0")
etichetta_storico.pack()

lista_storico = tk.Listbox(finestra, width=60, height=6, font=("Courier", 10))
lista_storico.pack(pady=5)

# === Separatore visivo ===
separator = tk.Frame(finestra, height=2, bd=1, relief="sunken", bg="#d0d0d0")
separator.pack(fill="x", padx=20, pady=10)

# === Sezione Statistiche ===
etichetta_titolo_statistiche = tk.Label(finestra, text="📊 Statistiche", font=("Helvetica", 14, "bold"), bg="#f0f0f0", fg="#2c3e50")
etichetta_titolo_statistiche.pack(pady=(5, 3))

etichetta_media = tk.Label(finestra, text="• Media: -", font=("Helvetica", 12), bg="#f0f0f0")
etichetta_media.pack(pady=2)

etichetta_distribuzione = tk.Label(finestra, text="• Distribuzione: -", font=("Helvetica", 12), bg="#f0f0f0")
etichetta_distribuzione.pack(pady=2)

# === Separatore visivo ===
separator = tk.Frame(finestra, height=2, bd=1, relief="sunken", bg="#d0d0d0")
separator.pack(fill="x", padx=20, pady=10)

# Pulsante reset
pulsante_reset = tk.Button(finestra, text="🗑 Cancella Storico", font=("Helvetica", 10), bg="#e74c3c", fg="white", activebackground="#c0392b", command=resetta_storico)
pulsante_reset.pack(pady=5)

# Avvio il lopp principale dell'interfaccia grafica
finestra.mainloop()

