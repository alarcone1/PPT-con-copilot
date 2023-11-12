<<<<<<< HEAD
<<<<<<< HEAD
# Especificación del minijuego de Piedra, Papel o Tijeras para ser ejecutado desde la terminal
# El objetivo del juego es ganar más rondas que el oponente.
# Reglas del juego:
    # Piedra gana a Tijeras
    # Tijeras gana a Papel
    # Papel gana a Piedra

# Interacciones del juego

# El jugador ingresa una opción: piedra, papel o tijeras.
import random

def pedir_opcion():
    """Pedir al usuario su opción"""
    
    opcion = input("¿Piedra, papel o tijera? ")
    while opcion not in ["piedra", "papel", "tijera"]:
        print("Opción inválida")
        opcion = input("¿Piedra, papel o tijera? ")
    return opcion

# La computadora elige una opción aleatoria.
def elegir_opcion():
    """Elegir una opción aleatoria"""
    
    return random.choice(["piedra", "papel", "tijera"])

# El juego determina el ganador.
def determinar_ganador(opcion_jugador, opcion_computadora):
    """Determinar el ganador"""
    
    if opcion_jugador == opcion_computadora:
        return "empate"
    elif opcion_jugador == "piedra" and opcion_computadora == "tijera":
        return "jugador"
    elif opcion_jugador == "tijera" and opcion_computadora == "papel":
        return "jugador"
    elif opcion_jugador == "papel" and opcion_computadora == "piedra":
        return "jugador"
    else:
        return "computadora"

# El jugador vuelve a ingresar una opción o termina el juego.
def jugar():
    """Jugar una partida"""
    
    opcion_jugador = pedir_opcion()
    opcion_computadora = elegir_opcion()
    print(f"Computadora: {opcion_computadora}")
    ganador = determinar_ganador(opcion_jugador, opcion_computadora)
    if ganador == "empate":
        print("Empate")
    else:
        print(f"Ganó el {ganador}")
    return ganador

# El juego termina cuando el jugador decide no continuar.
def main():
    """Función principal"""
    
    print("-->  Piedra, papel o tijera")
    ganador = jugar()
    while ganador == "jugador":
        ganador = jugar()
    print("Fin del juego")

if __name__ == "__main__":
    main()
=======

>>>>>>> origin
