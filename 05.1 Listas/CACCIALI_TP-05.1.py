# 1
print(list(range(4, 101, 4)))


# 2
lst = "elementos que mas te gusten".split()
print(lst[-1])


# 3
lst = []
lst.append("agregar")
lst.append("tres")
lst.append("palabras")
print(lst)


# 4
animales = ["perro", "gato", "conejo", "pez"]
animales[1] = "loro"
animales[-1] = "oso"
print(animales)


# 5
# Remueve el numero mas grande de la lista contenida en la variables "numeros"


# 6
lst = list(range(10, 35, 5))
print(lst[:2])


# 7
autos = ["sedan", "polo", "suran", "gol"]
autos[1] = "valores"
autos[2] = "cualesquiera"


# 8
dobles = []
for i in range(5, 20, 5):
    dobles.append(i*2)
print(dobles)


# 9
compras = [["pan", "leche"], ["arroz", "fideos", "salsa"], ["agua"]]
compras[2].append("jugo")
compras[1][1] = "tallarines"
compras[0].remove("pan")
print(compras)


# 10
lista_anidada = [15, True, [25.5, 57.9, 30.6], False]
print(lista_anidada)