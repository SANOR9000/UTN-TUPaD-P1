# 1
def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n-1)

entrada = int(input("Ingrese un numero: "))
for i in range(1, entrada + 1):
    print(f"{i}:\t{factorial(i)}")


# 2
def fibonacci(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibonacci(n-1) + fibonacci(n-2)

entrada = int(input("Ingrese un numero: "))
for i in range(1, entrada + 1):
    print(f"{i}:\t{fibonacci(i)}")


# 3
def potencia(n, m):
    if m == 1:
        return n
    return n * potencia(n, m-1)

num1 = int(input("Ingrese un numero: "))
num2 = int(input("Ingrese otro numero: "))
print(potencia(num1, num2))


# 4
def binario(n):
    if n // 2 == 0:
        return str(n % 2)
    return binario(n // 2) + str(n % 2)

entrada = int(input("Ingrese un numero: "))
print(entrada)


# 5
def es_palindromo(palabra):
    if len(palabra) <= 1:
        return True
    if palabra[0] == palabra[-1]:
        return es_palindromo(palabra[1:-1])
    return False
    
entrada = input("Ingrese una palabra: ")
print(es_palindromo(entrada))


# 6
def suma_digitos(n):
    if n < 10:
        return n
    return n%10 + suma_digitos(n//10)

entrada = int(input("Ingrese un numero: "))
print(suma_digitos(entrada))


# 7
def contar_bloques(n):
    if n <= 1:
        return n
    return n + contar_bloques(n-1)

entrada = int(input("Ingrese un numero: "))
print(contar_bloques(entrada))


# 8
def contar_digito(numero, digito):
    if numero <= 0:
        return 0
    return int(numero%10 == digito) + contar_digito(numero//10, digito)

num1 = int(input("Ingrese un numero: "))
num2 = int(input("Ingrese un digito: "))
print(contar_digito(num1, num2))