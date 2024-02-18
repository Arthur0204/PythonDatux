# 1.Realizar un programa que pida tus datos personales y mostrar en pantalla los datos solisitados

# Solicitar al usuario que ingrese sus datos personales
nombre = input("Ingrese su nombre: ")
apellido = input("Ingrese su apellido: ")
edad = input("Ingrese su edad: ")
ciudad = input("Ingrese su ciudad: ")
pais = input("Ingrese su país: ")

# Mostrar los datos ingresados por el usuario
print("\nDatos personales:")
print("Nombre:", nombre)
print("Apellido:", apellido)
print("Edad:", edad)
print("Ciudad:", ciudad)
print("País:", pais)

# 2.Realizar un programa que calcule el area y el perimetro de un poligono a tu eleccion( triangulo , cuadrado , circulo)
import math

def calcular_area_perimetro(opcion):
    if opcion == "triangulo":
        lado1 = float(input("Ingrese la longitud del primer lado del triángulo: "))
        lado2 = float(input("Ingrese la longitud del segundo lado del triángulo: "))
        lado3 = float(input("Ingrese la longitud del tercer lado del triángulo: "))

        # Calcular el perímetro del triángulo
        perimetro = lado1 + lado2 + lado3

        # Utilizar la fórmula de Herón para calcular el área del triángulo
        semi_perimetro = perimetro / 2
        area = math.sqrt(semi_perimetro * (semi_perimetro - lado1) * (semi_perimetro - lado2) * (semi_perimetro - lado3))

        return area, perimetro

    elif opcion == "cuadrado":
        lado = float(input("Ingrese la longitud del lado del cuadrado: "))

        # Calcular el área del cuadrado
        area = lado ** 2

        # Calcular el perímetro del cuadrado
        perimetro = 4 * lado

        return area, perimetro

    elif opcion == "circulo":
        radio = float(input("Ingrese el radio del círculo: "))

        # Calcular el área del círculo
        area = math.pi * (radio ** 2)

        # Calcular el perímetro del círculo
        perimetro = 2 * math.pi * radio

        return area, perimetro

    else:
        return None, None

# Solicitar al usuario que elija una opción
opcion = input("Elija una opción (triangulo, cuadrado, circulo): ")

# Calcular el área y el perímetro según la opción elegida
area, perimetro = calcular_area_perimetro(opcion)

# Mostrar los resultados
if area is not None and perimetro is not None:
    print("El área del", opcion, "es:", area)
    print("El perímetro del", opcion, "es:", perimetro)
else:
    print("Opción inválida.")

# 3.Realizar un programa que nos pida el ingreso total de un hogar y vaya pidiendo posibles gastos . Como resultado debe decir  todos los egresos y el ahorro.

# Solicitar al usuario el ingreso total del hogar
ingreso_total = float(input("Ingrese el ingreso total del hogar: "))

# Inicializar una lista para almacenar los gastos
gastos = []

# Solicitar al usuario los gastos uno por uno hasta que ingrese "fin"
while True:
    gasto = input("Ingrese un gasto (o escriba 'fin' para terminar): ")
    if gasto.lower() == 'fin':
        break
    else:
        gastos.append(float(gasto))

# Calcular la suma de todos los gastos
total_gastos = sum(gastos)

# Calcular el ahorro restante
ahorro = ingreso_total - total_gastos

# Mostrar todos los egresos y el ahorro
print("\nEgresos:")
for i, gasto in enumerate(gastos, start=1):
    print(f"Gasto {i}: ${gasto:.2f}")
print(f"\nIngreso total del hogar: ${ingreso_total:.2f}")
print(f"Total de gastos: ${total_gastos:.2f}")
print(f"Ahorro: ${ahorro:.2f}")

# 4.Realizar un programa que filtre si eres apto para registrar un negocio ,condiciones: mayor de edad , tener ruc y tener un nombre comercial ,los inputs son si y /o no . la salida debe ser si esta apto o no para abrir un comercio.

# Solicitar al usuario las condiciones para abrir un negocio
mayor_edad = input("¿Eres mayor de edad? (si/no): ").lower()
tiene_ruc = input("¿Tienes RUC? (si/no): ").lower()
tiene_nombre_comercial = input("¿Tienes un nombre comercial? (si/no): ").lower()

# Verificar las condiciones
if mayor_edad == 'si' and tiene_ruc == 'si' and tiene_nombre_comercial == 'si':
    print("¡Estás apto para abrir un negocio!")
else:
    print("No cumples con todas las condiciones para abrir un negocio.")

