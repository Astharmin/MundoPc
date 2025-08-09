from ClasePadre import DispoEntrada

class Teclado (DispoEntrada):

    contTec = 0

    def __init__(self, marca, tipo):
        Teclado.contTec +=1
        self._ID_Tec = Teclado.contTec
        super().__init__(marca, tipo)

    def __str__(self):
        return f'\nID: {self._ID_Tec}\nMarca: {self._marca}\nEntrada: {self._tipo_entrada}'

if __name__ == '__main__':
    teclado1 = Teclado('Geymer', 'Wifi')
    print(teclado1)

