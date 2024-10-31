# 6- Buscar qué preceptores se encuentran solo en un determinado
# año.

def buscar_preceptores_un_año(cursos, año_determinado):
    preceptores_por_año = {}

    for curso in cursos:
        año, division = curso["año_division"]
        preceptor = curso["preceptor"]

        if preceptor not in preceptores_por_año:
            preceptores_por_año[preceptor] = set()
        
        preceptores_por_año[preceptor].add(año)

    preceptores_un_año = {preceptor: años for preceptor, años in preceptores_por_año.items() if len(años) == 1 and año_determinado in años}

    return preceptores_un_año

cursos = [
    {"año_division": (2023, 'A'), "cantidad_alumnos": 30, "preceptor": "Juan"},
    {"año_division": (2023, 'B'), "cantidad_alumnos": 25, "preceptor": "Ana"},
    {"año_division": (2024, 'A'), "cantidad_alumnos": 30, "preceptor": "Juan"},
    {"año_division": (2024, 'B'), "cantidad_alumnos": 20, "preceptor": "Carlos"},
    {"año_division": (2023, 'C'), "cantidad_alumnos": 15, "preceptor": "Ana"},
    {"año_division": (2024, 'C'), "cantidad_alumnos": 10, "preceptor": "Pedro"},
]

año_determinado = 2023
preceptores_solo_un_año = buscar_preceptores_un_año(cursos, año_determinado)

print(f"Preceptores que solo se encuentran en el año {año_determinado}:")
for preceptor, años in preceptores_solo_un_año.items():
    print(f"{preceptor}: {list(años)}")
