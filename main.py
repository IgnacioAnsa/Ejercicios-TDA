from ejercicio 1 import cargar_alumnos
from ejercicio 2 import cargar_cursos
from ejercicio 3 import generar_preceptores_por_año
from ejercicio 4 import obtener_promedio_edad
from ejercicio 5 import buscar_preceptores_repetidos
from ejercicio 6 import buscar_preceptores_un_año
from ejercicio 7 import obtener_alumno_mas_joven_y_mas_viejo

def main():
    alumnos = []
    cursos = []

    while True:
        print("\nMenú de opciones:")
        print("1. Cargar Alumnos")
        print("2. Cargar Cursos")
        print("3. Generar Set de Preceptores por Año")
        print("4. Obtener Promedio de Edad de un Curso")
        print("5. Buscar Preceptores Repetidos en Dos Años Distintos")
        print("6. Buscar Preceptores Solo en un Año")
        print("7. Mostrar Alumno Más Joven y Más Viejo")
        print("8. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            alumnos = cargar_alumnos()
        elif opcion == "2":
            cursos = cargar_cursos()
        elif opcion == "3":
            preceptores_por_año = generar_preceptores_por_año(cursos)
            for año, preceptores in preceptores_por_año.items():
                print(f"Año {año}: {preceptores}")
        elif opcion == "4":
            curso_deseado = input("Ingrese el curso (año y división, separado por espacio): ").split()
            curso_deseado = (curso_deseado[0], curso_deseado[1])
            promedio = obtener_promedio_edad(alumnos, curso_deseado)
            print(f"Promedio de edad en el curso {curso_deseado}: {promedio}")
        elif opcion == "5":
            preceptores_repetidos = buscar_preceptores_repetidos(cursos)
            print("Preceptores repetidos en dos años distintos:")
            for preceptor, años in preceptores_repetidos.items():
                print(f"{preceptor}: {list(años)}")
        elif opcion == "6":
            año_deseado = input("Ingrese el año: ")
            preceptores_un_año = buscar_preceptores_un_año(cursos, año_deseado)
            print(f"Preceptores solo en el año {año_deseado}: {preceptores_un_año}")
        elif opcion == "7":
            alumno_mas_joven, alumno_mas_viejo = obtener_alumno_mas_joven_y_mas_viejo(alumnos)
            if alumno_mas_joven:
                print(f"Alumno más joven: {alumno_mas_joven['nombre']} {alumno_mas_joven['apellido']}, Edad: {alumno_mas_joven['edad']}")
            if alumno_mas_viejo:
                print(f"Alumno más viejo: {alumno_mas_viejo['nombre']} {alumno_mas_viejo['apellido']}, Edad: {alumno_mas_viejo['edad']}")
        elif opcion == "8":
            print("Saliendo del programa.")
            break
        else:
            print("Opción no válida, intente de nuevo.")

if __name__ == "__main__":
    main()
