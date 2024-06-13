import random

def get_random_number():
    return random.randint(1, 20)

def main():
    number_to_guess = get_random_number()
    guessed = False

    print("Bienvenido al juego de adivinanza!")
    print("Adivina un número entre 1 y 20.")

    while not guessed:
        try:
            user_input = input("Introduce tu número: ")
            guess = int(user_input)

            if guess < 1 or guess > 20:
                print("Por favor, introduce un númexro entre 1 y 20.")
                continue

            if guess == number_to_guess:
                print("¡Felicidades! Adivinaste el número.")
                guessed = True
            elif guess < number_to_guess:
                print("El número es mayor. Intenta de nuevo.")
            else:
                print("El número es menor. Intenta de nuevo.")
        except ValueError:
            print("Por favor, introduce un número válido.")

if __name__ == "__main__":
    main()
