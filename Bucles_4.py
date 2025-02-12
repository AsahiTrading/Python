## Palabra x 10 veces
word = input("Introduce una palabra: ")
for i in range(10):
    print(word)

## Edad
age = int(input("¿Que edad tienes?: "))
for i in range(age):
    print("Has cumplido " + str(i+1) + " años")

## Números impares
number = int(input("Introduce un número entero positivo: "))
for i in range(1, number+1, 2):
    print(i, end=", ")

## Números consecutivos hasta 0
number = int(input("Introduce un número entero positivo: "))
for i in range(number, -1, -1):
    print(i, end=", ")

## Inversión
amount = float(input("¿Cuánto va a invertir?: "))
interest = float(input("¿Interés porcentual anual?: "))
years = int(input("¿Cuantos años?: "))
for i in range(years):
    amount *= 1 + interest / 100
    print("Capital tras " + str(i+1) + " años: " + str(round(amount, 2)))

## Triangulo rectangulo (I)
high = int(input("ALtura del triángulo (entero positivo): "))
for i in range(high):
    for j in range(i+1):
        print("*", end="")
    print("")
#Triangulo rectángulo (II)
high = int(input("Introduce la altura del triángulo (entero positivo): "))
for i in range(high):
    print("*"*(i+1))

## Tabla de Multiplicar (10)
for i in range (1, 11):
    for j in range(1, 11):
        print(i*j, end="\t")
    print("")

## Triangulo rectángulo (Versión 2)
number = int(input("Introduce la altura del triángulo (entero positivo): "))
for i in range(1, number+1, 2):
    for j in range(i, 0, -2) :
        print(j, end=" ")
    print("")
# Debería darnos el siguiente triangulo:
# 1
# 3 1
# 5 3 1
# 7 5 3 1
# 9 7 5 3 1

## Contraseña
key = "contraseña"
password =""
while password != key:
    password = input("Introduce la contraseña: ")
print("Contraseña correcta")

## Número primo
n = int(input("Introduce un número entero positivo mayor que 2: "))
i = 2
}while n % i != 0:
    i += 1
if i == n:
    print(str(n) + " es primo")
else:
    print(str(n) + " no es primo")

## Deletreo desde el final
word = input("Introduce una palabra")
for i in range(len(word)-1, -1, -1):
    print(word[i])

frase = input("Introduce una frase: ")
letra = input("Introduce una letra: ")
contador = 0
for i in frase:
    if i == letra:
        contador += 1
print("La letra '%s' aparece %2i veces en la frase '%s?'." % (letra, contador, frase))

while True:
    frase = input("Introduce algo: ")
    if frase == "salir":
        break
    print(frase)