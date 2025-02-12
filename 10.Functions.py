### Functions ###

def my_function():
    print("Esto es una función")

my_function()
my_function()
my_function()

# Función con parámetros de entrada/argumentos

def sum_two_values (first_value: int, second_value):
    print(first_value + second_value)

sum_two_values(5, 7)
sum_two_values(58734, 7983724)
sum_two_values("5", "7")
sum_two_values(1.4, 5.2)

# Función con parámetros de entrada/argumentos y retorno

def sum_two_values_with_return (first_value, second_value):
    my_sum = first_value + second_value
    return my_sum

my_result = sum_two_values(1.4, 5.2)
print(my_result)

my_result = sum_two_values_with_return(10, 5)
print(my_result)

def print_name (name, surname):
    print(f"{name} {surname}")

print_name(surname = "Mora", name = "Rafael")

def print_name_with_default (name, surname, alias = "Sin alias"):
    print(f"{name} {surname} {alias}")

print_name_with_default("Rafael", "Mora") # sin alias
print_name_with_default("Rafael", "Mora", "Rafaelpartner") # con alias

#def print_texts(*text):
#    print(text)

def print_upper_texts(*texts):
    print(type(texts))
    for text in texts:
        print(text.upper())

print_upper_texts("Hola", "Python", "Rafaelpartner") #Con el asterisco en text, asegura que puedo pasarle cualquier cantidad de argumentos 
print_upper_texts("Hola")