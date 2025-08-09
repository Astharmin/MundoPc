class DispoEntrada:
    def __init__(self, marca, tipo_entrada):
        self._marca = marca
        self._tipo_entrada = tipo_entrada

if __name__ == '__main__':
    pc = DispoEntrada('Dell', 'Raton')
    pc2 = DispoEntrada('Dell', 'Raton')
    print(f'tipo de marca: {pc2._marca}\nTipo de entrada: {pc._tipo_entrada}')

    print(pc)
    print(pc2)
    
    if pc == pc2:
        print('son objetos iguales')
    else:
        print('Son objetos diferentes')