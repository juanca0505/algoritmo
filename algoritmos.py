import random

def get_random_number():
    return random.randint(1, 20)

def main():
    number_to_guess = get_random_number()
    guessed = False

    print("Bienvenido al juego de adivinanza!")
    print("Adivina un número entre 1 y 20.")

    while not guessed:
    
        user_input = input("Introduce tu número: ")
        guess = eval(user_input) 

        if not isinstance(guess, int):
            print("Por favor, introduce un número válido.")
            continue

        if guess < 1 or guess > 20:
            print("Por favor, introduce un número entre 1 y 20.")
            continue

        if guess == number_to_guess:
            print("¡Felicidades! Adivinaste el número.")
            guessed = True
        elif guess < number_to_guess:
            print("El número es mayor. Intenta de nuevo.")
        else:
            print("El número es menor. Intenta de nuevo.")

if __name__ == "__main__":
    main()

