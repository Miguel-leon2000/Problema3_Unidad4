# Se importa la clase JuegoAdivinaNumero quien es la clase padre
from JuegoAdivinaNumero import *

# Se declara el nombre de la clase hija de la super clase JuegoAdivinaNumero
class JuegoAdivinaPar(JuegoAdivinaNumero):

    """
    En este metodo ValidaNumero toma como parametro el numero introducido por el jugador
    para que este sea comparado, en este caso es de un numero par, aplicando la condicion
    de que el residuo de la division entre 2 debe ser igual a 0, o de lo contrario se le pide al
    jugador que introduzca el numero que se le pide, devolviendo un False.
    """
    def ValidaNumero(self, Numero):

        if (Numero % 2 == 0) and (Numero >= 0 and Numero <= 10):
            return True

        else:
            print("Error!! Porfavor introduce un numero par")
            return False
