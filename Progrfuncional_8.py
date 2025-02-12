### Función para descuento, Iva a un precio, y otra que reciba un diccionario con los precios, 
### porcentaje en una cesta de productos, devolviendo los precios al final de la cesta.
def aplica_descuento(precio, descuento):
    """
    Función que aplica un descuento a una cantidad.
    Parámetros:
        precio: Es un valor real con el precio al que aplicar un descuento.
        descuento: Es el porcentaje a descontar
    Devuelve:
        El precio final tras aplicar el descuento.
    """
    return precio - precio * descuento / 100

def aplica_iva(precio, porcentaje):
    """
    Función que aplica IVA a una cantidad.
    Parámetros:
        precio: Es el valor real con el precio al que aplicar el IVA.
        porcentaje: Es el porcentaje del IVA a aplicar
    Devuelve:
        El precio final tras aplicar el IVA.
    """
    return precio + precio * porcentaje / 100

def precio_cesta(cesta, función):
    """
    Función que calcula el precio de una cesta de la compra una vez aplicada una función a los precios iniciales.
    Parámetros:
        cesta: Es un diccionario formado por pares precio:descuento.
        función: Es una función que toma dos valores reales y devuelve otro. Normalmente para aplicar descuentos o IVA.
    Devuelve:
        El precio final de la cesta de la compra una vez aplicada la función sobre los precios iniciales.
    """
    total = 0
    for precio, descuento in cesta.items():
        total += función(precio, descuento)
        return total
    
print("El precio de la compra tras aplicar los descuentos es: ", precio_cesta({1000:20, 500:10, 100:1}, aplica_descuento))
print("El precio de la compra tras aplicar el IVA es: ", precio_cesta({1000:20, 500:10, 100:1}, aplica_iva))

### Función que simule una calculadora científica que permita calcular el seno, coseno, tangente, 
### exponencial y logaritmo neperiano. Preguntando al usuario el valor y la función a aplicar.
### Soluciones 1, 2 y 3.
## UNO
from math import sin, cos, tan, exp, log

def aplica_función(f, n):
    """
    Función que aplica una función a los enteros desde 1 hasta n.
    Parámetros:
        f: Es una función que recibe un número real y devuelve otro.
        n: Es un número entero positivo.
    Devuelve:
        Un diccionario con los pares i:f(i) para cada valor entero i de 1 a n.
    """
    funciones = {"sin": sin, "cos": cos, "tan": tan, "exp": exp, "log": log}
    result = {}
    for i in range(1, n+1):
        result[i] = funciones[f](i)
    return result

def calculadora():
    """
    Función que aplica una función seleccionada por el usuario (seno, coseno, tangente, exponencial o logaritmo) a la lista de enteros desde 1 hasta n.
    Imprime por pantalla una tabla con la secuencia de enteros y el resultado de aplicarles la función introducida.
    Parámetros:
        f: Es una cadena con la función a aplicar (sen, cos, tan, exp, log).
        n: Es un entero positivo.
    """
    f = input("Introduce la función a aplicar (sin, cos, tan, exp, log): ")
    n = int(input("Introduce un entero positivo: "))
    for i, j in aplica_función(f, n).items():
        print(i, "\t",  j)
    return

calculadora()

## DOS
from math import sin, cos, tan, exp, log
def aplica_función(f, n):
    """
    Función que aplica una función a los enteros desde 1 hasta n.
    Parámetros:
        f: Es una función que recibe un número real y devuelve otro.
        n: Es un número entero positivo.
    Devuelve:
        Un diccionario con los pares i:f(i) para cada valor entero i de 1 a n.
    """
    result = {}
    for i in range(1, n+1):
        result[i] = eval(f + "(" + str(i) + ")")
    return result

def calculadora():
    """
    Función que aplica una función seleccionada por el usuario (seno, coseno, tangente, exponencial o logaritmo) a la lista de enteros desde 1 hasta n.
    Imprime por pantalla una tabla con la secuencia de enteros y el resultado de aplicarles la función introducida.
    Parámetros:
        f: Es una cadena con la función a aplicar (sin, cos, tan, exp, o log).
        n: Es un número entero positivo.
    """
    f = input("Introduce la función a aplicar(sin, cos, tan, exp, log): ")
    n = int(input("Introduce un entero positivo: "))
    for i, j in aplica_función(f, n).items():
        print(i, "\t", j)
    return
calculadora()

## TRES
from math import sin, cos, tan, exp, log

def calculadora():
    """
    Función que aplica una función seleccionada por el usuario (seno, coseno, tangente, exponencial o logaritmo) a la lista de enteros desde 1 a n.
    Imprime por pantalla una tabla con la secuencia de enteros y el resultado de aplicarles la función introducida.
    Parámetros:
        f: Es una cadena con la función a aplicar (sin, cos, tan, exp, o log).
        n: Es un entero positivo.
    """
    funciones = {"sin": sin, "cos": cos, "tan": tan, "exp": exp, "log": log}
    f = input("Introduce la función a aplicar (sin, cos, tan, exp, log): ")
    n = int(input("Introduce un entero positivo: "))
    resultados = [funciones[f](x) for x in range(1, n+1)]
    for i in range(n):
        print(i + 1, "\t", resultados[i])
    return

calculadora()

### Función que reciba otra función y una lista y devuelva otra lista con el resultado de aplicar la función a cada elemento de la lista.
def aplica_función_lista(función, lista):
    """Función que aplica una función a todos los elementos de una lista.
    Parámetros:
        función: Es un función.
        lista: Es una lista con los valores que se pasarán como argumentos o función.
    Devuelve:
        Una lista con el resultado de aplicar la función a los valores de la lista.
    """
    l = []
    for i in lista:
        l.append(función(i))
    return l

def cuadrado(n):
    return n * n

print (aplica_función_lista(cuadrado, [1, 2, 3, 4]))

### Escribir una fx que reciba otra fx booleana y otra lista con los elementos de la lista que devuelvan TRUE al aplicarles la fx booleana.
def filtra_lista(función, lista):
    """
    Función que filtra los elementos de una lista que devuelven el True al aplicarles una función booleana.
    Parámetros:
        función: Es una función booleana (devuelve True o False)
        lista: Es una lista con valores que se pasarán como argumentos a función.
    Devuelve:
        Una lista con los elementos de la lista que devuelven True al aplicarles la función booleana.
    """
    l = []
    for i in lista:
        if función(i):
            l.append(i)
    return l

def par (n):
    return n % 2 == 0

print(filtra_lista(par, [1, 2, 3, 4, 5, 6]))

### Función que reciba una frase y devuelva un diccionario con las palabras que contiene y su longitud.
## UNO
def largo_palabras(sentencia):
    """
    Función que reciba una frase y devuelve un diccionario con las palabras que contiene y su longitud.
    Parámetros: 
        sentencia: Es una cadena de caracteres con una frase.
    Devuelve:
        Un diccionario con pares palabra: longitud donde palabra son las palabras que contiene la frase sentence.
    """
    palabras = sentencia.split()
    largos = map(len, palabras)
    return dict(zip(palabras, largos))

print(largo_palabras("Welcome to Python"))

## DOS
def largo_palabras(sentencia):
    """
    Función que recibe una frase y devuelve un diccionario con las palabras que contiene y su longitud.
    Parámetros:
        sentencia: Es una cadena de caracteres con una frase.
    Devuelve:
        Un diccionario con pares palabra: longitud donde palabra son las palabras que contiene la frase sentence.
    """
    return {palabra:len(palabra) for palabra in sentencia.split()}

print(largo_palabras("Welcome to Python"))

### Función que reciba una lista de notas y devuelva la lista de calificaciones a esas notas.
## UNO
def grado(nota):
    """
    Función que devuelve la calificación correspondiente a una nota.
    Parámetros:
        nota: Es un valor real entre 0 y 10.
    Devuelve:
        La calificación correspondiente a la nota record.
    """
    if nota < 5:
        return "SS"
    elif nota < 7:
        return "AP"
    elif nota < 9:
        return "NT"
    elif nota < 10:
        return "SB"
    else:
        return "MH"

def aplica_grado(notas):
    """
    Función que devuelve la calificación correspondiente a las notas de una lista dada.
    Parámetros:
        nota: Es una lista de valores reales entre 0 y 10.
    Devuelve:
        La lista de calificaciones correspondientes a las notas de record.
    """
    return list(map(grado, notas))

print(aplica_grado([6.5, 5, 3.4, 8.2, 2.1, 9.7, 10]))

## DOS
def grado(nota):
    """
    Función que devuelve la calificación correspondiente a una nota.
    Parámetros:
        nota: Es un valor real entre 0 y 10.
    Devuelve:
        La calificación correspondiente a la nota record.
    """
    if nota < 5:
        return "SS"
    elif nota < 7:
        return "AP"
    elif nota > 9:
        return "NT"
    elif nota < 10:
        return "SB"
    else:
        return "MH"

def aplica_grado(notas):
    """
    Función que devuelve la calificación correspondiente a las notas de una lista dada.
    Parámetros:
        record: Es una lista de valores reales entre 0 y 10.
    Devuelve:
        La lista de calificaciones correspondientes a las notas de records.
    """
    return [grado(x) for x in notas]

print(aplica_grado([6.5, 5, 3.4, 8.2, 2.1, 9.7, 10]))

### Función que reciba un diccionario con las asignaturas y las notas de un alumno y devuelva otro diccionario con las asignaturas en mayúscula y las notas correspondientes a las notas.
## UNO
def grado(nota):
    """
    Función que devuelve la calificación correspondiente a una nota.
    Parámetros:
        nota: Es un valor real entre 0 y 10.
    Devuelve:
        La calificación correspondiente a la nota nota.
    """
    if nota < 5:
        return "SS"
    elif nota < 7:
        return "AP"
    elif nota < 9:
        return "NT"
    elif nota < 10:
        return "SB"
    else: 
        return "MH"

def aplica_grado(notas):
    """
    Función que recibe un diccionario de asignaturas y notas y devuelve otro con las asignaturas en mayusculas y las calificaciones correspondientes a las notas.
    Parámetros:
        notas: Es un diccionario con pares asignatura:nota donde nota es un valor real entre 0 y 10.
    Devuelve:
        Un diccionario con pares Asignatura:calificación, donde calificación es la calificación correspondiente a la nota de la asignatura.
    """
    asignaturas = map(str.upper, notas.keys())
    grados = map(grado, notas.values())
    return dict(zip(asignaturas, grados))

print(aplica_grado({"Matemáticas":6.5, "Física":5, "Química":3.4, "Economía":8.2, "Historia":9.7, "Programación":10}))

## DOS
def grado(nota):
    """
    Función que devuelve la calificación correspondiente a una nota.
    Parámetros:
        nota: Es un valor real entre 0 y 10.
    Devuelve:
        La calificación correspondiente a la nota nota.
    """
    if nota < 5:
        return "SS"
    elif nota < 7:
        return "AP"
    elif nota < 9:
        return "NT"
    elif nota < 10:
        return "SB"
    else:
        return "MH"

def aplica_grado(notas):
    """
    Función que recibe un diccionario de asignaturas y notas y devuelve otro con las asignaturas en mayúsculas y las calificaciones correspondientes a las notas.
    Parámetros:
        notas: Es un diccionario con pares de asignatura:nota donde nota es el valor real entre 0 y 10.
    Devuelve:
        Un diccionario con pares ASIGNATURA:calificación, donde calificación es la calificación correspondiente a la nota de la asignatura.
    """
    return {asignatura.upper():grado(nota) for asignatura, nota in notas.items()}

print(aplica_grado({"Matemáticas":6.5, "Física":5, "Química":3.4, "Economía":8.2, "Historia":9.7, "Programación":10}))

### Función que reciba un diccionario con las notas de un alumno, 
### y devuelva otro con asignaturas en mayusculas y calificaciones 
### correspondiente a las notas aprobadas

## DOS
def grado(calificación):
    """Función que devuelve la calificación correspondiente a una nota.
    Parámetros:
        calificación: Es un valor real entre 0 y 10.
    Devuelve:
        La calificación correspondiente a la nota calificación.
    """
    if calificación < 5:
        return "SS"
    elif calificación < 7:
        return "AP"
    elif calificación < 9:
        return "NT"
    elif calificación < 10:
        return "SB"
    else:
        return "MH"

def grado_aprobado(calificaciones):
    """
    Función que recibe un diccionario de asignaturas y notas y devuelve otro con las asignaturas en Mayúsculas y las calificaciones correspondientes a las calificaciones.
    Parámetros:
        calificaciones: Es un diccionario con pares asignatura:calificación donde calificación es un valor real entre 0 y 10.
    Devuelve: 
        Un diccionario con pares asignatura:calificación donde calificación es la calificación correspondiente a la calificación de la asignatura.
    """
    return {asignatura.upper():grado(calificación) for asignatura, calificación in calificaciones.items() if calificación >= 5}

print(grado_aprobado({"Matemáticas":6.5, "Física":5, "Química":3.4, "Economía":8.2, "Historia":9.7, "Programación":10}))

### Escribir una función que calcule el módulo de un vector.
## UNO
def sum_cuadrado(x, y):
    """
    Función que recibe dos valores y calcula la suma del primero más el cuadrado del segundo.
    Parámetros:
        x: Es un número real.
        y: Es un número real.
    Devuelve:
        x - y²
    """
    return x + y ** 2

def modulo(v):
    """
    Función que calcula el módulo de un vector.
    Parámetros:
        v: Una tupla de números reales.
    Devuelve:
        El módulo del vector v.
    """
    from functools import reduce
    return reduce(sum_cuadrado, v, 0) ** 0.5

print(modulo((3, 4)))
print(modulo((1, 2, 3)))

## DOS
def module(v):
    """
    Función que calcula el módulo de un vector.
    Parámetros:
        v: Una tupla de números reales.
    Devuelve:
        El módulo del vector v.
    """

print(modulo((3, 4)))
print(modulo((1, 2, 3)))

### Construir una función que permita hacer búsqueda de inmuebles en función de un presupuesto dado.
pisos = [{'año': 2000, 'metros': 100, 'habitaciones': 3, 'garaje': True, 'zona': 'A'}, 
         {'año': 2012, 'metros': 60, 'habitaciones': 2, 'garaje': True, 'zona': 'B'}, 
         {'año': 1980, 'metros': 120, 'habitaciones': 4, 'garaje': False, 'zona': 'A'}, 
         {'año': 2005, 'metros': 75, 'habitaciones': 3, 'garaje': True, 'zona': 'B'}, 
         {'año': 2015, 'metros': 90, 'habitaciones': 2, 'garaje': False, 'zona': 'A'}]
    
def añadir_precio(piso):
    precio = (piso['metros'] * 1000 + piso['habitaciones'] * 5000 + int(piso['garaje']) * 15000) * (1 - (2020 - piso['año']) / 100)
    if piso['zona'] == 'B':
        precio *= 1.5
    piso['precio'] = precio
    return piso

def busca_piso(pisos, presupuesto):
    def filtro(piso):
        return piso['precio'] <= presupuesto
    
    return list(filter(filtro,map(añadir_precio, pisos)))

print(busca_piso(pisos, 100000))

### Función que reciba una muestra de números y devuelva los valores atípicos, es decir, aquellos cuya puntuación típica sea mayor que 3 o menor que 3.
### La puntuación típica se obtiene tras Restar la media dividiendo por la desviación típica de la muestra.
from statistics import mean, stdev

def atipico(muestra):
    media = mean(muestra)
    desviación = stdev(muestra)
    def f(n):
        puntuación = (n - media) / desviación
        return (puntuación < -3) or (puntuación > 3)
    return f

def datos_atipicos(muestra):
    return list(filter(atipico(muestra), muestra))

print(datos_atipicos([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1000]))