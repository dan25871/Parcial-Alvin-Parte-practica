from modelos.registro import Registro
from modelos.prestamo_libro import PrestamoLibro
from modelos.uso_sala_estudio import UsoSalaEstudio

print("=== COMMIT 1: Prueba base — Sistema de Atención Biblioteca ===\n")

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

registro.cargar_recurso(libro1)
registro.cargar_recurso(libro2)
registro.cargar_recurso(sala1)
registro.cargar_recurso(sala2)

print(f"\nRecursos cargados: {len(registro.recursos)}/4")
for r in registro.recursos:
    print(f"  [{r.codigo_identificador}] {r.__class__.__name__} — retraso: {r.retraso_acumulado}")

print("\n--- Probando invariante: límite de 4 recursos ---")
try:
    registro.cargar_recurso(libro3)
except ValueError as e:
    print(f"Correcto — sistema bloqueó: {e}")

print("\n--- Probando inmutabilidad de recursos ---")
try:
    registro.recursos.append(libro3)
except AttributeError as e:
    print(f"Correcto — tuple no permite modificación: {e}")

print("\n--- Auditoría de saldos (polimorfismo puro) ---")
print("  Ciclo con 3 alunos en espera (demanda baja):")
saldos_baja = registro.ejecutar_auditoria_saldos(alumnos_en_espera=3)
for codigo, multa in saldos_baja.items():
    print(f"    {codigo}: ${multa:.2f}")

print("  Ciclo con 7 alumnos en espera (demanda media):")
saldos_media = registro.ejecutar_auditoria_saldos(alumnos_en_espera=7)
for codigo, multa in saldos_media.items():
    print(f"    {codigo}: ${multa:.2f}")

print("  Ciclo con 12 alumnos en espera (demanda alta):")
saldos_alta = registro.ejecutar_auditoria_saldos(alumnos_en_espera=12)
for codigo, multa in saldos_alta.items():
    print(f"    {codigo}: ${multa:.2f}")

print("\nNota: PrestamoLibro ignora alumnos_en_espera — su multa es siempre días * $2.50")
