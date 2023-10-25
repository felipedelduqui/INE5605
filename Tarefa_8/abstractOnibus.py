from abc import ABC, abstractmethod


class AbstractOnibus(ABC):
    @abstractmethod
    def __init__(self, capacidade: int, total_passageiros: int, ligado: bool):
        pass

    # OnibusJahLigadoException
    @abstractmethod
    def ligar(self) -> str:
        pass

    # OnibusJahDesligadoException
    @abstractmethod
    def desligar(self) -> str:
        pass

    # OnibusJahCheioException
    @abstractmethod
    def embarca_pessoa(self) -> str:
        pass

    # OnibusJahVazioException
    @abstractmethod
    def desembarca_pessoa(self) -> str:
        pass

    @property
    @abstractmethod
    def capacidade(self) -> int:
        pass

    @property
    @abstractmethod
    def total_passageiros(self) -> int:
        pass

    @property
    @abstractmethod
    def ligado(self) -> bool:
        pass

    @capacidade.setter
    @abstractmethod
    def capacidade(self, capacidade: int):
        pass
