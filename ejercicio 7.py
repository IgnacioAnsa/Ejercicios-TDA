# 7- Mostrar nombre y apellido del alumno más jóven y más grande
# del colegio.

def obtener_alumno_mas_joven_y_mas_viejo(alumnos):
    if len(alumnos) == 0:
        return None, None

    alumno_mas_joven = alumnos[0]
    alumno_mas_viejo = alumnos[0]

    for alumno in alumnos:
        if alumno["edad"] < alumno_mas_joven["edad"]:
            alumno_mas_joven = alumno
        if alumno["edad"] > alumno_mas_viejo["edad"]:
            alumno_mas_viejo = alumno

    return alumno_mas_joven, alumno_mas_viejo

# Ejemplo de lista de alumnos
alumnos = [
    {"nombre": "Juan", "apellido": "Pérez", "edad": 15, "curso": ("2024", "A")},
    {"nombre": "Ana", "apellido": "Gómez", "edad": 14, "curso": ("2024", "B")},
    {"nombre": "Luis", "apellido": "Martínez", "edad": 16, "curso": ("2024", "A")},
    {"nombre": "Sofía", "apellido": "Fernández", "edad": 13, "curso": ("2024", "C")},
]

alumno_mas_joven, alumno_mas_viejo = obtener_alumno_mas_joven_y_mas_viejo(alumnos)

if alumno_mas_joven:
    print(f"Alumno más joven: {alumno_mas_joven['nombre']} {alumno_mas_joven['apellido']}, Edad: {alumno_mas_joven['edad']}")
if alumno_mas_viejo:
    print(f"Alumno más viejo: {alumno_mas_viejo['nombre']} {alumno_mas_viejo['apellido']}, Edad: {alumno_mas_viejo['edad']}")
