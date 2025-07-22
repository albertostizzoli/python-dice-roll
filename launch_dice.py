import random
import tkinter as tk

def anima_dadi(contatore=0):
    # Anima per circa 1 secondo (10 volte ogni 100 ms)
    if contatore < 10:
        risultati = [random.randint(1, 6) for _ in range(int(casella_input.get()))]
        etichetta_risultato.config(text="🎲 Lancio in corso: " + ", ".join(str(x) for x in risultati))
        finestra.after(100, anima_dadi, contatore + 1)
    else:
        mostra_risultato_finale()

def mostra_risultato_finale():
    try:
        num = int(casella_input.get())
        if num <= 1:
            etichetta_risultato.config(text="⚠ Inserisci un numero maggiore di 1.")
            return
        risultati = [random.randint(1, 6) for _ in range(num)]
        etichetta_risultato.config(text="✅ Risultato finale: " + ", ".join(str(x) for x in risultati))
    except ValueError:
        etichetta_risultato.config(text="❌ Inserisci un numero valido.")

# Interfaccia
finestra = tk.Tk()
finestra.title("Simulatore Dadi")
finestra.geometry("400x250")
finestra.config(bg="#f0f0f0")

# Titolo
titolo = tk.Label(finestra, text="LANCIO DEI DADI 🎲", font=("Helvetica", 18, "bold"), bg="#f0f0f0")
titolo.pack(pady=10)

# Input
casella_input = tk.Entry(finestra, font=("Helvetica", 14), justify="center")
casella_input.insert(0, "2")
casella_input.pack()

# Pulsante
pulsante = tk.Button(finestra, text="🎯 Lancia!", font=("Helvetica", 14), bg="#27ae60", fg="white", activebackground="#1e8449", command=anima_dadi)
pulsante.pack(pady=10)

# Risultato
etichetta_risultato = tk.Label(finestra, text="", font=("Helvetica", 14), bg="#f0f0f0")
etichetta_risultato.pack(pady=10)

finestra.mainloop()


