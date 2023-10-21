from ControladorJogo import *
from random import random, uniform

def partida(jogador_1, jogador_2) -> Jogador:
    for jogador in [jogador_1, jogador_2]:
        for _ in range(5):
            personagem = jogo.inclui_personagem_na_lista(int(10*random()),
                                                        int(10*random()),
                                                        int(10*random()),
                                                        int(10*random()), Tipo(int(3*random())))
            carta = jogo.inclui_carta_no_baralho(personagem)
            jogador.inclui_carta_na_mao(carta)

    contador = 0
    while True:
        contador +=1
        print(contador)

        carta_1 = jogador_1.baixa_carta_da_mao()
        carta_2 = jogador_2.baixa_carta_da_mao()

        mesa = Mesa(jogador_1, jogador_2, carta_1, carta_2)
        jogador_vencedor = jogo.jogada(mesa)

        if jogador_vencedor != None:
            return jogador_vencedor.nome

        if contador > 20:
            return None

if __name__ == '__main__':
    while True:
        jogo = ControladorJogo()

        jogador_1 = Jogador('Felipe')
        jogador_2 = Jogador('Eduardo')

        jogador_vencedor = partida(jogador_1, jogador_2)
        if jogador_vencedor != None:
            break
