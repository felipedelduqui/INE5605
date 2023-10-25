# Repositório para aula de DSOO - Desenvolvimento de Sistemas Orientados a Objetos

## Tarefa 7
### Descrição:

* Um jogo de cartas possui em cada carta o tipo de um personagem (Água, Terra, Ar, Fogo) e seus atributos: energia, habilidade, velocidade e resistência, que variam de 0 a 100.
* No jogo participam dois jogadores. Cada jogador possui cinco cartas na mão.
* Em cada rodada, cada jogador coloca uma carta na mesa. As duas cartas são então comparadas.
* Ganha a rodada o jogador que tiver maior valor total na sua carta na mesa, somando-se os valores de todos os atributos da carta.
* O jogador vencedor da rodada fica com a carta do adversário, devolvendo para sua mão a sua própria carta e a do adversário.
* Caso ocorra empate dos valores das cartas, ambos mantém suas respectivas cartas, colocando de volta cada um na sua mão.
* Caso um jogador fique sem cartas ao final de uma rodada, considere o jogo ganho pelo jogador que ainda possui cartas na mão.
* Observe que o jogo pode terminar em empate pois as somas dos atributos das cartas pode ser igual, sendo assim o número de rodadas foi limitado a 50.

## Tarefa 8
### Descrição:

* Ônibus são um meio de transporte comum. Para não violar as regras de transito é importante conhecer o estado atual do ônibus (ligado ou desligado), o número de pessoas que estão dentro do ônibus no momento e a capacidade total de pessoas permitida.
* As ações típicas de um ônibus são ligar, desligar e permitir ou não a entrada de um passageiro. Para isso, deve-se controlar a quantidade de pessoas que entram e saem do ônibus, se o ônibus está vazio (sem passageiros) ou se já está com a capacidade máxima. Também deve-se controlar se o ônibus está ligado (ligado=True) ou desligado (ligado=False).
* Esses controles são realizados por meio da implementação de exceções.
* Implemente as exceções esperadas e dispare as exceções nos momentos devidos.
* Não é necessário implementar o tratamento das exceções, pois o código de testes do Moodle já implementa esses tratamentos.
* Quando o controlador inicializar o ônibus, é importante garantir que os parâmetros de inicialização sejam válidos. Existem 4 casos que podem invalidar o comando de inicialização:
* Quando existe algum parâmetro que não é um valor inteiro ou booleano, de acordo com os respectivos tipos.
* Quando existe algum parâmetro inteiro com valor negativo.
* Se o número atual de passageiros não respeita a restrição da capacidade de passageiros dentro do ônibus.
* Se ao inicializar o ônibus for definido que o mesmo está desligado (ligado=False).
Quando qualquer um desses casos ocorrer, o comando de inicialização é considerado inválido e o ônibus deve manter seu estado anterior.