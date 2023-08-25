class Ordenacao():
    def __init__(self, array_para_ordenar:[]):
        self.__lista = array_para_ordenar

    def ordena(self):
        """Realiza a ordenacao do conteudo do array recebido no construtor"""

        lista = self.__lista
        ordem = []
        for i in range(len(self.__lista)):
            menor_valor = self.__lista[0]
            for j in self.__lista:
                if j < menor_valor:
                    menor_valor = j
        
            ordem.append(menor_valor)
            lista.remove(menor_valor)

        self.__ordem = ordem

        return self.__ordem
    
    def toString(self):
        """Converte o conteudo do array em String"""
        string = str(self.__ordem)[1:-1]
        string = string.replace(" ", "")
        self.__string = string

        return self.__string

entrada = "5 18 2 10 1"
teste = Ordenacao([int(w) for w in entrada.split()])
##teste = Ordenacao([int(w) for w in input().split()])
ordem = teste.ordena()
string = teste.toString()
print(string)