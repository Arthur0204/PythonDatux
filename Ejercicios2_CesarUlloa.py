#1. Crear un menu iterativo con las siguientes opciones 
#       opcion 1 'Saludar' , pedir datos personales
#       opcion 2 Realizar una operacion matematica pedir 2 numeros 
#       opcion 3 Agregar a lista un diccionario que tenga (nombre ,edad ,correo,cursos). Los cursos sera a su vez una lista de diccionario que tendra las llaves de nombre de curso y listado de notas
#       opcion 4 calcular el promedio de las notas y agregar las notas finales a una lista  
#       opcion 5 mostrar listado de alumnos aprobados 
#       opcion 6 mostrar listado de alumnos desaprobados
#       opcion 7 Generar una funcion rango hasta un numero grande (10^10) con un step y agregar a una lista los numeros que cumplan la condicion de ser multiplo de 2 ,  5 y de 7.Finalmente mostrar el tamaño de esa lista.
#       opcion 8 llamar a una funcion que devuelva el mayor de 2 numeros ingresados por teclado.
#       opcion 9 Salir. 

def saludar():
    nombre = input("Ingrese su nombre: ")
    edad = input("Ingrese su edad: ")
    correo = input("Ingrese su correo electrónico: ")
    print(f"¡Hola {nombre}! Bienvenido.")

def operacion_matematica():
    try:
        num1 = float(input("Ingrese el primer número: "))
        num2 = float(input("Ingrese el segundo número: "))
        suma = num1 + num2
        resta = num1 - num2
        multiplicacion = num1 * num2
        division = num1 / num2
        print("Resultado de la suma:", suma)
        print("Resultado de la resta:", resta)
        print("Resultado de la multiplicación:", multiplicacion)
        print("Resultado de la división:", division)
    except ValueError:
        print("Error: Ingrese valores numéricos válidos.")

def agregar_alumno(lista_alumnos):
    alumno = {}
    alumno["nombre"] = input("Ingrese el nombre del alumno: ")
    alumno["edad"] = input("Ingrese la edad del alumno: ")
    alumno["correo"] = input("Ingrese el correo electrónico del alumno: ")
    alumno["cursos"] = []
    cursos = int(input("Ingrese la cantidad de cursos: "))
    for _ in range(cursos):
        curso = {}
        curso["nombre"] = input("Ingrese el nombre del curso: ")
        notas = input("Ingrese las notas del curso separadas por comas: ")
        curso["notas"] = [float(nota.strip()) for nota in notas.split(",")]
        alumno["cursos"].append(curso)
    lista_alumnos.append(alumno)

def calcular_promedio_notas(lista_alumnos):
    notas_finales = []
    for alumno in lista_alumnos:
        for curso in alumno["cursos"]:
            promedio = sum(curso["notas"]) / len(curso["notas"])
            notas_finales.append(promedio)
    return notas_finales

def mostrar_alumnos_aprobados(lista_alumnos):
    print("Alumnos aprobados:")
    for alumno in lista_alumnos:
        promedios = calcular_promedio_notas([alumno])
        promedio_general = sum(promedios) / len(promedios)
        if promedio_general >= 11:
            print(f"- {alumno['nombre']}")

def mostrar_alumnos_desaprobados(lista_alumnos):
    print("Alumnos desaprobados:")
    for alumno in lista_alumnos:
        promedios = calcular_promedio_notas([alumno])
        promedio_general = sum(promedios) / len(promedios)
        if promedio_general < 11:
            print(f"- {alumno['nombre']}")

def generar_lista_multiplos():
    numeros_multiplos = []
    for num in range(1, 10**10):
        if num % 2 == 0 and num % 5 == 0 and num % 7 == 0:
            numeros_multiplos.append(num)
    print("Tamaño de la lista de múltiplos:", len(numeros_multiplos))

def mayor_de_dos_numeros():
    try:
        num1 = float(input("Ingrese el primer número: "))
        num2 = float(input("Ingrese el segundo número: "))
        print("El mayor número es:", max(num1, num2))
    except ValueError:
        print("Error: Ingrese valores numéricos válidos.")

def menu():
    lista_alumnos = []
    while True:
        print("\nMENU")
        print("1. Saludar")
        print("2. Realizar una operación matemática")
        print("3. Agregar un alumno")
        print("4. Calcular promedio de notas")
        print("5. Mostrar alumnos aprobados")
        print("6. Mostrar alumnos desaprobados")
        print("7. Generar lista de múltiplos")
        print("8. Mayor de dos números")
        print("9. Salir")
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            saludar()
        elif opcion == "2":
            operacion_matematica()
        elif opcion == "3":
            agregar_alumno(lista_alumnos)
        elif opcion == "4":
            notas_finales = calcular_promedio_notas(lista_alumnos)
            print("Promedio de notas finales:", sum(notas_finales) / len(notas_finales))
        elif opcion == "5":
            mostrar_alumnos_aprobados(lista_alumnos)
        elif opcion == "6":
            mostrar_alumnos_desaprobados(lista_alumnos)
        elif opcion == "7":
            generar_lista_multiplos()
        elif opcion == "8":
            mayor_de_dos_numeros()
        elif opcion == "9":
            break
        else:
            print("Opción no válida. Intente nuevamente.")

if __name__ == "__main__":
    menu()



