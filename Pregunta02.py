# Entrada
a=int(input("Ingrese el primer numero"))
b=int(input("Ingrese el segundo numero"))
c=int(input("Ingrese el tercer numero"))
d=int(input("Ingrese el cuarto numero"))
e=int(input("Ingrese el quinto numero"))

# Proceso

if a<b and a<c and a<d and a<e:
    arreglo= [b, c, d, e]

elif b<a and b<c and b<d and b<e:
    arreglo= [a, c, d, e]

elif c<a and c<b and c<d and c<e:
    arreglo= [a, b, d, e]

elif d<a and d<b and d<c and d<e:
    arreglo= [a, b, c, e]

elif e<a and e<b and e<c and e<d:
    arreglo= [a, b, c, d]

# Salida

print(arreglo)