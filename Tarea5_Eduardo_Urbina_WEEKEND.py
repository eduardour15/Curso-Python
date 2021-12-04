import pandas as pd
from random import randint
from datetime import datetime
from pandas.core import indexing
import webbrowser
from time import sleep

def menu_Master():
    try:
        while True:
            print("\t******Tarea N.5******\n")
            print("\t******ESCRIBA EL NUMERO DEL EJERCICIO******\n")
            print("\t******1. Ejercio #1 ")
            print("\t******2. Ejercio #2 ")
            print("\t******3. Ejercio #3 ")
            print("\t******4. Ejercio #4 ")
            print("\t******5. Ejercio #5 ")
            print("\t******6. Ejercio #6")
            print("\t******7. Ejercio #7 ")
            print("\t******8. Ejercio #8 ")
            print("\t******9. Ejercio #9 ")
            print("\t******10. Ejercio #10 ")
            print("\t******11. Salir ")
            opc = int(input("\t-----> "))
            if opc <= 0 or opc > 11:
                raise IndexError
            else:
                return opc
    except TypeError:
        print("No se permiten caracteres")
    except IndexError:
        print("Necesita ingresar un valor en el rango")
    except ValueError:
        print("Intenta ingresar un valor valido")


opc_master = 0
while opc_master != 11:
    
    opc_master=menu_Master()
    if opc_master == 1:
        """1. Realiza una función llamada añadir_una_vez(lista, elemento) que reciba una lista
        y un elemento.
        La función debe añadir el elemento al final de la lista con la condición de no repetir
        ningún elemento. Además si este elemento ya se encuentra en la lista se debe
        invocar un error de tipo ValueError que debe capturar y mostrar el siguiente
        mensaje en pantalla (haga uso de colores si le es posible):
        """

        def anadir_una_vez(lista, elemento):
            """[summary]

            Args:
                lista (list): una lista de entero
                elemento (int): [variable de tipo entero]

            Raises:
                ValueError: Si existe un elemento duplicado, levantará una excepción

            Returns:
                [type]: retorna la lista con el nuevo elemento añadido al final
            """
            while True:
                try:
                    if elemento in lista:
                        raise ValueError
                except ValueError:
                    print(
                        "\033[4;35m"+"Error: Imposible añadir elementos duplicados => "+str(elemento)+"\033[0m")
                    return lista
                else:
                    lista.append(elemento)
                    print("Hemos añadido el valor")
                    return lista

        lista = []
        num = int(input("-> Escriba cuantos números seleccionsará a la lista: "))
        cont = 0
        while num > cont:
            valor = int(input("\033[0m"+"-> Entrada=> "))
            lista = anadir_una_vez(lista, valor)
            cont += 1
        print(f"La lista: {lista}")
    elif opc_master == 2:
        """2. Escribir una función que reciba un string y retorne True si es un palíndromo (esto
        es, aquellas palabras se leen igual de izquierda a derecha o de derecha a
        izquierda), False en caso contrario.
        Utilizar esta función en un programa que permita al usuario seleccionsar palabras
        hasta que seleccionse la palabra “Terminar” (suponer que todas las palabras son en
        minúsculas o todas en mayúsculas, de forma consistente). Al finalizar, mostrar la
        cantidad de palíndromos seleccionsados.
        Debe de proteger al programa de no permitir seleccionso de numeros o combinaciones
        haciendo uso del manejo de errores o excepciones.
        Ejemplo de ejecución:
        1. Cadena: abba
        2. Cadena: m
        3. Cadena: luz
        4. Cadena: reconocer
        5. Cadena: golondrina
        6. Cadena: fin
        7. Cantidad de palíndromos: 3
        """

        def palindromo(cadena):
            if cadena in cadena[::-1]:
                return True
            else:
                return False

        cont_palindromo = 0
        while True:
            try:
                cadena = input("-> Escriba una cadena: ")
                if any(x.isdigit() for x in cadena):
                    raise TypeError
            except TypeError:
                print("El valor introducido no es una cadena")
            else:
                if cadena.casefold() == "terminar":
                    break
                ver = palindromo(cadena.lower())
                if ver == True:
                    print(f"-> Palindromo: {cadena}")
                    cont_palindromo += 1

        print(f"Se seleccionsaron {cont_palindromo} palindromos")

    elif opc_master == 3:
        """3. Una empresa tiene salas de juegos para todas las edades y quiere calcular de
        forma automática el precio que debe cobrar a sus clientes por entrar. El programa
        debe preguntar al usuario la edad del cliente y mostrar el precio de la entrada. Si
        el cliente es menor de 4 años no puede entrar, si tiene entre 4 y 10 años paga $5,
        11 a 18 años paga $10 y si es mayor de 18 años, $15.
        Desarrolle el programa asegurando que todos los posibles errores que pueden
        producirse estaran cubiertos, para garantizar que el programa no se caera
        (terminara) a menos que el usuario sea consultado y este acepte.
        """

        def calcPrecio(edad):
            if edad <= 0 or edad < 4:
                print("El niño no puede seleccionsar ")
            elif edad >= 4 or edad <= 10:
                print("El usuario pagara $5")
            elif edad >= 11 or edad <= 18:
                print("El usuario pagara $10")
            elif edad > 18:
                print("El usuario pagara $15")
            else:
                print("Edad incorrecta")

        while True:
            try:
                edad_user = int(input("==> Digite su edad: "))
            except:
                print("==> Se espera un número entero")
                resp = input("==>¿Desea continuar con la ejecucion? [s/n] ")
                if len(resp) == 1 and resp.isalpha():
                    if resp.lower() == "s":
                        pass
                    elif resp.lower() == "n":
                        print("Adios.....")
                        break
                    else:
                        print("Necesita introducir un solo carácter ==> 's/n' ")
                else:
                    print("Necesita introducir un solo carácter ==> 's/n' ")
            else:
                calcPrecio(edad_user)
                try:
                    salida=input("¿Desea continuar? (s/n): ")
                    if salida.lower() =='n':
                        break
                    elif salida.lower() =='s':
                        continue
                    else: 
                        print("Ingrese una opcion valida, el programa continuara")
                except Exception: 
                    print("Opcion invalida, el programa continara ")
    elif opc_master == 4:
        """4. La Pizzería Napolitana ofrece opciones vegetarianas y no vegetarianas a sus
        clientes. Los Ingredientes para cada tipo de pizza aparecen a continuación.
        • Ingredientes vegetarianos: Pimiento ($3) y tofu ($5).
        • Ingredientes no vegetarianos: Peperoni ($4), Jamón ($2), piña ($3) y
        Salmón ($10).
        Escribir un programa que pregunte a traves de un menu al usuario por los
        Ingredientes, y en función de su respuesta le diga si es una pizza vegetariana o
        no.
        Solo puede eligir un selecciondiente además de la mozzarella ($2) y el tomate ($2)
        que están en todas la pizzas.
        Al final adicional a mostrar por pantalla si la pizza confeccionada es vegetariana
        o no con todos sus Ingredientes que lleva, tambien tome en cuanta que el
        establecimiento unicamente opera de martes a domingo, por lo cual el dueño
        necesita almacenar en un archivo de bases de datos BDs.CSV la bitacora de
        dichas ventas al sumar los costos de cada selecciondiente seleccionado para luego
        analizar dicha información en excel.
        """

        def menu_pizza():
            while True:
                try:
                    print("\t*****Escriba que llevará su pizza*****")
                    print("\t*****MENU*****")
                    print("\t->1. Pimiento")
                    print("\t->2. Tofu")
                    print("\t->3. Peperonio")
                    print("\t->4. Jamón")
                    print("\t->5. Piña")
                    print("\t->6. Salmon")
                    print("\t->7. Salir")
                    opc_selecciondiente = int(input("\t-> "))
                    if opc_selecciondiente < 1 or opc_selecciondiente > 7:
                        raise IndexError
                    return opc_selecciondiente
                except IndexError:
                    print("Intenta escribir un número dentro de la selección")
                except ValueError:
                    print("Intenta no seleccionsar una letra ")

        seleccion = 0
        registro_pizza = {"Id_factura": [], "Id_Cliente": [],
                        "Fecha": [], "Tipo": [], "Ingredientes": [], "Precio": []}
        i = 0
        while True:
            seleccion = menu_pizza()

            if seleccion >= 1 and seleccion <= 2:
                registro_pizza["Tipo"].append("Vegetariana")
            elif seleccion >= 3 and seleccion <= 6:
                registro_pizza["Tipo"].append("No Vegetariana")
            if seleccion == 1:
                registro_pizza["Ingredientes"].append("Pimiento")
                registro_pizza["Precio"].append("$7")
            elif seleccion == 2:
                registro_pizza["Ingredientes"].append("Tofu")
                registro_pizza["Precio"].append("$9")
            elif seleccion == 3:
                registro_pizza["Ingredientes"].append("Peperoni")
                registro_pizza["Precio"].append("$8")
            elif seleccion == 4:
                registro_pizza["Ingredientes"].append("Jamon")
                registro_pizza["Precio"].append("6$")
            elif seleccion == 5:
                registro_pizza["Ingredientes"].append("Piña")
                registro_pizza["Precio"].append("$7")
            elif seleccion == 6:
                registro_pizza["Ingredientes"].append("Salmon")
                registro_pizza["Precio"].append("$14")
            elif seleccion == 7:
                print("Los datos han sido guardado correctamente")
                print(registro_pizza)
                break
            registro_pizza["Id_factura"].append(randint(1, 1000))
            registro_pizza["Id_Cliente"].append(randint(1000, 2000))
            registro_pizza["Fecha"].append(
                datetime.today().strftime('%Y-%m-%d'))
            print(f'La pizza confeccionada es: {registro_pizza["Tipo"][i]}')
            i += 1
        df = pd.DataFrame(registro_pizza, columns=[
            'Id_factura', 'Id_Cliente', 'Fecha', 'Tipo', 'Ingredientes', 'Precio'])
        df.to_csv("Pizzeria-registro.csv")
    elif opc_master == 5:
        """5. El método de multiplicación rusa consiste en multiplicar sucesivamente por 2 el
        multiplicando y dividir por 2 el multiplicador hasta que el multiplicador tome el valor
        1. Luego, se suman todos los multiplicandos correspondientes a los
        multiplicadores impares.
        Dicha suma es el producto de los dos números. La siguiente tabla muestra el
        cálculo realizado para multiplicar 37 por 12, cuyo resultado final es 12 + 48 + 384
        = 444.
        """
        while True:
            try:
                resp_mult = 0
                multi_1 = int(input("Escriba el multiplicador: "))
                multi_2 = int(input("Escriba el multiplicando: "))
                if multi_1 <= 0 or multi_2 <= 0:
                    raise ZeroDivisionError
                aux1 = multi_1
                aux2 = multi_2
                while aux1 != 0:
                    if aux1 % 2 != 0:
                        resp_mult = resp_mult+aux2
                    aux1 = aux1//2
                    aux2 = aux2*2
                print(
                    f"El resultado de la multiplicación ->{multi_1} x {multi_2} = {resp_mult}")
                break
            except ZeroDivisionError:
                print("Intenta no ingresar valores negativos o ceros")
            except ValueError:
                print("Se espera un número positivo no un caracter")

    elif opc_master == 6:
        """
        Escriba un programa que pida al usuario que ingrese varios valores enteros, que
        pueden ser positivos o negativos. Cuando se ingrese un cero, el programa debe
        terminar y mostrar un gráfico de cuántos valores positivos y negativos fueron
        ingresados
        """
        val_pos = 0
        val_neg = 0
        while True:
            try:
                val = int(input("Ingrese valores y termine con cero: "))
                if val > 0:
                    val_pos += 1
                elif val < 0:
                    val_neg += 1
                elif val == 0:
                    print("\nPositivo: ", end="")
                    for x in range(0, val_pos):
                        print("*", end="")
                    print("\nNegativo: ", end="")
                    for x in range(0, val_neg):
                        print("*", end="")
                    break
            except ValueError:
                print("No se puede ingresar un caracter")

    elif opc_master == 7:
        """"En finanzas, el VAN (valor actual neto) es un indicador de cuán rentable será un
        proyecto y se calcula sumando los flujos de dinero de cada mes divididos por
        (1+r)n, donde n es el número del mes y r es la tasa de descuento mensual, y
        restando la inversión inicial"""
        numMes = 1
        VAN = 0
        while VAN <= 0:
            try:
                inverInicial = int(input("Inversion inicial: "))
                if inverInicial <= 0:
                    raise ZeroDivisionError
                tasaDesc = int(input("% tasa de descuento: "))
                if tasaDesc <= 0:
                    raise ZeroDivisionError
            except ValueError:
                print("intenta no ingresar un caracter")
            except ZeroDivisionError:
                print("No puedes ingresar un valor negativo o cero")
            else:
                while True:
                    try:
                        flujo = int(input(f"Flujo de mes {numMes}: "))
                    except ValueError:
                        print("Intenta no ingrear un caracter ")
                    except ZeroDivisionError:
                        print("No puedes ingresar un valor negativo o cero ")
                    if numMes == 1:
                        VAN = int((inverInicial*-1) +
                                (flujo/((1+(tasaDesc/100))**numMes)))
                    elif numMes > 1:
                        VAN = int(VAN+(flujo/((1+(tasaDesc/100))**numMes)))
                    print(f"VAN: {VAN}")
                    numMes += 1
                    flujo = 0
                    if VAN > 0:
                        break

    elif opc_master == 8:
        """Escriba un programa en python que genere el codigo html necesario para mostrar
        un saludo introducido por el usuario y que el color de fondo de la página sea un
        color elegido al azar (El archivo de salida se llamara file-1.html)."""

        fraseSalida = input("Escriba un saludo para mostrar en la pantalla: ")
        colorFrase = randint(100, 500)
        f = open('file-1.html', 'w')

        mensaje = f"""<!DOCTYPE html>
        <html lang="es">
        <head>
        <meta charset="utf-8">
        <title> Salida File – 1 </title>
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        </head>
        <body style="background-color: hsl({colorFrase}, 100%, 50%)">
        <p>{fraseSalida}</p>
        </body>
        </html>"""

        f.write(mensaje)
        f.close()

        webbrowser.open_new_tab('file-1.html')

    elif opc_master == 9:
        """Mejore el programa anterior de manera que el saludo se muestre con un tipo de
        letra elegido al azar entre las cuatro familias serif, sans-serif, monospace y cursive
        y el tamaño también elegido al azar entre 200% y 800% (con valores múltiplos de
        100). (El archivo de salida se llamara file-2.html)."""

        fontFamily = ["serif", "san-serif", "monospace", "cursive"]
        indexFamily = randint(0, 3)
        tamaFrase2 = randint(200, 800)
        colorFrase = randint(100, 500)
        fraseSalida2 = input("Escriba un saludo para mostrar en pantalla. ")
        archivo = open('file-2.html', 'w')
        mensaje2 = f"""<!DOCTYPE html
        <html lang="es">
        <head>
        <meta charset="utf-8">
        <title> Sálida File - 2 </title>
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        </head>
        <body style="background-color: hsl({colorFrase}, 100%, 50%)">
        <p style="font-family: {fontFamily[indexFamily]}; font-size: {tamaFrase2}%">{fraseSalida2}</p>
        </body>
        </html>"""

        archivo.write(mensaje2)
        archivo.close()

        webbrowser.open_new_tab("file-2.html")

    elif opc_master == 10:

        """Mejore el programa anterior haciendo que el programa genere dos ficheros: la
        página web (file-3.html) y la hoja de estilo (style-1.css)."""

        font_family3 = ["serif", "san-serif", "monospace", "cursive"]
        indexFamily3 = randint(0, 3)
        tamanioFrase3 = randint(200, 800)
        colorFrase3 = randint(100, 500)

        fraseSalida3 = input("Escriba un saludo para mostrar en pantalla: ")
        archivoHTML = open("file-3.html", "w")
        archivoCSS = open("style-1.css", "w")

        datosHTML = f"""<!DOCTYPE html>
        <html lang="es">
        <head>
        <meta charset="utf-8">
        <title> Sálida File – 3 </title>
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <link rel="stylesheet" href=" style-1.css">
        </head>
        <body>
        <p>{fraseSalida3}</p>
        </body>
        </html>
        """

        datosCSS = """body {
        background-color: hsl("""+str(colorFrase3)+""", 100%, 50%);
        }
        p {
        font-family:"""+str(font_family3[indexFamily3])+""";
        font-size:""" + str(tamanioFrase3)+"""%;
        }"""

        archivoHTML.write(datosHTML)
        archivoCSS.write(datosCSS)

        archivoHTML.close()
        archivoCSS.close()

        webbrowser.open_new_tab("file-3.html")

    sleep(3)
