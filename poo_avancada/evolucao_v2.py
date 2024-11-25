#!/usr/bin/python3
class Humano:
    # atributo de classe
    especie = 'Hmo Sapiens'

    def __init__(self, nome):
        self.nome = nome


    def das_cavernas(self):
        self.especie = 'Homo Neanderthalensis'
        return self
    
    @staticmethod
    def especies():
        adjetivos = ('Habilis', 'Erectus', 'Neanderthalensis', 'Sapiens')
        return ('Autralopiteco', ) + tuple(f'Homo {adj}' for adj in adjetivos)
    
    @classmethod
    def is_evoluido(cls):
        return cls.especie == cls.especies()[-1]


class Neanderthal(Humano):
    especie = Humano.especies()[-2]


class HomoSapiens(Humano):
    especie = Humano.especies()[-1]


if __name__ == '__main__':
    jose = HomoSapiens('José')
    grokn = Neanderthal('Grokn')
    print(f'Evolução (a partir da classe): {", ".join(HomoSapiens.especies())}')
    print(f'Evolução (a partir da instância): {", ".join(jose.especies())}')
    print(f'Homo Sapiens evoluido? {HomoSapiens.is_evoluido()}')
    print(f'Neanderthal evoluido? {Neanderthal.is_evoluido()}')
    print(f'José evolucido? {jose.is_evoluido()}')
    print(f'Grokn evolucido? {grokn.is_evoluido()}')