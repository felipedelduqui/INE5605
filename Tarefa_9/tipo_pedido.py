class TipoPedido():
    def __init__(self, descricao: str, fator_distancia: float):
        '''
        O atributo fator_distancia eh um float que representa
        o custo pela distancia percorrida para aquele tipo de pedido.
        '''
        self.__descricao = descricao
        self.__fator_distancia = fator_distancia

    @property
    def descricao(self):
        return self.__descricao

    @property
    def fator_distancia(self):
        return self.__fator_distancia
