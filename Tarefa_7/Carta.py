from abstract.AbstractCarta import *
from Personagem import *

class Carta():
    def __init__(self, personagem: Personagem):
        self.__personagem = personagem

    def valor_total_carta(self) -> int:
        '''Soma e retorna todos os valores dos atributos
        do personagem da Carta

        @return Retorna o somatorio de todos os atributos do personagem da Carta'''

        valor = (self.personagem.energia + self.personagem.habilidade +
                 self.personagem.resistencia + self.personagem.velocidade)

        return valor

    @property
    def personagem(self) -> Personagem:
        '''Retorna para o personagem da carta'''

        return self.__personagem
