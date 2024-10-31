# 4- Obtener promedio de edad de un determinado curso.

def promedio_edad_por_año(alumnos, año, division):
    total_edad = 0
    contador = 0
    
    for alumno in alumnos:
        if alumno["curso"] == (año, division):
            total_edad += alumno["edad"]
            contador += 1
    
    if contador == 0:
        return 0  

    return total_edad / contador

alumnos = [
    {"nombre": "Ana", "apellido": "Pérez", "edad": 23, "curso": (2024, 'A')},
    {"nombre": "Luis", "apellido": "González", "edad": 25, "curso": (2023, 'A')},
    {"nombre": "Juan", "apellido": "Martínez", "edad": 22, "curso": (2024, 'B')},
    {"nombre": "Sofía", "apellido": "Lopez", "edad": 24, "curso": (2023, 'A')},
    {"nombre": "Roberto", "apellido": "Hernández", "edad": 21, "curso": (2024, 'A')},
]

año_curso = 2023
division_curso = 'A'
promedio = promedio_edad_por_año(alumnos, año_curso, division_curso)

print(f"Promedio de edad para el curso {año_curso} {division_curso}: {promedio:.2f}")
