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

## Tarefa 9
### Descrição

* Nesta atividade, você fará a implementação de um sistema de controle de entregas (delivery). O sistema permite o cadastro de clientes e pedidos, e calcula o valor total devido.

* Um pedido tem um tipo, um cliente e uma lista de itens.
Ele permite o calculo total do pedido com base no preço de cada item e na distância de entrega.

* Caso o cliente seja um cliente fidelidade, ele tem um desconto no total a ser pago.

* Dependendo do tipo do pedido, haverá um fator de distância para aquele pedido. Por exemplo, produtos perecíveis ou frágeis podem ter um fator distância maior que outros tipos de entrega mais simples.

* O sistema tem um controlador que controla a lista de pedidos e calcula o faturamento total com todos os pedidos de um determinado cliente.

-------------------------------------------------------------------------------------------------

### Pontuação:
* Questão 01 (1.5 PONTO) - Definição de Classes e Associações:

A estrutura das Classes e Associações deve estar exatamente igual ao modelo de classes. Qualquer diferença de nomes de atributos, tipos de dados, assinaturas de operações, etc. serão descontadas. Siga exatamente o que está definido no diagrama de classes.

* Questão 02 (1.0 PONTO) - Instanciar Controlador, Pedidos e Clientes:

O Controlador, Pedidos e Clientes devem poder ser instanciados seguindo as assinaturas dos construtores definidos no diagrama de classes. Os atributos devem ser implementados para receber os parâmetros dos construtores definidos.

* Questão 03 (2.0 PONTOS) - Manipulação das listas do controlador

Deve ser possível incluir e excluir pedidos no controlador. Prestar muita atenção quanto a inclusão de valores nulos ou de tipos diferentes, tratar tentativa de inserir entidades duplicadas. Não podem ser cadastrados dois pedidos com o mesmo número.

* Questão 04 (2.0 PONTOS) - Implementação da classe Pedido

Deve ser possível incluir e excluir itens no pedido. Prestar muita atenção quanto a inclusão de valores nulos ou de tipos diferentes, tratar tentativa de inserir entidades duplicadas. Não podem ser cadastrados dois itens com o mesmo código.

* Questão 05 (1.0 PONTO) - Herança

Herança deve ser implementada corretamente.

* Questão 06 (2.0 PONTOS) - Cálculo dos pedidos

Calculo correto do faturamento dos pedidos de um cliente identificado pelo seu cpf, considerando uma distancia dada. Considere atentamente os comentários nos métodos calcular_faturamento_pedidos e calcula_valor_pedido.

Para cada pedido do cliente, deve ser calculado o valor individual. O valor individual leva em consideração o fator distância e se o cliente é ou não um cliente fidelidade. Os valores individuais são somados no cálculo do faturamento total.

* Questão 07 (0.5 PONTO) - Estilo de código:

O estilo do código de todas as classes deve estar de acordo com o pep8.