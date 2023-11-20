import random

mejores_puntuaciones = [] 

def obtener_numero_random(rango_inicio, rango_fin):
    return random.randint(rango_inicio, rango_fin)

def guardar_puntuacion(intentos):
    nombre_jugador = input("Ingresa tu nombre: ")
    mejores_puntuaciones.append((nombre_jugador, intentos))

def mostrar_mejores_puntuaciones():
    print("\nMejores Puntuaciones:")
    for i, (nombre, puntuacion) in enumerate(mejores_puntuaciones, start=1):
        print(f"{i}. {nombre}: {puntuacion} intentos")

def jugar_nivel_simple():
    print("¡Bienvenido al nivel simple!")
    numero_secreto = obtener_numero_random(0, 100)
    intentos = 0

    while intentos < 10:
        intento = int(input("Adivina el número: "))
        intentos += 1

        if intento == numero_secreto:
            print(f"¡Correcto! Has adivinado en {intentos} intentos.")
            guardar_puntuacion(intentos)
            mostrar_mejores_puntuaciones()
            break
        elif intento < numero_secreto:
            print("Demasiado bajo. ¡Intenta de nuevo!")
        else:
            print("Demasiado alto. ¡Intenta de nuevo!")

def jugar_nivel_intermedio():
    print("¡Bienvenido al nivel intermedio!")
    numero_secreto = obtener_numero_random(0, 1000)
    intentos = 0

    while intentos < 15:
        intento = int(input("Adivina el número: "))
        intentos += 1

        if intento == numero_secreto:
            print(f"¡Correcto! Has adivinado en {intentos} intentos.")
            guardar_puntuacion(intentos)
            mostrar_mejores_puntuaciones()
            break
        elif intento < numero_secreto:
            print("Demasiado bajo. ¡Intenta de nuevo!")
        else:
            print("Demasiado alto. ¡Intenta de nuevo!")

def jugar_nivel_avanzado():
    print("¡Bienvenido al nivel avanzado!")
    numero_secreto = obtener_numero_random(0, 1000000)
    intentos = 0

    while intentos < 25:
        intento = int(input("Adivina el número: "))
        intentos += 1

        if intento == numero_secreto:
            print(f"¡Correcto! Has adivinado en {intentos} intentos.")
            guardar_puntuacion(intentos)
            mostrar_mejores_puntuaciones()
            break
        elif intento < numero_secreto:
            print("Demasiado bajo. ¡Intenta de nuevo!")
        else:
            print("Demasiado alto. ¡Intenta de nuevo!")

def jugar_nivel_experto():
    print("¡Bienvenido al nivel experto!")
    numero_secreto = obtener_numero_random(0, 1000000000000)
    intentos = 0

    while intentos < 60:
        intento = int(input("Adivina el número: "))
        intentos += 1

        if intento == numero_secreto:
            print(f"¡Correcto! Has adivinado en {intentos} intentos.")
            guardar_puntuacion(intentos)
            mostrar_mejores_puntuaciones()
            break
        elif intento < numero_secreto:
            print("Demasiado bajo. ¡Intenta de nuevo!")
        else:
            print("Demasiado alto. ¡Intenta de nuevo!")

# Menú principal
def menu_principal():
    print("Bienvenido al juego de adivinar el número")
    print("1. Nivel Simple (0-100) 10 intentos")
    print("2. Nivel Intermedio (0-1,000) 15 intentos")
    print("3. Nivel Avanzado (0-1,000,000) 25 intentos")
    print("4. Nivel Experto (0-1,000,000,000,000) 60 intentos")
    print("5. Salir")

while True: 
    menu_principal()
    opcion = input("Selecciona un nivel (1-5): ")

    if opcion == "1":
        jugar_nivel_simple()
    elif opcion == "2":
        jugar_nivel_intermedio()
    elif opcion == "3":
        jugar_nivel_avanzado()
    elif opcion == "4":
        jugar_nivel_experto()
    elif opcion == "5":
        print("¡Gracias por jugar! Hasta luego.")
        break
    else:
        print("Opción no válida. Por favor, elige una opción del 1 al 5.")
if __name__=="__main__":
    def menu_principal():
        print("Bienvenido al juego de adivinar el número")
        print("1. Nivel Simple (0-100) 10 intentos")
        print("2. Nivel Intermedio (0-1,000) 15 intentos")
        print("3. Nivel Avanzado (0-1,000,000) 25 intentos")
        print("4. Nivel Experto (0-1,000,000,000,000) 60 intentos")
        print("5. Salir")
        
