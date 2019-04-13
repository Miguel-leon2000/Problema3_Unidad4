# Esta clase (JuegoAdivinaNumero) deriva de la clase Juego
from Juego import *

"""
Se declara el nombre de la clase, y se coloca el parametro Juego, ya que es la clase padre,
para heredar atributos de ella.
"""
class JuegoAdivinaNumero(Juego):

    """
    Atributos donde se declara el numero del programa gemerado, y
    ademas de los intentos que realiza el jugador.
    """
    _NumeroPrograma = int(0)
    __Intentos = int(0)

    """
    Metodo constructor quien es el que recibe los atributos de entrada, en este caso el 
    numero de vidas esta heredado de la superclase Juego.
    """
    def __init__(self, NumeroVidas, NumeroPrograma):
        super().__init__(NumeroVidas)
        self._NumeroPrograma = NumeroPrograma

    """
    Metodo ReiniciarPartida donde se utiliza en el caso de que el jugador
    desee jugar de nuevo, redefiniendo los intentos a 0 y mandando llamr de nuevo
    al metodo juega quien es el que lleva las instrucciones del numero a adivinar.
    """
    def ReiniciarPartida(self):
        self.ReiniciarRecord()
        self._NumeroPrograma
        super().setVidas(3)
        self.Juega()

    # Metodo ActualizaRecord donde se le van aumentando 1 a los intentos realizados.
    def ActualizaRecord(self):
        self.__Intentos = self.__Intentos + 1

    # Se utiliza en el metodo ReiniciarPartida para volver a reiniciar los intentos.
    def ReiniciarRecord(self):
        self.__Intentos = 0

    # Metodo para mostrar los intentos realizados.
    def MostrarRecord(self):
        return self.__Intentos

    """
    Metodo Juega donde realiza todo el procedimiento del juego para adivinar el numero, 
    este se basa  en un ciclo while para que mientras haya vidas se vuelva a ejecutar.
    Se aplica la condicion if, teniendo en cuenta el metodo valida numero quien es el que compara el valor
    introducido por el jugador si es par o impar, al igual se emplean los metodos actualiza record para incrementar los intentos
    y ademas el metodo quitar vida en el caso de que se equivoque el jugador no adivine el numero.
    """
    def Juega(self):

        while self._NumeroVidas:

            Numero = int(input("Intenta adivinar el numero entre 0 y 10: "))

            if self.ValidaNumero(Numero):

                if (Numero == self._NumeroPrograma):

                    self.ActualizaRecord()

                    print("Acertaste!!")
                    print("Tu record es: ", self.__Intentos)
                    break

                else:

                    self.ActualizaRecord()

                    if self.QuitarVida():

                        if (Numero > self._NumeroPrograma):
                            print("Intentalo de nuevo. El numero a adivinar es menor")

                        else:
                            print("Intentalo de nuevo. El numero a adivinar es mayor")

                    else:
                        print("Lo siento has perdido el numero era: ", self._NumeroPrograma)
                        print("Tu record es: ", self.__Intentos)
            else:
                print("Introduce el numero:")

    """
    Metodo Valida numero, que se encarga de comparar si el numero introducido por jugador es par 
    o impar, teniendo en cuenta que el numero tiene que ser entre el rango 0 y 10, y va a devolver un true, en lo contrario,
    manda un mensaje indicando que escriba un numero entre ese rango, devolviendo un false.
    """

    def ValidaNumero(self, Numero):
        if Numero >= 0 and Numero <= 10:
            return True
        else:
            print("El numero debe ser entre 0 y 10!")
            return False

