import random

# 1
for i in range(1, 101):
    print(i)


# 2
num = int(input("Ingrese un numero: "))
print(len(str(num)))


# 3
num1 = int(input("Ingrse el primer numero: "))
num2 = int(input("Ingrse el segundo numero: "))
for i in range (num1+1, num2):
    print(i)


# 4
suma = 0
entrada = -1
while entrada != 0:
    entrada = float(input("Ingrese un numero: "))
    suma += entrada
print(f"La suma es {suma}")


# 5
num = random.randint(0, 9)
entrada = -1
attempt = 0
while entrada != num:
    entrada = float(input("Ingrese un numero: "))
    attempt += 1
print(attempt)


# 6
for i in reversed(range(1, 100)):
    print(i)


# 7
entrada = int(input("Ingrese un numero: "))
print(entrada*(entrada+1)/2)


# 8
cant = 100
pares = 0
impares = 0
negativos = 0
positivos = 0

for i in range(cant):
    entrada = input("Ingrese un numero: ")
    if entrada % 2 == 0:
        pares += 1
    else:
        impares += 1
    if entrada != 0:
        if entrada > 0:
            positivos += 1
        else:
            negativos += 1

print(f"Pos: {positivos}")
print(f"Neg: {negativos}")
print(f"Par: {pares}")
print(f"Imp: {impares}")


# 9
cant = 100
suma = 0
for i in range(cant):
    suma += int(input("Ingrese un numero: "))
print(suma / cant)


# 10
print("".join(reversed(str(int(input("Ingrese un numero: "))))))