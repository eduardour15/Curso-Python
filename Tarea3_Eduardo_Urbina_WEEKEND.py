import math as mt


# 1. Programe una funcion dinamica que consulte la cantidad de argumentos con la
# cual la misma funcionara y posterior a que el usuario ingrese la cantidad, tambien
# consulte los argumentos y sea capaz de determinar tanto el numero mas pequeño
# como el numero mas grande, considere que NO se podra utilizar las funciones
# min(), ni max() de python.
def calc_min_max(*num_funct):
    """Calcula el numero mayor y menor"""
    minimo = 100000000
    maximo = 0
    cant = len(num_funct[0])

    for cont in range(cant):
        if num_funct[0][cont] < minimo:
            minimo = num_funct[0][cont]
        else:
            maximo = num_funct[0][cont]
    print(f"El mayor: {maximo} y el menor: {minimo}")


argu = int(input("Escriba la cantidad de argumentos: "))
almc = []
for i in range(argu):
    val = int(input(f"Ingrese el valor num: {i + 1}: "))
    almc.append(val)
calc_min_max(almc)


# 2. Programe una funcion que sea capaz a partir del valor del lado de un cuadrado (3
# metros), muestre el valor de su perimetro (en centimetros) y el de su area (en
# pulgadas cuadradas) -> Al convertir la escala el perimetro debe darle 12 metros y
# el area 9 metros cuadrados.
def calc(per=3):
    perimetro = per + per + per + per
    per_centi = perimetro * 100
    area = per ** 2
    area_pulg = area * 1550
    print(f"El perimetro del cuadrado con lado {per}m es: {per_centi} cm")
    print(f"El area del cuadrado es: {area_pulg}pulg^2")


calc()


# 3. Desarrolle un programa que a partir del valor de la base y de la altura de un
# triangulo (3 y 5 metros, respectivamente), muestre el valor de su area (en metros
# cuadrados). Recuerde que el area A de un triangulo se puede calcular a partir de
# la base b y la altura h como A = 1/2 bh -> Sin embargo el programa no debe de
# permitir pasar un valor cero o negativo como parametro.

def artriang(base=0, altura_triang=0):
    """
    Función que calcula el área de un triangulo
    """
    if base > 0 or altura_triang > 0:
        area_trian = 0.5 * (base * altura_triang)
        print(f"El area del triangulo es: {area_trian}m^2")
        return
    print("No se aceptan valores igual a 0 o negativos")


while True:
    ba = int(input("Ingrese la base del triangulo: "))
    al = int(input("Ingrese la altura del triangulo: "))
    if ba > 0 and al > 0:
        break

artriang(ba, al)


# 4. El area A de un triangulo se puede calcular a partir del valor de dos de sus lados,
# a y b, y del angulo θ que estos forman entre si con la formula A = 1/2 ab sin(θ).
# Desarrolle un programa que pida al usuario el valor de los dos lados (en metros),
# el angulo que estos forman (en grados), y muestre el valor del area -> Nuevamente
# el programa no debe de permitir pasar un valor cero o negativo como parametro
# para ninguno de sus valores, tambien debe de mandar a imprimir por medio de un
# mensaje la explicación del porque la escala seleccionada (grados o radianes).

def calc_triangulo(lado_a, lado_b, grados):
    if lado_a > 0 or lado_b > 0 or grados > 0:
        resp = 0.5 * (lado_a * lado_b) * mt.sin(grados)
        option = 0
        while option != 1 and option != 2:
            print("¿En que sistema desea mostrar el resultado?")
            print("1. Grados")
            print("2. Radianes")
            option = int(input())
            if option == 1:
                print(f"El Area del triangulo em grados: {resp}")
            elif option == 2:
                print(f"El Area del triangulo en radianes: {mt.radians(resp)}")
            else:
                print("Opcion no valida, intente de nuevo")
        return
    print("No se admiten valores negativos")


lado1 = int(input("Escriba el valor del lado A del triangulo (metros): "))
lado2 = int(input("Escriba el valor del lado B del triangulo (metros): "))
angulo = int(input("Escriba el angulo que forman el lado A y B (grados): "))

calc_triangulo(lado1, lado2, angulo)


# 5. Desarrolle un programa que, dados diez numeros cualquiera, los vuelva enteros
# y determine cual de los ultimos nueve numeros es mas cercano al primero.
# (Ejemplo, si el usuario introduce los numeros 2, 6, 4, 8, 12.5, 9.1, 1, 3, 1 y 10, la
# funcion respondera que el numero mas cercano al 2 es el 1 -> No se debe de
# permitir el ingreso de cero y si lo hacemos el programa no tiene porque reiniciar
# la entrada de todos los numeros.

def conv_entero(calc_entero):
    for cont2 in range(len(calc_entero)):
        calc_entero[cont2] = int(calc_entero[cont2])

    numero = calc_entero[0]
    menor_conv = 0
    mayor = 0
    for cont2 in range(1, len(calc_entero)):
        if calc_entero[cont2] == numero:
            print(f"El valor más cercano al {numero} es: {calc_entero[cont2]}")
            return calc_entero
        if calc_entero[cont2] < numero:
            menor_conv = calc_entero[cont2]
        if calc_entero[cont2] > numero:
            mayor = calc_entero[cont2]

    if (mayor - numero) < (numero - menor_conv):
        print(f"El valor más cercano al {numero} es: {mayor}")
    else:
        print(f"El valor más cercano al {numero} es: {menor_conv}")
    return calc_entero


lista = []
num = 1
cony = 1
while cony <= 10:
    num = float(input(f"Ingrese el numero {cony}:"))
    if num > 0:
        cony += 1
        lista.append(num)
    else:
        print("El numero debe ser mayor a cero ")

print("Los numeros convertidos en entero: ")
print(conv_entero(lista))


# 6. Desarrolle un programa que dado cinco puntos en el plano cartesiano, determine
# cual de los cuatro ultimos puntos es mas cercano al primero. Un punto se
# representara con dos variables: una para la abcisa y otra para la ordenada. La
# distancia entre dos puntos (x1, y1) y (x2, y2) es !(𝑥1 − 𝑥2)! + (𝑦1 − 𝑦2)!


def calc_distancia(or_x, or_y, des_x, des_y):
    """La función aceptaa valores en el orden:
        funcion(origenX, origenY, destinoX, destinoY)"""
    result = mt.sqrt((or_x - des_x) ** 2 + (or_y - des_y) ** 2)
    return result


origen_x = float(input("Ingrese el primer punto del plano en X: "))
origen_y = float(input("Ingrese el primer punto plano en Y: "))
menor = 10000000000000
respuesta = 0
saveX = -1
saveY = -1
for i in range(2, 5):
    destino_x = float(input(f"Ingrese el punto en X #{i}: "))
    destino_y = float(input(f"Ingrese el punto en Y #{i}: \n"))
    aux = calc_distancia(origen_x, origen_y, destino_x, destino_y)
    if aux < menor:
        menor = aux
        respuesta = i
        saveX = destino_x
        saveY = destino_y

print(f"El punto más cercano al primero es el {respuesta} (X={saveX}, Y={saveY})")


# 7. Implemente un programa o funcion que muestre todos los multiplos de n entre n y
# m*n, ambos inclusive, donde n y m son numeros introducidos por el usuario.

def calc_multiplos(n_multiplos, m):
    """Devuelve una listra con los múltiplos ingresados"""
    high = n_multiplos * m
    list_multiplos = []
    for j in range(1, high):
        list_multiplos.append(j * n_multiplos)

    return list_multiplos


n_val = int(input("Ingrese el valor de n: "))
m_val = int(input("Ingrese el valor de m: "))

list_almc = calc_multiplos(n_val, m_val)

print(f"Los multiplos entre {n_val} y {n_val}*{m_val} son: ")
print(list_almc)

# 8. Desarrolle un programa que dada una cantidad dada por el cliente de un banco,
# solicite el desglose en billetes y monedas de una cantidad entera de euros. En la
# actualidad existen billetes de 500, 200, 100, 50, 20, 10 y 5 € y monedas de 2 y 1
# €, por lo cual se debe recorrer los valores de billete y monedas disponibles
# almacenados en la bobeda con uno o mas bucles for-in para lograr determinar
# cuantos billetes y monedas entregar, asi como saber cuanto queda aun disponible
# para atender a los demas clientes, esta sucursal al inicio del dia llama a la oficina
# central para informar con que cantidad quiere operar todos los dias.

cantBilletes = {"500": 0, "200": 0, "100": 0, "50": 0, "20": 0, "10": 0, "5": 0, "2": 0, "1": 0}

almc = {"500": 0, "200": 0, "100": 0, "50": 0, "20": 0, "10": 0, "5": 0, "2": 0, "1": 0}
print("\n*******INGRESANDO LA CANTIDAD DE DINERO EN SUCURSAL**********")
for k in cantBilletes.keys():
    cantBilletes[k] = int(input(f"Ingrese la cantidad de dinero en la denominación de {k}: "))

print("Los billetes guardados en boveda")

billetes_entr = [500, 200, 100, 50, 20, 10, 5, 2, 1]
while True:
    almc = {"500": 0, "200": 0, "100": 0, "50": 0, "20": 0, "10": 0, "5": 0, "2": 0, "1": 0}
    cant_cliente = int(input("Escriba la cantidad de dinero a retirar: "))
    for x in billetes_entr:
        if cant_cliente >= x:
            queda = cant_cliente // x
            if queda < cantBilletes[str(x)]:
                cantBilletes[str(x)] -= queda
                almc[str(x)] = queda
            else:
                continue
            cant_cliente %= x

    for n in almc:
        if almc[n] > 0:
            print(f"Se entregará {n}: {almc[n]}")
        else:
            continue

    opc = input("¿Desea seguir retirando dinero? (S/N)")
    if opc == 's' or opc == 'S':

        continue
    elif opc == 'n' or opc == 'N':
        break
    else:
        print("Opcion incorrecta")

#
# 9. Escriba un programa que sea capaz de dibujar las siguientes formas a partir de la
# seleccion y valores introducidos por el usuario, ejemplo:

hexadec = int(input("Escriba la cant. de asterisco en los lados del Hexágono: "))
aux_hex = hexadec - 1
for i in range(hexadec, 3 * hexadec, 2):
    print(" " * aux_hex + "*" * i)
    aux_hex -= 1
aux_hex = 1
for i in range(3 * hexadec - 4, hexadec - 2, -2):
    print(" " * aux_hex + "*" * i)
    aux_hex += 1

altura = int(input("Ingrese la altura del cuadro: "))
ancho = int(input("Ingrese el ancho del cuadro: "))
for i in range(altura):
    print(" *" * ancho)

altura2 = int(input("Ingrese la altura del triangulo: "))
for x in range(altura2 + 1):
    print(" *" * x)

# 10. La secuencia de Collatz de un número entero se construye de la siguiente forma:
# • Si el número es par, se lo divide por dos;
# • Si es impar, se le multiplica tres y se le suma uno;
# • La sucesión termina al llegar a uno.

num_collatz = int(input("Ingrese un numero: "))

while num_collatz != 1:
    if num_collatz % 2 == 0:
        num_collatz = num_collatz / 2
    else:
        num_collatz = num_collatz * 3 + 1
    print(f"{int(num_collatz)}: " + "* " * int(num_collatz))
