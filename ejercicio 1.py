# 1- Cargar secuencialmente una lista de alumnos, cada alumno
# debe ser un diccionario con cuatro claves: nombre, apellido, edad y
# la clave curso que posea de valor una tupla con el curso.

def cargar_alumnos():

    lista_alumnos = []

    while True:

        nombre = input("ingrese el nombre del alumno (o salir para finalizar): ")
        
        if nombre.lower() == "salir":
            break

        apellido = input("ingrese el apellido del alumno: ")
        
        edad = int(input("ingrese la edad del alumno: "))
        
        curso = input("ingrese el curso del alumno: ")

        alumno = {
            "nombre": nombre,
            "apellido": apellido,
            "edad": edad,
            "curso": (curso,)
        }

        lista_alumnos.append(alumno)

    return lista_alumnos

alumnos_cargados = cargar_alumnos()

for alumno in alumnos_cargados:
    print(alumno)
