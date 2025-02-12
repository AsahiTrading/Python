def saludo():
    """Función que muestra el saludo ¡Hola amiga! por pantalla."""
    print('¡Hola amiga!')
    return
    
saludo()

## Función que muestra un saludo por pantalla
def saludo(nombre):
    """Definición que muestra un saludo por pantalla.
    Parámetros
    nombre: Nombre del Usuario
    Devuelve el saludo ¡Hola nombre!.
    """
    print("¡Hola " + nombre + "!")
    return

saludo("Alf")
saludo("Python")

## Función que reciba un numero y devuelva su factorial
def factorial(n):
    """Función que calcula el factorial de un numero entero positivo.
    Parámetros
    n: Es un entero positivo.
    Devuelve el factorial de n.
    """
    tmp = 1
    for i in range(n):
        tmp *= i+1
    return tmp

print(factorial(4))
print(factorial(20))

## Función que calcula el total de una factura aplicando el IVA.
def factura(monto, iva=21):
    """Función que aplica el IVA a una factura.
    Parámetros
    monto: Es la cantidad sin IVA
    iva: Es el porcentaje de IVA
    Devuelve el total de la factura una vez aplicado el IVA.
    """
    return monto + monto*iva/100

print(factura(1000, 10))
print(factura(1000))

## Función que calcula el área de un círculo y otra el volumen de un cilindro usando la primera función.
def area_circulo(radio):
    """Función que calcula el área de un círculo.
    Parámetros
    radio: Es el radio del círculo.
    Devuelve el área del círculo de radio radio.
    """
    pi = 3.1415
    return pi*radio**2

def volumen_cilindro(radio, alto):
    """Función que calcula el volúmen de un cilindro.
    Parámetros
    radio: Es el radio de la base del cilindro.
    alto: Es la altura del cilindro.
    Devuelve el volúmen del cilindro de radio radio y altura alto.
    """
    return area_circulo(radio)*alto

print(volumen_cilindro(3,5))

## Función que reciba una muestra de números en una lista y devuelva su media.
def muestra(ejemplo):
    """Función que calcula la media de una muestra de números
    Parámetros
    ejemplo: Es una lista de números
    Devuelve la media de los números en ejemplo.
    """
    return sum(ejemplo)/len(ejemplo)

print(muestra([1, 2, 3, 4, 5]))
print(muestra([2.3, 5.7, 6.8, 9.7, 12.1, 15.6]))

## Función que reciba una muestra de numeros en una lista y devuelva otra lista con sus cuadrados.
def cuadrado(ejemplo):
    """Función que calcula los cuadrados de una lista de números.
    Parámetros
    ejemplo: Es una lista de números
    Devuelve una lista con los cuadrados de los números de la lista ejemplo.
    """
    list = []
    for i in ejemplo:
        list.append(i**2)
    return list

print(cuadrado([1, 2, 3, 4, 5]))
print(cuadrado([2.3, 5.7, 6.8, 9.7, 12.1, 15.6]))

## Función que reciba una muestra de numeros en una lista y devualva un diccionario con su media, varianza y desviación típica.
def cuadrado(ejemplo):
    """Función que calcula los cuadrados de una lista de números
    Parámetros
    ejemplo: Es una lista de números
    Devuelve una lista con los cuadrados de los números de la lista ejemplo.
    """
    list = []
    for i in ejemplo:
        list.append(i**2)
    return list

def estadística(ejemplo):
    """Función que calcula la media, varianza, y desvición tipica de una muestra de números.
    Parámetros
    ejemplo: Es una lista de números
    Devuelve un diccionario con la media, varianza, y desviación típica de los números en ejemplo.
    """
    estadística = {}
    estadística["media"] = sum(ejemplo)/len(ejemplo)
    estadística["varianza"] = sum(cuadrado(ejemplo))/len(ejemplo)-estadística["media"]**2
    estadística["desviación tipica"] = estadística["varianza"]**0.5
    return estadística

print(estadística([1, 2, 3, 4, 5]))
print(estadística([2.3, 5.7, 6.8, 9.7, 12.1, 15.6]))

## Función que calcule el maximo común divisor de dos numeros y otra que calcule el mínimo común múltiplo.
def mcd(n, m):
    """Función que calcula el máximo común divisor de dos números.
    Parámetros:
        n: Es un número entero
        m: Es un número entero
    Devuelve:
        El máximo común divisor de n y m
        """
    rest = 0
    while(m > 0):
        rest = m
        m = n % m
        n = rest
    return n

def mcm(n, m):
    """Función que calcula el mínimo común múltiplo de dos números.
    Parámetros:
        n: Es un número entero.
        m: Es un número entero.
    Devuelve:
        El mínimo común múltiplo de n y m.
        """
    if n > m:
        mayor = n
    else:
        mayor = m
    while (mayor % n != 0) or (mayor % m !=0):
        mayor += 1
    return mayor

print(mcd(24,36))
print(mcm(24,36))

## Función que convierta un número decimal en binario, y otra al revés.
def a_decimal(n):
    """Función que convierte un número binario en decimal.
    Parámetros:
        - n: Es una cadena de ceros y unos.
    Devuelve:
        El número decimal correspondiente a n.
    """
    n = list(n)
    n.reverse()
    decimal = 0
    for i in range(len(n)):
        decimal += int(n[i]) * 2 ** i
    return decimal

def a_binario(n):
    """Función que convierte un número decimal en binario.
    Parámetros:
        n: Es un número entero.
    Devuelve:
        El número binario correspondiente a n.
    """
    binario = []
    while n > 0:
        binario.append(str(n % 2))
        n //= 2
    binario.reverse()
    return ''.join(binario)

print(a_decimal("10110"))
print(a_binario(22))
print(a_decimal(a_binario(22)))
print(a_binario(a_decimal("10110")))

## Función que reciba una cadena de caracteres y devuelva un diccionario con cada palabra que contiene y su frecuencia.
## Otra que recibe el diccionario generado de la función anterior y devuelva un tupla con la palabra más repetida y su frecuencia.
def cuenta_palabras(texto):
    """Función que cuenta el número de veces que aparece cada palabra en un texto.
    Parámetros:
        - texto: Es una cadena de caracteres.
    Devuelve:
        Un diccionario con pares palabra: frecuencia con las palabras contenidas en el texto y su frecuencia.
    """
    texto = texto.split()
    palabras = {}
    for i in texto:
        if i in palabras:
            palabras[i] += 1
        else:
            palabras[i] = 1
    return palabras

def mas_repetida(palabras):
    max_palabra = ""
    max_frecuencia = 0
    for palabra, frecuencia in palabras.items():
        if frecuencia > max_frecuencia:
            max_palabra = palabra
            max_frecuencia = frecuencia
    return max_palabra, max_frecuencia

texto = "Como quieres que te quiera si el que quiero que me quiera no me quiere como quiero que me quiera"
print(cuenta_palabras(texto))
print(mas_repetida(cuenta_palabras(texto)))