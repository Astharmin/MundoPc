class Monitor:
    contTec = 0

    def __init__(self, marca, tipo, pulgadas):
        Monitor.contTec += 1
        self._ID_Tec = Monitor.contTec
        self._marca = marca
        self._tipo = tipo
        self._pulgadas = pulgadas

    def __str__(self):
        return f'\nID: {self._ID_Tec}\nMarca: {self._marca}\nEntrada: {self._tipo}\nPulgadas: {self._pulgadas}\n'

if __name__ == '__main__':
    monitor1 = Monitor('HP', 'HDMI', 20)
    print(monitor1)

    monitor2 = Monitor('Dell', 'VGA', 35)
    print(monitor2)