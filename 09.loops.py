### Loops ###

# While

my_condition = 0

while my_condition < 10:
    print(my_condition)
    my_condition += 2
else: # Es opcional
    print("Mi condición es mayor o igual que 10")

print("La ejecución continúa")

while my_condition < 20:
    my_condition += 1
    if my_condition == 15:
        print("Se detiene la ejecución")
        break
    print(my_condition)

print("La ejecución continúa")

# For

my_list = [35, 24, 62, 52, 30, 30, 17]

for element in my_list:
    print(element)

my_tuple = (40, 1.82, "Rafael", "Mora", "Rafael")
for element in my_tuple:
    print(element)

my_set = {"Kotlin", "Swift", "Python"}
for element in my_set:
    print(element)

my_dict = {"Nombre": "Rafael", "Apellido": "Mora", "Edad":40, 1:"Python"}
for element in my_dict: # podemos llamar a "my_dict.values()"
    print(element)
    if element == "Edad":
        break
    print("Se ejecuta")
else:
    print("El bucle for para diccionario ha finalizado")

for element in my_dict:
    print(element)
    if element == "Edad":
        continue
    print("Se ejecuta")
else:
    print("El bucle for para diccionario ha finalizado")

print("La ejecución continúa")