### Tuples ###

my_tuple = tuple()
my_other_tuple = ()

my_tuple = (40, 1.82, "Rafael", "Mora", "Rafael")
my_other_tuple = (35, 60, 30)

print(my_tuple)
print(type(my_tuple))

print(my_tuple[0])
print(my_tuple[-1])
#print(my_tuple[4]) IndexError
#print(my_tuple[-6]) IndexError

print(my_tuple.count("Rafael"))
print(my_tuple.index("Mora"))
print(my_tuple.index("Rafael"))

#my_tuple[1] = 1.90 'tuple' object does not support item assignment

my_sum_tuple = my_tuple + my_other_tuple
print(my_sum_tuple)

print(my_sum_tuple[3:6])

my_tuple = list(my_tuple)
print(type(my_tuple))

my_tuple[4] = "Rafaelpartner"
my_tuple.insert(1, "Azul")
my_tuple = tuple(my_tuple)
print(my_tuple)
print(type(my_tuple))

#del my_tuple[2] TypeError: 'tuple' object doesn't support item deletion

del my_tuple
#print(my_tuple) NameError: name "my_tuple" is not defined
