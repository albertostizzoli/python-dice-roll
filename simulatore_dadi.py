import random

# creo una funzione che simula il lancio di un dado
def roll_dice(num_dice):
    results = [random.randint(1, 6) for _ in range(num_dice)]
    return results

