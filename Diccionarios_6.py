## Diccionario de Divisas
monedas = {'Dolar': '$', 'Euro': '€', 'Yen': '¥'}
moneda = input("Introduce una divisa: ")
if moneda.title() in monedas:
    print(monedas[moneda.title()])
else:
    print("La divisa no está.")

## Usuario responde por datos personales
nombre = input("¿Cuál es tu nombre?: ")
edad = input("¿Qué edad tienes?: ")
dirección = input("¿Cuál es tu dirección?: ")
teléfono = input("Cuál es tu número telefónico?: ")
persona = {'nombre': nombre, 'edad': edad, 'dirección': dirección, 'teléfono': teléfono}
print(persona['nombre'], 'tiene', persona['edad'], 'años, vive en', persona['dirección'], 'y su número de teléfono es', persona['teléfono'])

## Valor de la fruta en una Tabla
frutas = {'Plátano':1.35, 'Manzana':0.8, 'Pera':0.85, 'Naranja':0.7}
fruta = input("¿Qué fruta llevas?: ").title()
kg = float(input('¿Cuántos kilos? '))
if fruta in frutas:
    print(kg, 'kilos de', fruta, 'valen', frutas[fruta]*kg, '€')
else:
    print("Lo siento, la fruta", fruta, "no está disponible.")

## Pregunta por fecha en formato dd/mm/aaaa
meses = {1:'enero', 2:'febrero', 3:'marzo', 4:'abril', 5:'mayo', 6:'junio', 7:'julio', 8:'agosto', 9:'septiembre', 10:'octubre', 11:'noviembre', 12:'diciembre'}
fecha = input('Introduce una fecha en formato dd/mm/aaaa: ')
fecha = fecha.split('/')
print(fecha[0], 'de', meses[int(fecha[1])], 'de', fecha[2])

## Cŕeditos por Asignaturas
curso = {'Matemáticas': 6, 'Física': 4, 'Química': 5}
total_créditos = 0
for asignatura, créditos in curso.items():
    print(asignatura, 'tiene', créditos, 'créditos')
    total_créditos += créditos
print("Número total de créditos del curso: ", total_créditos)

## Diccionario Vacío se va llenando por el usuario
persona = {}
continuar = True
while continuar:
    clave = input('¿Qué dato quieres introducir? ')
    valor = input(clave + ': ')
    persona[clave] = valor
    print(persona)
    continuar = input('¿Quieres añadir más información (Si/No)? ') == "Si"

## Cesta de compra. Artículo y Precio.
cesta = {}
continuar = True
while continuar:
    item = input('Introduce un artículo: ')
    precio = float(input('Introduce el precio de ' + item + ': '))
    cesta[item] = precio
    continuar = input('¿Quieres añadir más artículos a la cesta (Si/No)? ') == "Si"
coste = 0
print('Lista de la compra')
for item, precio in cesta.items():
    print(item, '\t', precio)
    coste += precio
print('Coste total: ', coste)

## Diccionario de traducción español/inglés
diccionario = {}
palabras = input("Introduce la lista de palabras y traducciones en formato palabra:traducción separadas por comas: ")
for i in palabras.split(','):
    clave, valor = i.split(':')
    diccionario[clave] = valor
frase = input('Introduce una frase en español: ')
for i in frase.split():
    if i in diccionario:
        print(diccionario[i], end =' ')
    else:
        print(i, end=' ')
    
## Gestión de facturas pendientes de cobro.
facturas = {}
cobrado = 0
pendiente = 0
more = ''
while more != 'T':
    if more != 'A':
        clave = input('Introduce el número de la factura: ')
        coste = float(input('Introduce el coste de la factura: '))
        facturas[clave] = coste
        pendiente += coste
    if more == 'P':
        clave = input('Introduce el coste de la factura: ')
        coste = facturas.pop(clave, 0)
        cobrado +=coste
        pendiente -= coste
    print('Recaudado', cobrado)
    print('Pendiente de cobro: ', pendiente)
    more = input('¿Quieres añadir una nueva factura (A), pagarla (P), o terminar (T)? ')

## Gestionar Base de Datos de clientes de una Empresa.
clientes = {}
opción = ''
while opción != '6':
    if opción == '1':
        nif = input('Introduce NIF del cliente: ')
        nombre = input('Introduce el nomber del cliente: ')
        dirección = input('Introduce la dirección del cliente: ')
        teléfono = input('Introduce el teléfono del cliente: ')
        email = input('Introduce el email del cliente: ')
        vip = input('¿Es un cliente preferente (S/N)? ')
        cliente = {'nombre':nombre, 'dirección':dirección, 'email': email, 'preferente':vip=='S'}
        clientes[nif] = cliente
    if opción == '2':
        nif = input('Introduce NIF del cliente: ')
        if nif in clientes:
            del clientes[nif]
        else:
            print('No existe el cliente con el nif', nif)
    if opción == '3':
        nif = input('Introduce NIF del cliente: ')
        if nif in clientes:
            print('NIF:', nif)
            for clave, valor in clientes[nif].items():
        else:
            print('No existe el cliente con el nif', nif)
    if opción == '4':
        print('Lista de clientes')
        for clave, valor in clientes.items():
            print(clave, valor['nombre'])
    if opción == '5':
        print('Lista de clientes preferentes')
        for clave, valor in clientes.items():
            if valor['preferente']:
                print(clave, valor['nombre'])
    opción = input('Menú de opciones\n(1) Añadir cliente\n(2) Eliminar cliente\n(3) Mostrar cliente\n(4) Listar clientes\n(5) Listar clientes preferentes\n(6) Terminar\nElige una opción:')

## Directorio de Empresa en cadena
datos_clientes = "nif;nombre;email;teléfono;descuento\01234567L; Luis González;luisgonzalez@mail.com;656343576;12.5\n71476342J;Macarena Ramírez;macarena@mail.com;692839321;8\n63823376M;Juan José Martínez;juanjo@mail.com;664888233;5.2\n98376547F;Carmen Sánchez;carmen@mail.com;667677855;15.7"
#Dividimos la cadena por el carácter de cambio de linea \n y creamos una lista con las subcadenas.
lista_clientes = datos_clientes.split('\n')
#Inicializamos el diccionario que va a contener el directorio de clientes a vacío.
directorio = {}
#Dividimos la cadena del primer elemento de la lista de clientes(que contienen los
# nombres de los campos) por el carácter ; y creamos una lista con los cambios.
lista_campos = lista_clientes[0].split(';')
#Bucle iterativo para recorrer los elementos de la lista lista_clientes.
# la variable cliente recorre desde el segundo elemento hasta el último elemento de la lista
#(el primer elemento contiene los nombres de campo asi que no corresponde a un cliente)
for i in lista_clientes[1:]:
    # Inicializamos el diccionario que va a contener los datos del cliente actual a vacío.
    cliente = {}
    # Dividimos la cadena i por el carácter ; y creamos una lista con las subcadenas con la
    # información del cliente.
    lista_info = i.split(';')
    # Bucle iterativo para recorrer los campos y añadir los pares al diccionario del cliente.
    # j toma valores de 1 al número de campos menos 1. El primer elemento (posición 0) corresponde
    # al nif y no se añade al diccionario porque se utilizará después como clave en el diccionario
    # principal.
    for j in range (1,len(lista_campos)):
        # Condicional. Si el campo actual es descuento convertimos su valor en real
        if lista_campos[j] == 'descuento':
            lista_info[j] = float(lista_info[j])
        cliente[lista_campos[j]] = lista_info[j]
    # Añadimos un par al diccionario del directorio con la clave el nif del cliente y valor
    # el diccionario que acabamos de crear con el resto de sus datos.
    directorio[lista_info[0]] = cliente
# Mostramos el diccionario por pantalla
print(directorio)