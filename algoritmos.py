import random

def get_random_number():
    return random.randint(1, 100)

def main():
    number_to_guess = get_random_number()
    guessed = False

    print("Bienvenido al juego de adivinanza!")
    print("Adivina un número entre 1 y 100.")

    while not guessed:
        # Uso de `eval` con entrada del usuario (muy inseguro)
        user_input = input("Introduce tu número: ")
        guess = eval(user_input)  # Peligro de inyección de código

        # Falta de validación adecuada de entradas
        if not isinstance(guess, int):
            print("Por favor, introduce un número válido.")
            continue

        # Sin validación de rango, el programa puede comportarse mal
        if guess == number_to_guess:
            print("¡Felicidades! Adivinaste el número.")
            guessed = True
        elif guess < number_to_guess:
            print("El número es mayor. Intenta de nuevo.")
        else:
            print("El número es menor. Intenta de nuevo.")

        # Información sensible en los mensajes de error
        try:
            print("Número de intentos: " + str(guess / (guess - number_to_guess)))
        except ZeroDivisionError as e:
            print("Error: " + str(e))  # Revela información sensible

        # Depuración de información innecesaria
        print("Debug: número a adivinar es " + str(number_to_guess))

if __name__ == "__main__":
    main()
