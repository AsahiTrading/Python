### Dictionaries ###

my_dict = dict()
my_other_dict = {}

print(type(my_dict))
print(type(my_other_dict))

my_other_dict = {"Nombre": "Rafael", "Apellido": "Mora", "Edad":40, 1:"Python"}

my_dict = {
    "Nombre": "Rafael",
    "Apellido":"Mora",
    "Edad":40,
    "Lenguajes": {"Python", "Swift", "Kotlin"},
    1:1.82
    }

print(my_other_dict)
print(my_dict)

print(len(my_other_dict))
print(len(my_dict))

print(my_dict["Nombre"])

my_dict["Nombre"] = "Pedro"
print(my_dict["Nombre"])

print(my_dict[1])

my_dict["Calle"] = "Calle 123"
print(my_dict)

del my_dict["Calle"]
print(my_dict)

print("Mora" in my_dict) #False
print("Apellido" in my_dict) #True
#print("Mori" in my_dict) #False

print(my_dict.items())
print(my_dict.keys())
print(my_dict.values())
print(my_dict.fromkeys("Nombre", 1))

my_list = ["Nombre", 1, "Piso"]

my_new_dict = dict.fromkeys(my_list)
print(my_new_dict)
#my_new_dict = dict.fromkeys("Nombre", 1, "Piso") # None # TypeError: fromkeys expected at most 2 arguments, got 3
#print(my_new_dict)
#my_new_dict =dict.fromkeys(my_dict) #
#print(my_new_dict)
#my_new_dict = dict.fromkeys(my_dict, "Rafaelpartner")
#print(my_new_dict)

my_values = my_new_dict.values()
print(type(my_values))

print(my_new_dict.values())
print(dict.fromkeys(list(my_new_dict.values())).keys())
print(tuple(my_new_dict))
print(set(my_new_dict))