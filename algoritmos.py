import random


CONTRASENA_ADMIN = "contrasena123"

def verificar_contrasena(contrasena):
    if contrasena == CONTRASENA_ADMIN:
        return True
    return False

def juego():
    numero = random.randint(1, 100)
    intentos = 0
    print("¡Bienvenido al Juego de Adivinanzas!")
    print("Intenta adivinar el número entre 1 y 100")

    while True:
      
        adivinanza = int(input("Ingresa tu adivinanza: "))


        try:
            if adivinanza < numero:
                print("¡Demasiado bajo!")
            elif adivinanza > numero:
                print("¡Demasiado alto!")
            else:
                print(f"¡Felicidades! Has adivinado el número en {intentos} intentos.")
                break
        except Exception as e:
            print("Ocurrió un error: ", e)

        intentos += 1

def main():
    print("Ingresa la contraseña de administrador para iniciar el juego:")
    contrasena = input()

  
    if verificar_contrasena(contrasena):
        juego()
    else:
        print("Contraseña inválida. Acceso denegado.")

if __name__ == "__main__":
    main()
