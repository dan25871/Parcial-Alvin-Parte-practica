from abc import ABC, abstractmethod


class RecursoAtencion(ABC):
    def __init__(self, codigo_identificador: str):
        self.codigo_identificador = codigo_identificador
        self.retraso_acumulado = 0

    @abstractmethod
    def calcular_multa(self, **kwargs) -> float:
        pass

    def es_sala_de_alta_demanda(self, alumnos_en_espera: int) -> bool:
        return False
