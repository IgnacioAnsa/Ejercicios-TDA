# 3- Generar un set de preceptores para cada año

def generar_preceptores_por_año(cursos):
    preceptores_por_año = {}

    for curso in cursos:
        año = curso["año_division"][0]
        preceptor = curso["preceptor"]

        if año in preceptores_por_año:
            preceptores_por_año[año].add(preceptor)
        else:
            preceptores_por_año[año] = {preceptor}

    return preceptores_por_año

cursos = [
    {"año_division": (2023, 'A'), "cantidad_alumnos": 30, "preceptor": "Juan"},
    {"año_division": (2023, 'B'), "cantidad_alumnos": 25, "preceptor": "Ana"},
    {"año_division": (2024, 'A'), "cantidad_alumnos": 20, "preceptor": "Juan"},
    {"año_division": (2024, 'B'), "cantidad_alumnos": 22, "preceptor": "Luis"},
    {"año_division": (2023, 'A'), "cantidad_alumnos": 30, "preceptor": "Ana"},
]

preceptores = generar_preceptores_por_año(cursos)

for año, preceptores_set in preceptores.items():
    print(f"Año: {año}, Preceptores: {preceptores_set}")
