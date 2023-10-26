from pedido_duplicado_exception import PedidoDuplicadoException
from pedido import Pedido


class ControladorPedidos():
    def __init__(self):
        self.__pedidos = list()

    @property
    def pedidos(self):
        return self.__pedidos

    def busca_pedido_por_numero(self, numero: int):
        '''
        Busca pedido pelo numero.
        Se o pedido nao existir, deve retornar None
        Caso contrario, retorna o pedido.
        '''

        for pedido in self.pedidos:
            if pedido.numero == numero:
                return pedido

        return None

    def incluir_pedido(self, pedido: Pedido):
        '''
        Incluir pedido na lista.
        Tratar os casos de instancias incorretas e pedido duplicado.
        Caso o pedido já exista na lista, gerar a excecao:
        PedidoDuplicadoException
        '''
        if isinstance(pedido, Pedido):
            for pedido_na_lista in self.pedidos:
                if pedido_na_lista.numero == pedido.numero:
                    raise PedidoDuplicadoException()

            self.__pedidos.append(pedido)
            return pedido

    def excluir_pedido(self, numero: int):
        '''
        Exclui pedido pelo numero.
        Se o pedido nao existir, deve retornar None
        Caso contrario, retorna o pedido excluido
        '''

        pedido = self.busca_pedido_por_numero(numero)
        if pedido is not None:
            self.__pedidos.remove(pedido)
            return pedido

        return None

    def calcular_faturamento_pedidos(self, distancia: float, cpf: str):
        '''
        Deve calcular o total do faturamento para todos os
        itens pedidos por um CPF.
        Recebe como parametro:
        distancia: um float que corresponde a distancia percorrida
        cpf: uma string representando o CPF do Cliente a ser faturado
        '''

        valor_total = 0
        for pedido_na_lista in self.pedidos:
            if pedido_na_lista.cliente.cpf == cpf:

                valor_pedido = pedido_na_lista.calcula_valor_pedido(distancia)
                valor_total += valor_pedido

        return valor_total
