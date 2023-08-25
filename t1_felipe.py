class Ordenacao():
    def __init__(self, array):
        self.__lista = array

    def ordena(self):
        """Realiza a ordenacao do conteudo do array recebido no construtor"""
        lista = self.__lista
        ordem = []
        while len(lista) != 0:
            ordem.append(min(lista))
            lista.remove(min(lista))
        
        self.__ordem = ordem

        return self.__ordem
    
    def to_string(self):
        """Converte o conteudo do array em String"""
        string = str(self.__ordem)[1:-1]
        string = string.replace(" ", "")
        self.__string = string

        return self.__string