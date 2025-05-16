# 1
print("Hola Mundo!")


# 2
nombre = input("¿Quien es usted?")
print(f"¡Hola {nombre}!")


# 3
nombre = input("Ingrese su nombre: ")
apellido = input("Ingrese su apellido: ")
edad = input("Ingrese su edad: ")
lugar_de_residencia = input("Ingrese su lugar de residencia: ")
print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {lugar_de_residencia}")


# 4
pi = 3.1416
radio = float(input("Ingrese el radio de un circulo: "))
print(f"Area: {pi*radio**2}")
print(f"Perimetro: {2*pi*radio}")


# 5
seg = float(input("Ingrese una cantidad de segundos: "))
print(f"En horas: {seg/60/60}")


# 6
num = float(input("Ingrese un numero: "))
for i in range(1, 11):
    print(f"{i}:\t{i*num}")


# 7
num1 = float(input("Ingrese un primer numero: "))
num2 = float(input("Ingrese un segundo numero: "))
print(f"Suma: {num1+num2}")
print(f"Resta: {num1-num2}")
print(f"Multiplicacion: {num1*num2}")
print(f"Division: {num1/num2}")


# 8
altura = float(input("Ingrese su altura: "))
peso = float(input("Ingrese su peso: "))
print(f"IMC: {peso / (altura ** 2)}")


# 9
temp_c = float(input("Ingrese una temperatura en Celsius"))
print(f"En Fahrenheit: {9/5*temp_c+32}")


# 10
num1 = float(input("Ingrese un primer numero: "))
num2 = float(input("Ingrese un segundo numero: "))
num3 = float(input("Ingrese un tercer numero: "))
print(f"Promedio: {(num1+num2+num3)/3}")
