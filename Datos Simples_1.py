## Hola Mundo
print("¡Hola Mundo!")

## Saludo
saludo = ("¡Hola Mundo!")
print(saludo)

nombre = input("¿Cual es tu nombre: ")
print("¡Hola", nombre,"!")

## Operación Aritmética
x = ((3 + 2)/(2 * 5)) ** 2
print(x)

## Horas Trabajadas
valor_hora = int(100)
horas_pago = int(input("¿Cuántas horas trabajaste hoy?: "))
print(valor_hora * int(horas_pago))

## Entero Positivo
n = int(input("Introduce un número entero: "))
for i in range(1, n + 1):
	print(sum(range(1, i + 1)))

## Indice Masa Corporal (IMC)
peso = float(input("¿Cuál es su Peso en kilogramos?: "))
estatura = float(input("¿Cuál es su estatura en metros?: "))
imc = peso / estatura ** 2
print(imc)

## Dos Enteros
num_uno = input("Ingrese un número: ")
num_dos = input("Ingrese un número: ")
print(num_uno + " entre " + num_dos + " da un cociente " + str(int(num_uno) // int(num_dos)) + " y un resto " + str(int(num_uno) % int(num_dos)))

## Inversión
inversión = float(input("¿Con qué monto esta invirtiendo: "))
interes = float(input("Interés Porcentual anual: "))
años = int(input("¿Años de inversión: "))
print("Capital final: " + str(round(inversión * (interes/100 + 1) ** años, 2)))

## Juguetería
peso_payasos = 112
peso_muñecas = 75
pedido_uno = int(input("¿Cuántos payasos llevas?: "))
pedido_dos = int(input("¿Cuántas muñecas llevas?: "))
print(("El peso para tu envío es: "), (pedido_uno * peso_payasos) + (pedido_dos * peso_muñecas))

## Cuenta de ahorro
cta_cte = 5000.00
interes_anual = 0.04
print("Tu ahorro es: ", cta_cte)
print("Tu ganancia en este año es ", (cta_cte * interes_anual) + cta_cte)
print("Tu ganancia en este segundo año es ", (cta_cte * interes_anual * 2) + cta_cte)
print("Tu ganancia en este tercer año es ", (cta_cte * interes_anual * 3) + cta_cte)

## Ventas Panadería
barras = int(input("Número de barras vendidas que no son frescas?: "))
precio = 3.49
descuento = 0.6
coste = barras * precio * (1 - descuento)
print("El coste de una barra fresca es " + str(precio) + " €")
print("El descuento sobre una barra no fresca es " + str(descuento * 100) + "%")
print("El coste final a pagar es " + str(round(coste, 2)) + " €")