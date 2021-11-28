import math
import statistics as stats
from math import factorial
from datetime import datetime

"""PROGRAMA 1"""
print("\n\t*****PROGRAMA1******")
nombre = input("Ingrese su nombre: ")
apellido = input("Ingrese su apellido: ")
print("Bienvenido " + nombre + apellido + " son las: " + datetime.now().strftime('%H:%M:%S'))

"""------------------------------------------------"""
"""PROGRAMA 2”"""
print("\n\t*****PROGRAMA2******")
print("Ingrese un 5 numeros: \n")
num1 = int(input("1: "))
num2 = int(input("2: "))
num3 = int(input("3: "))
num4 = int(input("4: "))
num5 = int(input("5: "))
resul = ((num1 * num2 * num3) - num4) + num5 ** 3
print("La respuesta al problema es: " + str(resul))

"""------------------------------------------------"""
"""PROGRAMA 3"""
print("\n\t*****PROGRAMA3******")
r = math.sqrt(16 + 5) + math.pi * (+5 / 2) * 3 ** 7
print("El resultado al ejercicio 3 es: {:.4f}".format(r))

"""------------------------------------------------"""
"""PROGRAMA 4"""
print("\n\t*****PROGRAMA4******")
r = factorial(9) - math.sqrt(math.sqrt(16))
print("El resultado al ejercicio 4 es: {:.4f}".format(r))

"""------------------------------------------------"""
"""PROGRAMA 5"""
print("\n\t*****PROGRAMA5******")
r = (20 - (3 / 5) * (4 / 3) + 8)
print("El resultado al ejercicio 5 es: {:.2f}".format(r))

"""------------------------------------------------"""
"""PROGRAMA 6"""
print("\n\t*****PROGRAMA6******")
xVal = int(input("Ingrese el valor de X: "))
r = math.cos(2 * xVal + 5)
print("El resultado al ejercicio 6 es: {:.2f}".format(r))

"""------------------------------------------------"""
"""PROGRAMA 7"""
print("\n\t*****PROGRAMA7******")
xVal = int(input("Ingrese el valor de x: "))
nVal = int(input("Ingrese el valor de n: "))
r = 1 + ((nVal * xVal) / factorial(1) + (nVal * (nVal - 1) * xVal ** 2) / factorial(4))
print("El resultado al ejercicio 7 es: {:.2f}".format(r))

"""------------------------------------------------"""
"""PROGRAMA 8"""
print("\n\t*****PROGRAMA8******")
print("El resultado al ejercicio 8 es: {:.2f}".format(math.log(15, 9)))

"""------------------------------------------------"""
"""PROGRAMA 9"""
print("\n\t*****PROGRAMA9******")
print("El resultado al ejercicio 9 es: {:.2f}".format(math.log(7)))

"""------------------------------------------------"""
"""PROGRAMA 10"""
print("\n\t*****PROGRAMA10******")
b = int(input("Ingrese el valor de b: "))
c = int(input("Ingrese el valor de c: "))
a = math.pi
valor1 = (-b + math.sqrt(b ** 2 - (4 * a * c))) / (2 * a)
valor2 = (-b - math.sqrt(b ** 2 - (4 * a * a))) / (2 * a)
print("Valor positivo: " + str(valor1))
print("Valor negativo: " + str(valor2))

"""------------------------------------------------"""
"""PROGRAMA 11"""
print("\n\t*****PROGRAMA11******")
r = math.pow(math.e, 0.6895528)
print("El resultado del ejercicio 11: {:.4f}".format(r))

"""------------------------------------------------"""
"""PROGRAMA 12"""
print("\n\t*****PROGRAMA12******")
a = math.pi
b = -170
print("El resultado del ejercicicio 12: {:.4f}".format(math.sqrt(math.pow(a, 2) + math.pow(b, 2))))

"""SEGUNDA PARTE"""

"""II. Considerando que:
• x = (20, -11, 42, a, -1, 8, -1, -7, 22, 𝜋 ∗ 1 )
• y = (30, -55, 12, 𝜋 ∗ 2, 10, 55, -8, 13/2,1, Sen 2)"""
print("\nSEGUNDA PARTE DE LA LISTA DE EJERCICIOS")
print("EJERCICIO 1 (SE HA CREADO LA LISTA)")
a = int(input("Ingrese el valor de a: "))
x = [20, -11, 42, a, -1, 8, -7, 22, math.pi * 1]
y = [30, -55, 12, math.pi * 2, 10, 55, -5, 13 / 2, 1, math.sin(2)]
"""EJER2"""
print("\n\tEJERCICIO 2")
print("2. Extraiga los valores de los indices 5 y 4 de cada lista.")
print("X[4]: " + str(x[4]) + "X[5]: " + str(x[5]))
print("Y[4]: " + str(y[4]) + "Y[5]: " + str(y[5]))

"""EJER3"""
print("\n\tEJERCICIO 3")
print("3. Extraiga los valores de los ultimos dos valores de y.")
print("Y[-2]: " + str(y[-2]) + " Y[-1]: " + str(y[-1]))

"""EJER4"""
print("\n\tEJERCICIO 4")
print("4. Extraiga los valores de los primeros dos valores de x.")
print("X[0]: " + str(x[0]) + " X[1]: " + str(x[1]))

"""EJER5"""
print("\n\tEJERCICIO 5")
print("5. Invierta los valores de ambas listas x & y.")
x.reverse()
y.reverse()
print("Lista X al reves: " + str(x))
print("Lista Y al revés: " + str(y))

"""EJER6"""
print("\n\tEJERCICIO 6")
print("6. De cada lista extraiga los dos valores del centro, luego sumelos y calcule el\
promedio de esos cuatro numros.")
num1 = len(x)
num2 = len(y)
aux1 = int(num1 / 2)
aux2 = int(num2 / 2)
prom = (x[aux1] + x[aux1 + 1] + y[aux2] + y[aux2 + 1]) / 4
print("El promedio es: {:.2f} ".format(prom))

"""EJER7"""
print("\n\tEJERCICIO 7")
print("7. Estimar los siguientes indices tanto de x & y:")
mediaX = stats.mean(x)
mediaY = stats.mean(y)
print("La media de X: " + str(mediaX) + " la media de Y: " + str(mediaY))
modaX = stats.mode(x)
modaY = stats.mode(y)
print("La moda de X: " + str(modaX) + " la moda de Y: " + str(modaY))
varX = stats.variance(x)
varY = stats.variance(y)
print("La varianza de X: " + str(varX) + " la varianza de Y: " + str(varY))
desvX = stats.stdev(x)
desvY = stats.stdev(y)
print("La vdesviacion de X: " + str(desvX) + " la desviacion de Y: " + str(desvY))

"""EJER8"""
print("\n\tEJERCICIO 8")
almc = {'Nic': 0.20, 'ElSal': 0.25, 'Hond': 0.3, 'CR': 0.35, 'Guat': 0.3, 'Pana': 0.4}
print("\t***********Calcula los salarios por pais***********")
salXhora = int(input("Ingrese el salario por hora : "))
horasTrab = int(input("Ingrese las horas trabajadas: "))
totalBruto = (horasTrab * salXhora)
almc["Sal_Nic"] = totalBruto - (totalBruto * almc["Nic"])
almc["Sal_ElSal"] = totalBruto - (totalBruto * almc["ElSal"])
almc["Sal_Hond"] = totalBruto - (totalBruto * almc["Hond"])
almc["Sal_CR"] = totalBruto - (totalBruto * almc["CR"])
almc["Sal_Guat"] = totalBruto - (totalBruto * almc["Guat"])
almc["Sal_Pana"] = totalBruto - (totalBruto * almc["Pana"])
print("\t*************LOS SALARIOS NETO POR PAIS********************")
print("-> NICARAGUA : " + str(almc["Sal_Nic"]))
print("-> EL SALVADOR : " + str(almc["Sal_ElSal"]))
print("-> HONDURAS : " + str(almc["Sal_Hond"]))
print("-> COSTA RICA : " + str(almc["Sal_CR"]))
print("-> GUATEMALA : " + str(almc["Sal_Guat"]))
print("-> PANAMA : " + str(almc["Sal_Pana"]))

print("\t*************ACTUALIZANDO LOS VALORES********************")
print("Ingrese el nuevo impuesto por pais: EJ: 0.15 ")
almc["Nic"] = float(input("NICARAGUA: "))
almc["ElSal"] = float(input("EL SALVADOR: "))
almc["Hond"] = float(input("HONDURAS: "))
almc["CR"] = float(input("COSTA RICA: "))
almc["Guat"] = float(input("GUATEMALA: "))
almc["Pana"] = float(input("PANAMA: "))

print("\t***************LOS VALORES HAN SIDO ACTUALIZADOS************")
