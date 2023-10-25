from abc import ABC, abstractmethod
from onibus import Onibus


class AbstractControladorOnibus(ABC):
    @abstractmethod
    def __init__(self):
        pass

    '''
    Metodo para ligar o onibus. Se o onibus ja estiver ligado, dispara a excecao
    @return Mensagem informando o que ocorreu com o onibus 
    @throws OnibusJahLigadoException 
    '''
    @abstractmethod
    def ligar(self) -> str:
        pass

    '''
    Metodo para desligar o onibus. Se o onibus ja estiver desligado, dispara a excecao
    @return Mensagem informando o que ocorreu com o onibus 
    @throws OnibusJahDesligadoException 
    '''
    @abstractmethod
    def desligar(self) -> str:
        pass

    '''
    Um passageiro entra no onibus. Se nao for possivel permitir o embarque, dispara a excecao
    @return Mensagem informando o que ocorreu com o onibus 
    @throws OnibusJahCheioException 
    '''
    @abstractmethod
    def embarca_pessoa(self) -> str:
        pass

    '''
    Um passageiro sai do onibus. Se nao for possivel permitir o desembarque, dispara a excecao
    @return Mensagem informando o que ocorreu com o onibus 
    @throws OnibusJahVazioException 
    '''
    @abstractmethod
    def desembarca_pessoa(self) -> str:
        pass

    '''
    @return Onibus
    '''
    @property
    @abstractmethod
    def onibus(self) -> Onibus:
        pass

    '''
    @param capacidade total permitida de passageiros
    @param total_pessoas total de pessoas atual no onibus
    @param ligado utilizado para definir se onibus esta ligado=True ou ligado=False
    '''
    @abstractmethod
    def inicializar_onibus(self, capacidade: int, total_passageiros: int, ligado: bool):
        pass
