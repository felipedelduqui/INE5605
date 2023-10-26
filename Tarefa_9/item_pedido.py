class ItemPedido():
    def __init__(self, codigo: int, descricao: str, preco_unitario: float):
        self.__codigo = codigo
        self.__descricao = descricao
        self.__preco_unitario = preco_unitario

    @property
    def codigo(self) -> int:
        return self.__codigo

    @property
    def descricao(self) -> str:
        return self.__descricao

    @property
    def preco_unitario(self) -> float:
        return self.__preco_unitario

    @codigo.setter
    def codigo(self, codigo):
        self.__codigo = codigo

    @descricao.setter
    def descricao(self, descricao):
        self.__descricao = descricao

    @preco_unitario.setter
    def preco_unitario(self, preco_unitario):
        self.__preco_unitario = preco_unitario
