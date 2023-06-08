import time
import random
import os

clear = lambda: os.system('clear')

def carta_aleatoria(baraja):
    aleatorio = random.randrange(len(baraja))
    carta = baraja.pop(aleatorio)
    return carta

def num_carta(carta):

    if len(carta) != 0:
        numero = carta[-2]
        if numero == "A":
            return 1
        elif numero == "0":
            return 10
        elif numero == "J":
            return 11
        elif numero == "Q":
            return 12
        elif numero == "K":
            return 13
        else:
            return int(numero)
    else:
        return 0

def bj_sum_cartas(cartas):
    if len(cartas) != 0:
        suma = 0
        cantidad_de_As = 0
        for i in range(len(cartas)):
            carta = cartas[i]
            numero = num_carta(carta)
            if numero == 10 or numero == 11 or numero == 12 or numero == 13:
                suma+=10
            elif numero == 1:
                cantidad_de_As+=1
            else:
                suma+=numero
        for i in range(cantidad_de_As):
            if suma >= 11:
                suma+=1
            else:
                suma+=11
    else:
        suma = 0
    return suma

def bj_hay_blackjack(cartas):
    bj = False
    if len(cartas) == 2 and bj_sum_cartas(cartas) == 21:
        bj = True
    return bj

def bj_poder_doblar(cartas):
    puede = False
    s = bj_sum_cartas(cartas)
    if len(cartas) == 2 and (s==9 or s==10 or s==11):
        puede = True
    return puede

def bj_poder_rendirse(cartas):
    res = False
    if len(cartas) == 2:
        res = True
    return res

def bj_ganador(jugador_cartas, crupier_cartas):

    jugador_puntos = bj_sum_cartas(jugador_cartas)
    crupier_puntos = bj_sum_cartas(crupier_cartas)

    if jugador_puntos > 21:
        jugador_puntos = 0
    if crupier_puntos > 21:
        crupier_puntos = 0

    proporcion = 0
    if jugador_puntos > crupier_puntos:
        proporcion = 1
        if bj_hay_blackjack(jugador_cartas):
            proporcion = 3/2
    elif jugador_puntos < crupier_puntos:
        proporcion = -1
    else:
        if bj_hay_blackjack(jugador_cartas) and bj_hay_blackjack(crupier_cartas):
            proporcion = 0
        elif bj_hay_blackjack(jugador_cartas):
            proporcion = 3/2
        elif bj_hay_blackjack(crupier_cartas):
            proporcion = -1
    return proporcion

def blackjack(fichas_apostadas):

    #Declarar variables
    apuesta = fichas_apostadas
    jugador_cartas = []
    crupier_cartas = []
    jugador_decidiendo = True
    crupier_decidiendo = True
    opciones = {}
    mostrar_opciones = False
    resultado = 0
    mostrar_resultado = False
    mostrar_ganador = False
    mostrar_rendido = False
    jugador_rendido = False
    jugador_doblado = False


    def imprimir():
        time.sleep(0.8)
        clear()

        print("Blackjack", end="    -    ")
        if jugador_doblado:
            print("Apuesta: " + str(fichas_apostadas) + " -> " + str(apuesta))
        elif jugador_rendido:
            print("Apuesta: " + str(fichas_apostadas) + " -> " + str(apuesta))
        else:
            print("Apuesta: " + str(apuesta))
        print("--------------------------------------")
        print()


        print("Jugador: ",jugador_cartas)
        if len(jugador_cartas) != 0 and jugador_decidiendo == False:
            if bj_hay_blackjack(jugador_cartas):
                print("Jugador Total: ", bj_sum_cartas(jugador_cartas), " BLACKJACK")
            else:
                print("Jugador Total: ", bj_sum_cartas(jugador_cartas))

        else:
            print()

        print("Crupier: ",crupier_cartas)
        if len(crupier_cartas) != 0 and crupier_decidiendo == False:
            if bj_hay_blackjack(crupier_cartas):
                print("Crupier Total: ", bj_sum_cartas(crupier_cartas), " BLACKJACK")
            else:
                print("Crupier Total: ", bj_sum_cartas(crupier_cartas))

        else:
            print()

        print()
        print("-------------------------------------")

        if jugador_decidiendo == True and mostrar_opciones == True:
            print("OPCIONES:", opciones )

        elif jugador_rendido == True and mostrar_rendido == True:
            print("RENDICION: " + str(resultado) + " fichas.")

        elif crupier_decidiendo == False and mostrar_ganador == True:
            ganador = bj_ganador(jugador_cartas, crupier_cartas)
            res_auxiliar = ""
            if ganador > 0:
                print("GANADOR: JUGADOR")
                res_auxiliar = "+"
            elif ganador < 0:
                print("GANADOR: CRUPIER")
            else:
                print("EMPATE")
            if mostrar_resultado == True:
                print("RESULTADO: " + str(res_auxiliar) + str(resultado) + " fichas.")

    # Crear baraja
    palos = ["♠", "♥", "♦", "♣"]
    numeros = ["A",2,3,4,5,6,7,8,9,10,"J","Q","K"]
    baraja = []
    for i in range(len(palos)):
        for j in range(len(numeros)):
            baraja.append(str(numeros[j])+ palos[i])

    imprimir()

    # Sacar 2 aleatorios para jugador
    for i in range(2):
        jugador_cartas.append(carta_aleatoria(baraja))
    imprimir()

    # Revisar si blackjack automático
    if bj_hay_blackjack(jugador_cartas):
        jugador_decidiendo = False

    # Si no hay blackjack automático
    else:
        mostrar_opciones = True
        jugador_decidiendo = True
        # Agregar opciones de Doblar, dividir, rendirse
        s = bj_sum_cartas(jugador_cartas)
        opciones[1]= "Plantarse"
        opciones[2] = "Robar"
        # Poder Doblar
        if bj_poder_doblar(jugador_cartas):
            opciones[3] = "Doblar"
        # Poder Rendirse
        if bj_poder_rendirse(jugador_cartas):
            opciones[4] = "Rendirse"

    imprimir()

    # TURNOS DEL JUGADOR

    while(jugador_decidiendo):

        decision = int(input())

        if decision == 1:
            mostrar_opciones = False
            imprimir()
            jugador_decidiendo = False
            imprimir()
        elif decision == 2:
            jugador_cartas.append(carta_aleatoria(baraja))
            imprimir()
            if len(jugador_cartas) >= 2 and len(opciones) !=2:
                # Resetear opciones a opciones basicas
                opciones = {}
                opciones[1] = "Plantarse"
                opciones[2] = "Robar"
                imprimir()
            if bj_sum_cartas(jugador_cartas) >= 21:
                mostrar_opciones = False
                imprimir()
                jugador_decidiendo = False
                imprimir()
        elif decision == 3:
            if bj_poder_doblar(jugador_cartas):
                mostrar_opciones = False
                imprimir()
                jugador_doblado = True
                apuesta = apuesta*2
                imprimir()
                jugador_cartas.append(carta_aleatoria(baraja))
                imprimir()
                jugador_decidiendo = False
                imprimir()
        elif decision == 4:
            mostrar_opciones = False
            imprimir()
            if bj_poder_rendirse(jugador_cartas):
                jugador_rendido = True
                apuesta = apuesta/2
                imprimir()
                mostrar_rendido = True
                resultado = (-1) * apuesta
                imprimir()
                return round(resultado)


    # Sacar 2 aleatorios para crupier

    for i in range(2):
        crupier_cartas.append(carta_aleatoria(baraja))
    imprimir()

    # Sacar más cartas si crupier necesita

    while (crupier_decidiendo):
        if bj_sum_cartas(crupier_cartas) >= 17:
            crupier_decidiendo = False
            imprimir()
        else:
            crupier_cartas.append(carta_aleatoria(baraja))
            imprimir()

    # Resultado e imprimirlo

    proporcion = bj_ganador(jugador_cartas, crupier_cartas)
    resultado = apuesta * proporcion
    # Caso especial: Si jugador dobló y perdió, solo perderá lo apostado inicialmente
    if jugador_doblado and proporcion < 0:
        resultado = fichas_apostadas * (-1)

    mostrar_ganador = True
    imprimir()
    mostrar_resultado = True
    imprimir()

    # Return apuesta

    return round(resultado)

if __name__ == "__main__":
    blackjack(10)