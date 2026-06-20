from modelos.recurso_atencion import RecursoAtencion

MULTA_POR_DIA = 2.50


class PrestamoLibro(RecursoAtencion):
    def __init__(self, codigo_identificador: str, titulo: str, autor: str):
        super().__init__(codigo_identificador)
        self.titulo = titulo
        self.autor = autor

    def calcular_multa(self, **kwargs) -> float:
        return self.retraso_acumulado * MULTA_POR_DIA
