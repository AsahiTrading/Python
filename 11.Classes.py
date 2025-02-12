### Classes ###

class MyEmptyPerson:
    pass

print(MyEmptyPerson)
print(MyEmptyPerson())

class Person:
    def __init__ (self, name, surname, alias = "Sin alias"):
        self.full_name = f"{name} {surname} ({alias})" # Propiedad Pública
        self.__name = name # Propiedad privada

    def get_name (self):
        return self.__name

    def walk(self):
        print(f"{self.full_name} está caminando")

my_person = Person("Rafael", "Mora")
print(my_person.full_name)
print(my_person.get_name())
my_person.walk()

my_other_person = Person("Rafael", "Mora", "Rafaelpartner")
print(my_other_person.full_name)
my_other_person.walk()
my_other_person.full_name = "Andres Cardenas (El de las hojas de Palma)"
print(my_other_person.full_name)

my_other_person.full_name = 666
print(my_other_person.full_name) 