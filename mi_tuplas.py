print("ejemplo de tuplas")
canciones=("te amo", "el noa noa ", "amor eterno ")
print(canciones)
y=list(canciones)
print(y)
y[1]= "la puerta negra"
x=tuple(y)
print(x)
print("Listado de elementos de tupla con ciclo for")
for sosa in canciones:
   print(sosa)
   