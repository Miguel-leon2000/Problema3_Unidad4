# Se importa la libreria "abc" para crear el metodo Juega abstracto
import abc
from abc import ABC

# Se declara la clase Juego (Clase padre) teniendo como parametro la libreria "ABC"
class Juego(ABC):

    # Atributo, en este caso NumeroVidas esta protegido ya que se lo hereda a la clase JuegoAdivinaNumero
    _NumeroVidas = int(0)

    def __init__(self, NumeroVidas):
        self._NumeroVidas = NumeroVidas

    """
    Metodo abstracto Juega en el que no toma parametros y solo devuelve 0,
    ya que no esta definidas las sentencias, es decir las instrucciones e implementa las clases
    En la clase JuegoAdivinaNumero.
    """
    @abc.abstractmethod
    def Juega(self):
        return 0

    """
    Metodo QuitarVida en el que resta una vida, en el caso de que el jugador no adivine
    el numero del programa. Se aplica la condicion if, teniendo en cuenta que si el 
    numero de vidas es mayor a 0, sigue mostrando el mensaje de que vuelva a introducir el numero
    mientras que si es menor a 0, devuelve falso y se terminan las oportunidades del jugador.
    """
    def QuitarVida(self):
        self._NumeroVidas = self._NumeroVidas - 1

        if (self._NumeroVidas > 0):
            return True

        else:
            return False

    # Metodo getVidas, que funciona para obtener el valor del atributo NumeroVidas
    def getVidas(self):
        return self._NumeroVidas

    # Metodo setVidas, que se utiliza para realizar modificaciones al atributo NumeroVidas
    def setVidas(self, Vidas):
        self._NumeroVidas = Vidas
