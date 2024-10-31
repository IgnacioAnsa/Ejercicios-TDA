# 5- Buscar qué preceptores se encuentran repetidos en dos años

def buscar_preceptores_repetidos(cursos):
    preceptores_por_año = {}

    for curso in cursos:
        año, division = curso["año_division"]
        preceptor = curso["preceptor"]

        if preceptor in preceptores_por_año:
            preceptores_por_año[preceptor].add(año)
        else:
            preceptores_por_año[preceptor] = {año}

    preceptores_repetidos = {preceptor: años for preceptor, años in preceptores_por_año.items() if len(años) > 1}

    return preceptores_repetidos

cursos = [
    {"año_division": (2023, 'A'), "cantidad_alumnos": 30, "preceptor": "Juan"},
    {"año_division": (2023, 'B'), "cantidad_alumnos": 25, "preceptor": "Ana"},
    {"año_division": (2024, 'A'), "cantidad_alumnos": 30, "preceptor": "Juan"},
    {"año_division": (2024, 'B'), "cantidad_alumnos": 20, "preceptor": "Carlos"},
    {"año_division": (2023, 'C'), "cantidad_alumnos": 15, "preceptor": "Ana"},
    {"año_division": (2024, 'C'), "cantidad_alumnos": 10, "preceptor": "Ana"},
]

preceptores_repetidos = buscar_preceptores_repetidos(cursos)

print("Preceptores repetidos en dos años distintos:")
for preceptor, años in preceptores_repetidos.items():
    print(f"{preceptor}: {list(años)}")
