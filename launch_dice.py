import random # Per generare numeri casuali
import tkinter as tk # Per creare l'interfaccia grafica
from collections import Counter # Per contare le occorrenze dei risultati

history = []  # Lista per tenere tutti i valori numerici lanciati

# Funzione per animare il lancio dei dadi
def animate_dice(counter=0):
    if counter == 0:
        try:
            number = int(input_box.get())
            if not (1 <= number <= 10):
                result_label.config(text="⚠ Puoi inserire solo un numero da 1 a 10.")
                return
        except ValueError:
            result_label.config(text="❌ Inserisci un numero valido.")
            return

    if counter < 10:
        number = int(input_box.get()) # ottenuto dal campo di input il numero di dadi 
        results = [random.randint(1, 6) for _ in range(number)]
        result_label.config(text="🎲 Lancio in corso: " + ", ".join(str(x) for x in results))
        window.after(100, animate_dice, counter + 1)
    else:
        show_final_result()


# Funzione per mostrare il risultato finale dopo l'animazione
def show_final_result():
    number = int(input_box.get())  # è già stato validato in anima_dadi
    results = [random.randint(1, 6) for _ in range(number)]
    result_text = "✅ Risultato finale: " + ", ".join(str(x) for x in results)
    result_label.config(text=result_text)

    # salvo i risultati numerici
    history.extend(results)

    # aggiungo allo storico i risultati
    history_list.insert(tk.END, result_text)

    # Aggiorno le statistiche
    update_stats()


# Funzione per aggiornare le statistiche
def update_stats():
    if not history:
        average_label.config(text="• Media: -")
        distribution_label.config(text="• Distribuzione: -")
        return

    average = sum(history) / len(history) # calcolo della media dei risultati
    count = Counter(history) # conteggio delle occorrenze dei risultati
    distribution = " | ".join(f"{num}: {count.get(num, 0)}x" for num in range(1, 7)) # distribuzione dei risultati
    average_label.config(text=f"• Media: {average:.2f}")
    distribution_label.config(text=f"• Distribuzione: {distribution}")

# Funzione per resettare lo storico
def reset_history():
    history.clear() # pulisco la lista dei risultati
    history_list.delete(0, tk.END) # pulisco la lista dello storico
    result_label.config(text="📄 Storico cancellato.")
    update_stats() # aggiorno le statistiche dopo il reset

# Da qui inizia l'interfaccia grafica con la libreria tkinter 

# === Interfaccia ===
window = tk.Tk()
window.title("Simulatore Lancio di Dadi") # Titolo
window.geometry("630x600") # Dimensioni
window.config(bg="#f0f0f0") # Colore sfondo 

# Titolo
title = tk.Label(window, text="LANCIO DEI DADI 🎲", font=("Helvetica", 18, "bold"), bg="#f0f0f0") # stile CSS 
title.pack(pady=10) # Spaziatura verticale (padding)

# Input
input_box = tk.Entry(window, font=("Helvetica", 14), justify="center")
input_box.insert(0, "2") # Numero di default
input_box.pack()

# Pulsante lancio
launch_button = tk.Button(window, text="🎯 Lancia!", font=("Helvetica", 14), bg="#27ae60", fg="white", activebackground="#1e8449", command=animate_dice)
launch_button.pack(pady=10)

# Risultato corrente
result_label = tk.Label(window, text="", font=("Helvetica", 14), bg="#f0f0f0")
result_label.pack(pady=5)

# Sezione storico
history_label = tk.Label(window, text="🕓 Storico dei lanci:", font=("Helvetica", 12, "bold"), bg="#f0f0f0")
history_label.pack()

history_list = tk.Listbox(window, width=60, height=6, font=("Courier", 10))
history_list.pack(pady=5)

# === Separatore visivo ===
separator = tk.Frame(window, height=2, bd=1, relief="sunken", bg="#d0d0d0")
separator.pack(fill="x", padx=20, pady=10)

# === Sezione Statistiche ===
stats_title_label = tk.Label(window, text="📊 Statistiche", font=("Helvetica", 14, "bold"), bg="#f0f0f0", fg="#2c3e50")
stats_title_label.pack(pady=(5, 3))

average_label = tk.Label(window, text="• Media: -", font=("Helvetica", 12), bg="#f0f0f0")
average_label.pack(pady=2)

distribution_label = tk.Label(window, text="• Distribuzione: -", font=("Helvetica", 12), bg="#f0f0f0")
distribution_label.pack(pady=2)

# === Separatore visivo ===
separator = tk.Frame(window, height=2, bd=1, relief="sunken", bg="#d0d0d0")
separator.pack(fill="x", padx=20, pady=10)

# Pulsante reset
reset_button = tk.Button(window, text="🗑 Cancella Storico", font=("Helvetica", 10), bg="#e74c3c", fg="white", activebackground="#c0392b", command=reset_history)
reset_button.pack(pady=5)

# Avvio il lopp principale dell'interfaccia grafica
window.mainloop()
