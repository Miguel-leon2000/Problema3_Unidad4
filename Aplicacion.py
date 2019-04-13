"""
Se importan las clases derivadas creandoles una instancia para poder acceder a ellas,
ademas de importar la libreria random para que la consola genere un numero aleatorio,
en este caso el rango es de 0 y 10.
"""
from random import *
from JuegoAdivinaImpar import *
from JuegoAdivinaPar import *
from JuegoAdivinaNumero import *

# Metodo main donde contiene los juegos derivados de las clases establecidas
def main():

    """
    Dentro del metodo main se aplica un switch para que el jugador elija el juego
    que mas le agrade.
    """
    JD = int(input("Elige el juego que desees jugar: "
                   "\n 1 = Adivinar número "
                   "\n 2 = Adivinar número Par "
                   "\n 3 = Adivinar número Impar "
                   "\n Recuerda que solo tienes 3 vidas!"))

    if JD == 1:
        juega = JuegoAdivinaNumero(3, randrange(10))

    if JD == 2:
        juega = JuegoAdivinaPar(3, choice([0, 2, 4, 6, 8, 10])) # Se aplica choice para establecer los valores

    if JD == 3:
        juega = JuegoAdivinaImpar(3, choice([1, 3, 5, 7, 9]))

    juega.Juega() # Manda llamar al metodo Juega mediante la instancia creada


    """
    Ciclo while en el que si es verdadero (True), es decir que el jugador quiera volver a jugar
    y su respuesta sea Si, se vuelve a ejecutar el juego en el que esta, mandando llamar de nuevo al metodo Juega.
    """
    while True:
        Reiniciar = input('¿Quieres volver a jugar Si o No?')

        if Reiniciar == "Si":
            juega.ReiniciarPartida()

        else:
            if Reiniciar == "No":
                print("Espero te haya gustado el juego!")
                break

            else:
                print("Porfavor escribe bien la pabalabra")

if __name__ == '__main__':  # Manda ejecutar al metodo main
    main()
