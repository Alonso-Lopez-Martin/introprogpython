#Array con rangos
for i in range(10):
    print("i=", i)

#Trabajamos con Arrays
print(f"Trabajamos con Arrays\n")
print ("lista array")
miLista=[3,4,-1,9]

#Sacamos elementos
print(f"Sacamos elementos\n")
print(miLista)
print(miLista[2])
print(miLista[-1]) #coge el último valor

#Añadimos elementos
print(f"Añadimos elementos\n")
miLista.append(7)
print(miLista)
miLista.append("Hola")
print(miLista)
miLista.pop()

#Copiamos lista
print(f"Copiamos lista\n")
import copy
otraLista = copy.deepcopy(miLista)

#Arrays mágicos
for item in miLista:
    print(item)

#Funciones
print("maximo", max(miLista))
print("suma", sum(miLista))

#Operadores y Booleanos
x = True
y = False
print(x and y)
print(x or y)

if x or y:
    print("verdad verdadera")
else:
    print("Mentira Cochina")

m = "mauricio"
print(m*7 + str(miLista))



