from Ob_Hijo import Mause
from Ob_Hijo2 import Teclado
from Objeto import Monitor


class Computadora:

    contComp = 0

    def __init__(self, nombre, monitor, teclado, raton):
        Computadora.contComp += 1
        self._IDcomp = Computadora.contComp
        self._nombre = nombre
        self._monitor = monitor
        self._teclado = teclado
        self._raton = raton

    def __str__(self):
        return f'''  
ID Computadora: {self._IDcomp}
Nombre: {self._nombre}

Monitor: {self._monitor}

Teclado: {self._teclado}

Raton: {self._raton}
    
'''

if __name__ == '__main__':
    teclado1 = Teclado('Dragon', 'USB')
    raton1 = Mause('Dell', 'USB')
    monitor1 = Monitor('HP', 'HDMI', 40)

    computadora1 = Computadora('GamerPro',monitor1,teclado1,raton1)
    print(computadora1)