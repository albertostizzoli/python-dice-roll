import random

# creo una funzione che simula il lancio di un dado
def roll_dice(num_dice):
    # uso il modulo random per generare numeri casuali tra 1 e 6 e restituire i risultati in una lista
    results = [random.randint(1, 6) for _ in range(num_dice)] 
    return results

# funzione principale per eseguire il lancio dei dadi
def main():
    print("BENVENUTO AL LANCIO DEI DADI!")

    while True:
        try:
            # chiedo all'utente quanti dadi vuole lanciare
            num_dice = int(input("QUANTI DADI VUOI LANCIARE?: "))
            if num_dice <= 1:
                print("PER FAVORE. INSERISCI UN NUMERO SOPRA L'1.")
                continue
            # chiamo la funzione per lanciare i dadi e stampo i risultati
            results = roll_dice(num_dice)
            print(f"HAI LANCIATO {num_dice} DADI E I RISULTATI SONO: {', '.join(map(str, results))}")
        # gestisco l'eccezione se l'input non è un numero valido
        except ValueError:
            print("PER FAVORE. INSERISCI UN NUMERO VALIDO.")

        # chiedo all'utente se vuole lanciare di nuovo i dadi
        again = input("VUOI LANCIARE DI NUOVO I DADI? (s/n): ").strip().lower()
        # se l'utente risponde 'n' o qualcosa di diverso da 's', esco dal ciclo
        if again != 's':
            print("GRAZIE PER AVER GIOCATO! ARRIVEDERCI!")
            break       
# Eseguo la funzione principale se il file viene eseguito direttamente
if __name__ == "__main__":
    main()


