from modelos.registro import Registro
from modelos.prestamo_libro import PrestamoLibro
from modelos.uso_sala_estudio import UsoSalaEstudio

libro1 = PrestamoLibro("PL-001", "Clean Code", "Robert C. Martin")
libro2 = PrestamoLibro("PL-002", "Estructuras de Datos", "Thomas Cormen")
sala1  = UsoSalaEstudio("US-001", "Sala B-204")
sala2  = UsoSalaEstudio("US-002", "Sala A-101")
libro3 = PrestamoLibro("PL-003", "Python Fluente", "Luciano Ramalho")

libro1.retraso_acumulado = 3
libro2.retraso_acumulado = 0
sala1.retraso_acumulado  = 2
sala2.retraso_acumulado  = 5

registro = Registro(
    id_registro="REG-20260620-001",
    carnet_alumno="20245510",
    nombre_empleado="Erick Pineda",
    codigo_usuario="BLIB-042",
)

print(f"Registro ID   : {registro.id_registro}")
print(f"Carnet alumno : {registro.carnet_alumno}")
print(f"Bibliotecario : {registro.bibliotecario.nombre_empleado} ({registro.bibliotecario.codigo_usuario})")
print(f"Estado        : {registro.estado}")

registro.cargar_recurso(libro1)
registro.cargar_recurso(libro2)
registro.cargar_recurso(sala1)
registro.cargar_recurso(sala2)

print(f"\nRecursos cargados: {len(registro.recursos)}/4")
for r in registro.recursos:
    print(f"  [{r.codigo_identificador}] {r.__class__.__name__} — retraso: {r.retraso_acumulado}")

try:
    registro.cargar_recurso(libro3)
except ValueError as e:
    print(f"sistema bloqueó: {e}")

try:
    registro.recursos.append(libro3)
except AttributeError as e:
    print(f"Correcto — tupla no permite que lo modifique: {e}")

saldos = registro.ejecutar_auditoria_saldos(alumnos_en_espera=7)
for codigo, multa in saldos.items():
    print(f"  {codigo}: ${multa:.2f}")
promedio = sum(saldos.values()) / len(saldos)
print(f"  Promedio: ${promedio:.2f} — Estado: {registro.estado}")



libro_pesado = PrestamoLibro("PL-010", "Cálculo", "Gaus")
sala_pesada  = UsoSalaEstudio("US-010", "Sala C-301")
libro_pesado.retraso_acumulado = 8   
sala_pesada.retraso_acumulado  = 10  

registro_a = Registro(
    id_registro="REG-20260620-002",
    carnet_alumno="20241100",
    nombre_empleado="Leonel Messi",
    codigo_usuario="BLIB-099",
)
registro_a.cargar_recurso(libro_pesado)
registro_a.cargar_recurso(sala_pesada)

saldos_a = registro_a.ejecutar_auditoria_saldos(alumnos_en_espera=12)
promedio_a = sum(saldos_a.values()) / len(saldos_a)
for codigo, multa in saldos_a.items():
    print(f"  {codigo}: ${multa:.2f}")
print(f"  Promedio: ${promedio_a:.2f} — Estado: {registro_a.estado}")

try:
    registro_a.ejecutar_auditoria_saldos(alumnos_en_espera=12)
except RuntimeError as e:
    print(f"sistema bloqueó: {e}")

sala_b = UsoSalaEstudio("US-020", "Sala D-102")
sala_b.retraso_acumulado = 1  

registro_b = Registro(
    id_registro="REG-20260620-003",
    carnet_alumno="20243300",
    nombre_empleado="Daniel Baires", #Mi segundo nombre y apelido jejej
    codigo_usuario="AUX-017",
)
registro_b.cargar_recurso(sala_b)

saldos_b = registro_b.ejecutar_auditoria_saldos(alumnos_en_espera=11)
promedio_b = sum(saldos_b.values()) / len(saldos_b)
for codigo, multa in saldos_b.items():
    print(f"  {codigo}: ${multa:.2f}")
print(f"  Promedio: ${promedio_b:.2f} (bajo) — Estado: {registro_b.estado}")

try:
    registro_b.ejecutar_auditoria_saldos(alumnos_en_espera=11)
except RuntimeError as e:
    print(f"sistema bloqueó: {e}")
