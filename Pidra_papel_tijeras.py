# Piedra Papel Tijeras
import os
import random
import time

opciones = ["Piedra", "Papel", "Tijera"]

# Posibles resultados


def Resultado(OpcionJugador, OpcionMaquina):
    if OpcionJugador == OpcionMaquina:
        print("\nEmpate")
    elif OpcionJugador == "Piedra" and OpcionMaquina == "Tijera":
        print("\nGana Jugador")
    elif OpcionJugador == "Papel" and OpcionMaquina == "Piedra":
        print("\nGana Jugador")
    elif OpcionJugador == "Tijera" and OpcionMaquina == "Papel":
        print("\nGana Jugador")
    else:
        print("\nGana la Maquina")
    print(f" \nTu opción: {OpcionJugador}")
    print(f"Opcion de la máquina: {OpcionMaquina}")


jugarSiNo = input("¿Quieres jugar a pidra papel y tijeras? (si/no): ")
quiereJugar = 0
while quiereJugar != 1:
    if jugarSiNo == "si":
        OpcionMaquina = random.choice(opciones)
        OpcionJugador = input("Piedra, Papel, o Tijera: ")
        i = 0
        if OpcionJugador == "Piedra" or OpcionJugador == "Papel" or OpcionJugador == "Tijera":
                i += 1
        while i != 1: 
            OpcionJugador = input("Opcion invalida, Piedra, Papel, o Tijera :")
            if OpcionJugador == "Piedra" or OpcionJugador == "Papel" or OpcionJugador == "Tijera":
                i += 1
        Resultado(OpcionJugador, OpcionMaquina)
        volverAjugar = input("Quieres volver a jugar??(si/no): ")
        os.system('cls')
        if volverAjugar == "no":
            print("Bien Jugado :)")
            time.sleep(3)
            quiereJugar += 1
        elif volverAjugar != "si":
            print("Opcion invalida, cerrando juego")
            time.sleep(3)
            quiereJugar += 1
    elif jugarSiNo == "no":
        print("Nos vemos!!")
        time.sleep(3)
        quiereJugar += 1
    else:
        invalido = 0
        while invalido != 1:
            print("Opcion invalida")
            invalida = input("La opcion dada es invalida, quieres jugar? (si/no): ")
            if invalida == "no":
                print("Nos vemos!!!")
                time.sleep(3)
                invalido += 1
                quiereJugar += 1
            elif invalida == "si":
                invalido += 1
                jugarSiNo = "si"
