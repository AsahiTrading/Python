# Uno
contraseña = input("Introduce la contraseña: ")
if contraseña in ["sesamo"]:
    print("Pasa")
else:
    print("No pasa")

# Dos
base = float(input("Introduce la base imponible de la factura: "))

def aplica_iva(base, iva = 21):
      base += base * iva / 100
      return base

print(aplica_iva(base))

# Tres
u = [1, 2, 3]
v = [4, 5, 6]

def producto_escalar(u, v):
    for i in range(len(u)):
        u[i] *= v[i]
    return sum(u)
print(producto_escalar(u, v))

# Cuatro
listin = {"Juan":123456789, "Pedro":987654321}

def elimina(listin, usuario):
    return listin.pop(usuario, "")

print(elimina(listin, "Pedro"))

# Cinco
a = ((1, 2, 3),
     (3, 2, 1))
b = ((1, 2),
     (3, 4),
     (5, 6))

def producto(a, b):
    producto = []
    for i in range(len(a)):
        fila = []
        for j in range(len(b[0])):
            suma = 0
            for k in range(len(a[0])):
                suma += a[i][k] * b[k][j]
            fila.append(suma)
        producto.append(tuple(fila))
    return tuple(producto)

print(producto(a, b))