## ejercicio 1
name = str(input("¿Cuál es tu nombre?: "))
num = int(input("¿Dígame un numero entero: "))
print(name * num)

## ejercicio 2
name = str(input("¿Cuál es su nombre completo? "))
print(name.upper() * 3)
print(name.lower() * 3)
print(name)

## ejercicio 3
name = str(input("¿Cuál es su nombre? "))
print(name.upper() + " tiene " + str(len(name)) + " letras")

## ejercicio 4
tel = input("Introduce un número de teléfono con el formato +xx-xxxxxxx-xx: ")
print("El número de teléfono es: ", tel[3:-2])

## ejercicio 5 Frase al revés
phrase = input("Dime una frase: ")
print(phrase[::-1])

## ejercicio 6
phrase = input("Dime una frase: ")
vocal = input("Dime una vocal en minúscula: ")
print(phrase.replace(vocal, vocal.upper()))

## ejercicio 7
email = input("Dime tu correo electrónico: ")
print(email[:email.find("@")] + "@ceu.es")

## ejercicio 8
precio = float(input("Precio del producto: "))
print(precio, "€")

## ejercicio 9
fecha = ("Ingrese su fecha de nacimiento en el formato dd/mm/aaaa: ")
print("Día", fecha[:2])
print("Mes", fecha[3:5])
print("Año", fecha[6:])

fecha = input("Introduce la fecha de tu nacimiento en formato día/mes/año: ")
dia = fecha[:fecha.find("/")]
mesaño = fecha[fecha.find("/")+1:]
mes = mesaño[:mesaño.find("/")]
año = mesaño[mesaño.find("/")+1:]
print("Día", dia)
print("Mes", mes)
print("Año", año)

## ejercicio 10
compra = input("Introduzca los productos que lleva separados por comas: ")
print(compra.replace(",", "\n"))

## ejercicio 11
producto = input("Nombre del producto: ")
precio = float(input("Precio unitario: "))
unidades = int(input("Número de unidades: "))
print("{producto}: {unidades:3d} unidades x {precio:9.2f}€ = {total:11.2f}€".format(producto = producto, unidades = unidades, precio = precio, total = unidades * precio))