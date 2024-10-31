# 2- Cargar secuencialmente una lista de cursos, cada curso debe
# ser un diccionario con dos claves: una tupla que contenga año y
# división, debe tener cargada como valor la cantidad de alumnos y
# el preceptor a cargo

def cargar_cursos():

    lista_cursos = []

    while True:

        año = (input("ingrese el año del curso (o salir para finalizar): "))
        if año.lower() == "salir":
            break

        division = input("ingrese la division del curso: ")
        cantidad_alumnos = int(input("ingrese la cantidad de alumnos: "))
        preceptor = input("ingrese el nombre del preceptor: ")

        curso = {

        "año_division": (año, division),
        "cantidad_alumnos": cantidad_alumnos,
        "preceptor": preceptor
        }

    lista_cursos.append(curso)

    return lista_cursos

cursos_cargados = cargar_cursos()

for curso in cursos_cargados:
    print(curso)



