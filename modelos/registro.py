from modelos.bibliotecario import Bibliotecario
from modelos.recurso_atencion import RecursoAtencion

LIMITE_RECURSOS_POR_ATENCION = 4
UMBRAL_MULTA_PROMEDIO = 15.00


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
        self.estado = "ACTIVA"

    def cargar_recurso(self, recurso: RecursoAtencion) -> None:
        if len(self._recursos) >= LIMITE_RECURSOS_POR_ATENCION:
            raise ValueError(
                f"La atención ya alcanzó el límite de {LIMITE_RECURSOS_POR_ATENCION} recursos por alumno"
            )
        self._recursos.append(recurso)

    def quitar_recurso(self, recurso: RecursoAtencion) -> None:
        self._recursos.remove(recurso)

    def ejecutar_auditoria_saldos(self, **parametros) -> dict[str, float]:
        if self.estado == "CUENTA_SUSPENDIDA":
            raise RuntimeError(
                f"Operación bloqueada: la cuenta del alumno {self.carnet_alumno} está suspendida por protocolo de restricción"
            )
        saldos = {
            recurso.codigo_identificador: recurso.calcular_multa(**parametros)
            for recurso in self._recursos
        }
        self._verificar_restriccion(saldos, **parametros)
        return saldos

    def _verificar_restriccion(self, saldos: dict[str, float], alumnos_en_espera: int = 0, **kwargs) -> None:
        if saldos and sum(saldos.values()) / len(saldos) > UMBRAL_MULTA_PROMEDIO:
            self.estado = "CUENTA_SUSPENDIDA"
            return

        bibliotecario_es_auxiliar = self.bibliotecario.codigo_usuario.startswith("AUX")
        tiene_sala_de_alta_demanda = any(
            r.es_sala_de_alta_demanda(alumnos_en_espera) for r in self._recursos
        )
        if bibliotecario_es_auxiliar and tiene_sala_de_alta_demanda:
            self.estado = "CUENTA_SUSPENDIDA"

    @property
    def recursos(self) -> tuple:
        return tuple(self._recursos)
