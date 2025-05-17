
import math

# 1
def imprimir_hola_mundo():
    print("Hola Mundo!")


# 2
def saludar_usuario(nombre):
    return f"Hola {nombre}!"


# 3
def informacion_personal(nombre, apellido, edad, residencia):
    print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}")


# 4.1
def calcular_area_circulo(radio):
    return math.pi * (radio ** 2)


# 4.2
def calcular_perimetro_circulo(radio):
    return math.pi * 2 * radio


# 5
def segundos_a_horas(segundos):
    return segundos / 60 / 60


# 6
def tabla_multiplicar(numero):
    for i in range(1, 11):
        print(f"{i}:\t{i*numero}")


# 7
def operaciones_basicas(a, b):
    return (a+b, a-b, a*b, a/b)


# 8
def calcular_imc(peso, altura):
    return peso / (altura ** 2)


# 9
def celsius_a_fahrenheit(celsius):
    return celsius * 9 / 5 + 32


# 10
def calcular_promedio(a, b, c):
    return (a + b + c)/3


# 1
imprimir_hola_mundo()

# 2
print(saludar_usuario(input("Ingrese un nombre: ")))

# 3
informacion_personal(input("Ingrese su nombre: "), input("Ingrese su apellido: "), input("Ingrese su edad: "), input("Ingrese su residencia: "))

# 4
rad = int(input("Ingrese un radio: "))
print(calcular_area_circulo(rad))
print(calcular_perimetro_circulo(rad))

# 5
print(segundos_a_horas(int(input("Ingrese una cantidad de segundos: "))))

# 6
tabla_multiplicar(int(input("Ingrese un numero: ")))

# 7
suma, rest, mult, divi = operaciones_basicas(float(input("Ingrese el primer numero: ")), float(input("Ingrese el segundo numero: ")))
print(f"Suma: {suma}")
print(f"Resta: {rest}")
print(f"Multiplicacion: {mult}")
print(f"Division: {divi}")

# 8
print(calcular_imc(float(input("Ingrese el peso: ")), float(input("Ingrese la altura: "))))

# 9
print(celsius_a_fahrenheit(int(input("Ingrese la temperatura en celsius: "))))

# 10
print(calcular_promedio(float(input("Ingrese el primer numero: ")), float(input("Ingrese el segundo numero: ")), float(input("Ingrese el tercer numero: "))))
