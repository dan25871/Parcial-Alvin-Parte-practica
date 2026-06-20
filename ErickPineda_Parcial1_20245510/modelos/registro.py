from modelos.bibliotecario import Bibliotecario
from modelos.recurso_atencion import RecursoAtencion

LIMITE_RECURSOS_POR_ATENCION = 4


class Registro:
    def __init__(
        self,
        id_registro: str,
        carnet_alumno: str,
        nombre_empleado: str,
        codigo_usuario: str,
    ):
        self.id_registro = id_registro
        self.carnet_alumno = carnet_alumno
        self.bibliotecario = Bibliotecario(nombre_empleado, codigo_usuario)
        self._recursos: list[RecursoAtencion] = []

    def cargar_recurso(self, recurso: RecursoAtencion) -> None:
        if len(self._recursos) >= LIMITE_RECURSOS_POR_ATENCION:
            raise ValueError(
                f"La atención ya alcanzó el límite de {LIMITE_RECURSOS_POR_ATENCION} recursos por alumno"
            )
        self._recursos.append(recurso)

    def quitar_recurso(self, recurso: RecursoAtencion) -> None:
        self._recursos.remove(recurso)

    def ejecutar_auditoria_saldos(self, **parametros) -> dict[str, float]:
        return {
            recurso.codigo_identificador: recurso.calcular_multa(**parametros)
            for recurso in self._recursos
        }

    @property
    def recursos(self) -> tuple:
        return tuple(self._recursos)
