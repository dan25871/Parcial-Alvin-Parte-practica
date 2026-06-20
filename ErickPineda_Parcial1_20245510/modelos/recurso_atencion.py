from abc import ABC, abstractmethod


class RecursoAtencion(ABC):
    def __init__(self, codigo_identificador: str):
        self.codigo_identificador = codigo_identificador
        self.retraso_acumulado = 0

    @abstractmethod
    def calcular_multa(self, **kwargs) -> float:
        pass
