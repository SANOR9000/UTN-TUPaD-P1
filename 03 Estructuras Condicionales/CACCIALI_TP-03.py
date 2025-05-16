# 1
edad = float(input("Ingrese su edad: "))
if edad > 18:
    print("Es mayor de edad")


# 2
nota = float(input("Ingrese la nota: "))
if nota >= 6:
    print("Aprobado")
else:
    print("Desaprobado")


# 3
num = float(input("Ingrese un numero: "))
if num % 2 == 0:
    print("Ha ingresado un número par")
else:
    print("Por favor, ingrese un número par")


# 4
edad = float(input("Ingrese su edad: "))
if edad < 12:
    print("Niño/a")
elif edad < 18:
    print("Adolescente")
elif edad < 30:
    print("Adulto/a joven")
else:
    print("Adulto/a")


# 5
password = input("Ingrese una contraseña: ")
if 8 <= len(password) <= 14:
    print("Ha ingresado una contraseña correcta")
else:
    print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres")


# 6
from statistics import mode, median, mean  # noqa: E402   pylint: disable=wrong-import-position
import random  # noqa: E402   pylint: disable=wrong-import-position

numeros_aleatorios = [random.randint(1, 100) for i in range(50)]
if mean(numeros_aleatorios) > median(numeros_aleatorios) > mode(numeros_aleatorios):
    print("Sesgo positivo o a la derecha")
elif mean(numeros_aleatorios) < median(numeros_aleatorios) < mode(numeros_aleatorios):
    print("Sesgo negativo o a la izquierda")
else:
    print("Sin sesgo")


# 7
frase = input("Ingrese una palabra o frase: ")
if frase[-1].upper() in ["A", "E", "I", "O", "U"]:
    frase = f"{frase}!"
print(frase)


# 8
nombre = input("Ingrese su nombre: ")
print("1. Si quiere su nombre en mayúsculas. Por ejemplo: PEDRO.")
print("2. Si quiere su nombre en minúsculas. Por ejemplo: pedro.")
print("3. Si quiere su nombre con la primera letra mayúscula. Por ejemplo: Pedro.")
opcion = int(input("Ingrese un numero para seleccionar la opcion correspondiente: "))
if opcion == 1:
    nombre = nombre.upper()
if opcion == 2:
    nombre = nombre.lower()
if opcion == 3:
    nombre = nombre.title()
print(nombre)


# 9
magnitud = float(input("Ingrese la magnitud del terremoto: "))
if magnitud < 3:
    print("Muy leve")
elif magnitud < 4:
    print("Leve")
elif magnitud < 5:
    print("Moderado")
elif magnitud < 6:
    print("Fuerte")
elif magnitud < 7:
    print("Muy fuerte")
else:
    print("Extremo")


# 10
hemisferio = input("Ingrese en que hemisferio se encuentra (N/S): ").title()
mes = input("Ingrese que mes es como numero: ").title()
dia = int(input("Ingrese que dia es como numero: "))

if mes in ["Enero", "Febrero"] or (mes == "Diciembre" and dia >= 21) or (mes == "Marzo" and dia <= 20):
    periodo = 0
elif mes in ["Abril", "Mayo"] or (mes == "Marzo" and dia >= 21) or (mes == "Junio" and dia <= 20):
    periodo = 1
elif mes in ["Julio", "Agosto"] or (mes == "Junio" and dia >= 21) or (mes == "Septiembre" and dia <= 20):
    periodo = 2
else:
    periodo = 3

if hemisferio == "N":
    estaciones = ["Invierno", "Primavera", "Verano", "Otoño"]
else:
    estaciones = ["Verano", "Otoño", "Invierno", "Primavera"]

output = estaciones[periodo]
print(f"Usted se encuentra en la estacion: {output}")
