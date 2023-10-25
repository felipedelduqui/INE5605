from abstractOnibus import AbstractOnibus
from onibusJahCheioException import OnibusJahCheioException
from onibusJahVazioException import OnibusJahVazioException
from onibusJahLigadoException import OnibusJahLigadoException
from onibusJahDesligadoException import OnibusJahDesligadoException


class Onibus(AbstractOnibus):
    def __init__(self, capacidade: int, total_passageiros: int, ligado: bool):
        self.__capacidade = capacidade
        self.__total_passageiros = total_passageiros
        self.__ligado = ligado

    def ligar(self) -> str:
        '''
        Metodo para ligar o onibus. Se o onibus ja estiver ligado, dispara a
        excecao
        @return Mensagem informando o que ocorreu com o onibus
        @throws OnibusJahLigadoException
        '''

        if self.ligado is True:
            raise OnibusJahLigadoException()
        else:
            self.__ligado = True
            return print("Onibus ligado")

    def desligar(self) -> str:
        '''
        Metodo para ligar o onibus. Se o onibus ja estiver ligado, dispara a
        excecao
        @return Mensagem informando o que ocorreu com o onibus
        @throws OnibusJahLigadoException
        '''

        if self.ligado is False:
            raise OnibusJahDesligadoException()
        else:
            self.__ligado = False
            return print("Onibus desligado")

    def embarca_pessoa(self) -> str:
        '''
        Metodo para embarcar pessoa no onibus. Se o onibus ja estiver cheio,
        dispara a excecao
        @return Mensagem informando o que ocorreu com o onibus
        @throws OnibusJahCheioException
        '''

        if self.total_passageiros == self.capacidade:
            raise OnibusJahCheioException()
        else:
            self.__total_passageiros += 1
            return print("Pessoa embarcada")

    def desembarca_pessoa(self) -> str:
        '''
        Metodo para desembarcar pessoa no onibus. Se o onibus ja estiver vazio,
        dispara a excecao
        @return Mensagem informando o que ocorreu com o onibus
        @throws OnibusJahVazioException
        '''

        if self.total_passageiros == 0:
            raise OnibusJahVazioException()
        else:
            self.__total_passageiros -= 1
            return print("Pessoa embarcada")

    @property
    def ligado(self):
        return self.__ligado

    @property
    def total_passageiros(self):
        return self.__total_passageiros

    @property
    def capacidade(self):
        return self.__capacidade

    @capacidade.setter
    def capacidade(self, capacidade: int):
        self.__capacidade = capacidade
