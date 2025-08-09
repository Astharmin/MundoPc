from ClasePadre import DispoEntrada

class Mause (DispoEntrada):

    contMau = 0

    def __init__(self, marca, tipo):
        Mause.contMau +=1
        self._ID_mau = Mause.contMau
        super().__init__(marca, tipo)

    def __str__(self):
        return f'\nID: {self._ID_mau}\nMarca: {self._marca}\nEntrada: {self._tipo_entrada}\n'

if __name__ == '__main__':
    raton1 = Mause('Dell', 'USB')
    print(raton1)

    raton2 = Mause('Accer', 'Blutus')
    print(raton2)