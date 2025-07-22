import random
import tkinter as tk

storico = []  # Lista per tenere lo storico dei lanci

def anima_dadi(contatore=0):
    if contatore < 10:
        try:
            numero = int(casella_input.get())
            risultati = [random.randint(1, 6) for _ in range(numero)]
            etichetta_risultato.config(text="🎲 Lancio in corso: " + ", ".join(str(x) for x in risultati))
            finestra.after(100, anima_dadi, contatore + 1)
        except ValueError:
            etichetta_risultato.config(text="❌ Inserisci un numero valido.")
    else:
        mostra_risultato_finale()

def mostra_risultato_finale():
    try:
        numero = int(casella_input.get())
        if numero <= 1:
            etichetta_risultato.config(text="⚠ Inserisci un numero maggiore di 1.")
            return
        risultati = [random.randint(1, 6) for _ in range(numero)]
        testo_risultato = "✅ Risultato finale: " + ", ".join(str(x) for x in risultati)
        etichetta_risultato.config(text=testo_risultato)

        # Aggiungo al log e aggiorno la lista grafica
        storico.append(testo_risultato)
        lista_storico.insert(tk.END, testo_risultato)

    except ValueError:
        etichetta_risultato.config(text="❌ Inserisci un numero valido.")

def resetta_storico():
    storico.clear()
    lista_storico.delete(0, tk.END)
    etichetta_risultato.config(text="📄 Storico cancellato.")

# Interfaccia
finestra = tk.Tk()
finestra.title("Simulatore Dadi con Storico")
finestra.geometry("550x400")
finestra.config(bg="#f0f0f0")

# Titolo
titolo = tk.Label(finestra, text="LANCIO DEI DADI 🎲", font=("Helvetica", 18, "bold"), bg="#f0f0f0")
titolo.pack(pady=10)

# Input
casella_input = tk.Entry(finestra, font=("Helvetica", 14), justify="center")
casella_input.insert(0, "2")
casella_input.pack()

# Pulsante lancia
pulsante = tk.Button(finestra, text="🎯 Lancia!", font=("Helvetica", 14), bg="#27ae60", fg="white",
                     activebackground="#1e8449", command=anima_dadi)
pulsante.pack(pady=10)

# Risultato corrente
etichetta_risultato = tk.Label(finestra, text="", font=("Helvetica", 14), bg="#f0f0f0")
etichetta_risultato.pack(pady=5)

# Storico
etichetta_storico = tk.Label(finestra, text="🕓 Storico dei lanci:", font=("Helvetica", 12, "bold"), bg="#f0f0f0")
etichetta_storico.pack()

# Listbox per storico
lista_storico = tk.Listbox(finestra, width=50, height=6, font=("Courier", 10))
lista_storico.pack(pady=5)

# Pulsante per resettare lo storico
pulsante_reset = tk.Button(finestra, text="🗑 Cancella Storico", font=("Helvetica", 10), bg="#e74c3c", fg="white",
                           activebackground="#c0392b", command=resetta_storico)
pulsante_reset.pack(pady=5)

# Avvio dell'app
finestra.mainloop()



