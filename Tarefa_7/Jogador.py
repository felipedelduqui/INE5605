from abc import ABC, abstractmethod
from Carta import *
from abstract.AbstractJogador import*
from random import random

class Jogador(AbstractJogador):
    def __init__(self, nome: str) -> None:
        self.__nome = nome
        self.__mao = list()

    @property
    def nome(self) -> str:
        '''
    Retorna o nome do jogador
    @return nome do jogador
    '''

        return self.__nome

    def baixa_carta_da_mao(self) ->Carta:
        '''
    Retira uma das cartas do Jogador. Esta operacao eh utilizada para realizar 
    uma jogada (baixar uma carta na mesa)
    A carta sai da mao (ou seja, a carta sai da lista das cartas que o jogador 
    possui)
    @return Retorna a Carta que foi retirada da mao do jogador (lista das cartas
    que ele possui)
    '''
        carta = self.mao[0]
        self.mao.remove(carta)

        return  carta

    @property
    def mao(self) -> list:
        '''
        @return Retorna a mao atual do jogador (lista das cartas que ele possui)
        '''

        return self.__mao

    def inclui_carta_na_mao(self, carta: Carta):
        '''
        Inclui na mao do jogador a carta passada como parametro

        @param carta Carta que sera incluida na mao do jogador
        '''

        '''@return Retorna a Carta que foi incluida no baralho'''

        self.mao.append(carta)
