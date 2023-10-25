from abstractControladorOnibus import AbstractControladorOnibus
from comandoInvalidoException import ComandoInvalidoException
from onibus import Onibus


class ControladorOnibus(AbstractControladorOnibus):

    def __init__(self):
        self.__onibus = None

    def ligar(self) -> str:
        '''
        Metodo para ligar o onibus. Se o onibus ja estiver ligado, dispara a
        excecao
        @return Mensagem informando o que ocorreu com o onibus
        @throws OnibusJahLigadoException
        '''

        self.onibus.ligar()

    def desligar(self) -> str:
        '''
        Metodo para desligar o onibus. Se o onibus ja estiver desligado,
        dispara a excecao
        @return Mensagem informando o que ocorreu com o onibus
        @throws OnibusJahDesligadoException
        '''

        self.onibus.desligar()

    def embarca_pessoa(self) -> str:
        '''
        Um passageiro entra no onibus. Se nao for possivel permitir o
        embarque, dispara a excecao
        @return Mensagem informando o que ocorreu com o onibus
        @throws OnibusJahCheioException
        '''
        self.onibus.embarca_pessoa()

    def desembarca_pessoa(self) -> str:
        '''
        Um passageiro sai do onibus. Se nao for possivel permitir o
        desembarque, dispara a excecao
        @return Mensagem informando o que ocorreu com o onibus
        @throws OnibusJahVazioException
        '''
        self.onibus.desembarca_pessoa()

    @property
    def onibus(self) -> Onibus:
        '''
        @return Onibus
        '''

        return self.__onibus

    def inicializar_onibus(self, capacidade: int,
                           total_passageiros: int,
                           ligado: bool):
        '''
        @param capacidade total permitida de passageiros
        @param total_pessoas total de pessoas atual no onibus
        @param ligado utilizado para definir se onibus esta ligado=True ou
        ligado=False
        '''
        if (isinstance(capacidade, int) and
                isinstance(total_passageiros, int) and
                isinstance(ligado, bool) and
                capacidade >= total_passageiros and
                capacidade >= 1 and
                total_passageiros >= 0):
            onibus = Onibus(capacidade,
                            total_passageiros,
                            ligado)
            self.__onibus = onibus
        else:
            raise ComandoInvalidoException()
