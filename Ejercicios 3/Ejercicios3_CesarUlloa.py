#Lista de Ejercicios nro3

#1.Una tienda de autopartes necesita un programa para catalogar sus productos,crear la clase catalogo
# y producto, realizar un objeto dentro de un catalgo de productos el cual debe tener un metodo para agregar
# productos el cual debe tener un metodo para agregar productos y otra para mostrar toda la lista de productos.

class Producto:
    def __init__(self, codigo, nombre, precio):
        self.codigo = codigo
        self.nombre = nombre
        self.precio = precio

    def __str__(self):
        return f"Código: {self.codigo}, Nombre: {self.nombre}, Precio: {self.precio}"


class Catalogo:
    def __init__(self):
        self.productos = []

    def agregar_producto(self, producto):
        self.productos.append(producto)

    def mostrar_productos(self):
        if self.productos:
            print("Lista de productos:")
            for producto in self.productos:
                print(producto)
        else:
            print("El catálogo está vacío")

#2. Realizar un programa que tenga una clase producto el cual solo tiene los atributos de nombre y codigo
# el codigo tiene la siguiente estructura PAIS-LOTE-AÑO ejemplo:PERU-00001-2024 crear un metodo que imprima el objeto de forma 
# literal (__str__) y que permita identificar el pais de origen y nro de lote

class Producto:
    def __init__(self, nombre, codigo):
        self.nombre = nombre
        self.codigo = codigo

    def __str__(self):
        return f"Nombre: {self.nombre}, Código: {self.codigo}"

    def identificar_origen_lote(self):
        partes_codigo = self.codigo.split("-")
        pais = partes_codigo[0]
        lote = partes_codigo[1]
        print(f"País de origen: {pais}, Número de lote: {lote}")

#3. Del siguiente texto :
"""
Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.
"""
# realizar al menos 4 funciones de string 

texto = """
Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.
"""
#Función para contar la cantidad de veces que aparece una palabra en el texto
def contar_palabra(texto, palabra):
    return texto.count(palabra)
#Función para convertir el texto a minúsculas
def texto_minusculas(texto):
    return texto.lower()
#Función para encontrar la posición de la primera aparición de una palabra en el texto
def encontrar_palabra(texto, palabra):
    return texto.find(palabra)
#Función para reemplazar una palabra por otra en el texto
def reemplazar_palabra(texto, palabra_antigua, palabra_nueva):
    return texto.replace(palabra_antigua, palabra_nueva)

#4. crear un archivo nuevo y realizar una funcion que permita dividir 2 numeros, importar esta funcion
# ponerlo en un bucle while True , y al ser llamada la importacion ponerlo dentro de un try except 
# ejecutar la funcion hasta que realice correctamente la division luego de eso romper el bucle

from operación import dividir

while True:
    try:
        a = float(input("Ingrese el primer número: "))
        b = float(input("Ingrese el segundo número: "))
        resultado = dividir(a, b)
        print("El resultado de la división es:", resultado)
        break  # Salir del bucle si la división se realiza con éxito
    except ValueError:
        print("Error: Ingrese solo números.")
    except ZeroDivisionError:
        print("Error: No se puede dividir por cero.")
