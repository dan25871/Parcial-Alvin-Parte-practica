from modelos.recurso_atencion import RecursoAtencion


class UsoSalaEstudio(RecursoAtencion):
    def __init__(self, codigo_identificador: str, nombre_sala: str):
        super().__init__(codigo_identificador)
        self.nombre_sala = nombre_sala

    def calcular_multa(self, alumnos_en_espera: int = 0, **kwargs) -> float:
        return self.retraso_acumulado * self._factor_por_demanda(alumnos_en_espera)

    def es_sala_de_alta_demanda(self, alumnos_en_espera: int) -> bool:
        return alumnos_en_espera > 10

    def _factor_por_demanda(self, alumnos_en_espera: int) -> float:
        if alumnos_en_espera >= 10:
            return 5.00
        if alumnos_en_espera >= 5:
            return 3.00
        return 1.50
