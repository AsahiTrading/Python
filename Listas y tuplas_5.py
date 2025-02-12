## Asignaturas en una Lista
materias = ["Matemáticas", "Física", "Química", "Historia", "Lengua"]
print(materias)

## Asignaturas en lista muestra en pantalla
materias = ["Matemáticas", "Física", "Química", "Historia", "Lengua"]
for materia in materias:
    print("Yo estudio " + materia)

## Asignatura y Notas
materias = ["Matemáticas", "Física", "Química", "Historia", "Lengua"]
notas = []
for materia in materias:
    nota = input("¿Qué nota has sacado en " + materia + "? ")
    notas.append(nota)
for i in range(len(materias)):
    print("En " + materias[i] + " has sacado " + notas[i])

## Ganadores Lotería
ganador = []
for i in range(6):
    ganador.append(int(input("Introduce un número ganador: ")))
ganador.sort()
print("Los números ganadores son " + str(ganador))

## Números al revés I
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(", ".join(map(str, numbers[::-1])))
# Números al revés II
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
numbers.reverse()
for number in numbers:
    print(number, end=", ")

## Asignaturas aprobadas/reprobadas
materias = ["Matemáticas", "Física", "Química", "Historia", "Lengua"]
aprobadas = []
for materia in materias:
    nota = float(input("¿Qué nota has sacado en " + materia + "? "))
    if nota >= 5:
        aprobadas.append(materia)
for materia in aprobadas:
    materias.remove(materia)
print("Tienes que repetir" + str(materias))

## Alfabeto sin multiples de 3 I
alfabeto = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'ñ', 'o', 'p' , 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
for i in range(len(alfabeto), 1, -1):
    if i % 3 == 0:
        alfabeto.pop(i-1)
print(alfabeto)
# Alfabeto II
alfabeto = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'ñ', 'o', 'p' , 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
for i in range(len(alfabeto), 1, -1):
    if i % 3 == 0:
        alfabeto.pop(i-1)
print(alfabeto)

## Palabra palíndromo
palabra = input("Introduce una palabra: ")
reves_palabra = palabra
palabra = list(palabra)
reves_palabra = list(reves_palabra)
reves_palabra.reverse()
if palabra == reves_palabra:
    print("Es un palíndromo")
else:
    print("No es un palíndromo")

## Escribe una palabra repite vocal.
palabra = input("Introduce una palabra: ")
vocales = ['a', 'e', 'i', 'o', 'u']
for vocal in vocales:
    veces = 0
    for letra in palabra:
        if letra == vocal:
            veces += 1
    print("La vocal " + vocal + " aparece ", str(veces) + " veces")

## Orden de precios
precios = [50, 75, 46, 22, 80, 65, 8]
min = max = precios[0]
for precio in precios:
    if precio < min:
        min = precio
    elif precio > max:
        max = precio
print("El minimo es ", str(min))
print("El máximo es ", str(max))

## Vectores en dos listas
vector_uno = (1, 2, 3)
vector_dos = (-1, 0, 2)
producto = 0
for i in range(len(vector_uno)):
    producto += vector_uno[i]*vector_dos[i]
print("El producto de los vectores" + str(vector_uno) + " y " + str(vector_dos) + " es " + str(producto))

## Matrices
a = ((1, 2, 3),
     (4, 5, 6))
b = ((-1, 0),
     (0, 1),
     (1,1))
resultado = [[0,0],
             [0,0]]
for i in range(len(a)):
    for j in range(len(b[0])):
        for k in range(len(b)):
            resultado[i][j] += a[i][k] * b[k][j]
for i in range(len(resultado)):
    resultado[i] = tuple(resultado[i])
resultado = tuple(resultado)
for i in range(len(resultado)):
    print(resultado[i])

## Muestra de numeros separados por comas
ejemplo = input("Introduce una muestra de números separados por comas: ")
ejemplo = ejemplo.split(',')
n = len(ejemplo)
for i in range(n):
    ejemplo[i] = int(ejemplo[i])
ejemplo = tuple(ejemplo)
suma = 0
sumasq = 0
for i in ejemplo:
    suma += i
    sumasq += i**2
muestra = suma/n
desviacion = (sumasq/n-muestra**2)**(1/2)
print("La media es", muestra, ", y la desviación típica es", desviacion)