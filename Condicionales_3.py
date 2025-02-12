## Condicional / Mayor de edad

edad = input("¿Que edad tienes:? ")
if int(edad) >= 18:
    print("Usted es mayor de edad")
else:
    print("Usted es menor de edad")

## Contraseñas
contraseña = "por el chico no hay guagua" 
password = input("Ingrese la contraseña correcta: ")
if contraseña == password.lower():
    print("Contraseña correcta")
else:
    print("Contraseña incorrecta")

## Dos números
number_one = float(input("Ingresa un número: "))
number_dos = float(input("Ingresa otro número: "))
if number_dos == 0:
    print("¡Error!, No se puede dividir por 0.")
else:
    print(number_one/number_dos)

## Par / Impar
number = int(input("Ingrese un número: "))
if number % 2 == 0:
    print("El número " + str(number) + " es par")
else:
    print("El número " + str(number) + " es impar")

## Orden Tributario
edad = int(input("¿Qué edad tienes?: "))
ingreso = float(input("¿Cuanto es tu ingreso mensual?: "))
tributo = edad + ingreso
if edad > 16 and ingreso >= 1000:
    print("Si tienes que tributar")
else:
    print("Usted debe reunir todos los requisitos para tributar")

## Alumnos de un Curso Mixto I
gender = input("¿Con qué sexo te defines (M o H)?: ")
name = str(input("¿Con qué letra comienza tu apellido: "))
if gender == "M":
    if name.lower() < "m":
        group = "A"
    else:
        group = "B"
else:
    if name.lower() > "n":
        group = "A"
    else:
        group = "B"
print("Tu grupo es " + group)
## Alumnos de un Curso Mixto II
name = input("¿Cómo te llamas?: ")
gender = input ("¿Cuál es tu sexo (H o M)?: ")
if (gender == "M" and name.lower() < "m") or (gender == "H" and name.lower() > "n"):
    group = "A"
else:
    group = "B"
print("Tu grupo es " + group)

## Programa de renta anual
renta = float(input("¿Cuál es su renta anual?: "))
# Condicional para determinar el tipo impositivo
if renta < 10000:
    tipo = 5
elif renta < 20000:
    tipo = 15
elif renta < 35000:
    tipo = 20
elif renta < 60000:
    tipo = 30
else:
    tipo = 45
# Mostrar por pantalla el producto de la renta por el tipo impositivo
print("Tienes que pagar ", renta * tipo / 100, " €", sep="")

## Evaluación de empleados
puntuación = float(input("¿Cuál es su evaluación final?: "))
if puntuación == 0.0:
    nivel = "Inaceptable"
elif puntuación == 0.4:
    nivel = "Aceptable"
elif puntuación >= 0.6:
    nivel = "Meritorio"
print("Tu evaluación es ", nivel)

## Salas de juego
edad = int(input("¿Qué edad tienes?: "))
if edad < 4:
    precio = 0
elif edad <= 18:
    precio = 4
else:
    precio = 10
print("El precio de la entrada es ", precio, "€.")

## Pizzería Bella Napoli
#Presentación del menú con los tipos de pizza
print("Bienvenido a la pizzería Bella Napoli.\nTipos de pizza\n\t1- vegetariana\n\t2- No vegetariana\n")
tipo = input("Introduce el número correspondiente al tipo de pizza que quieres: ")
#Decisión sobre el tipo de pizza
if tipo == "1":
    print("Ingredientes de pizzas vegetarianas\n\t 1-Pimiento\n\t2- Tofu\n")
    ingrediente = ("Introduce el ingrediente que deseas: ")
    print("Pizza vegetariana con mozzarella, tomate y ", end="")
    if ingrediente == "1":
        print("pimiento")
    else:
        print("tofu")
else
    print("Ingredientes de pizzas no vegetarianas\n\t1- Peperoni\n\t2- Jamón\n\t3- Salmón\n")
    ingrediente = input("Introduce el ingrediente que deseas: ")
    print("Pizza no vegetariana con mozzarella, tomate y ", end="")
    if ingrediente == "1":
        print("peperoni")
    elif ingrediente == "2":
        print("jamón")
    else:
        print("salmón")