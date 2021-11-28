# Ejemplo de como sería normalmente el código
lista = []

for i in range(0, 10):
    lista.append((i + 2))
print("Ejemplo de como seria de forma normal: " + str(lista))

# Ejemplo de como puede ser acortado
nueva_lista = [i * 2 for i in range(0, 10)]
print("Ejemplo utilizando comprehension: " + str(nueva_lista))

# Se puede realizar operaciones if dentro
# En este ejemplo se uso numeros pares
almc = [2, 3, 4, 5, 6, 7, 8, 9, 10]
par = [i for i in almc if i % 2 == 0]
print("Numeros pares: " + str(par))

almc2 = {f"{i} x 2 =": i * 2 for i in range(1, 6)}
print("Imprime la tabla del 2: \n")

for i in almc2.items():
    print(i)

# Almacena la temperatura de los días de la semana dentro de un diccionario
day = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
temp = [30.5, 32.6, 31.8, 33.4, 29.8, 30.2, 29.9]
print("Imprime la temperatura de cada dia de la semana: ")
temp_semanal = {dias: temp for (dias, temp) in zip(day, temp)}
for i in temp_semanal.items():
    print(i)
