import math
#ENTRADA DE DATOS

a=float(input("Digita el valor de a:"))
b=float(input("Digita el valor de b:"))
c=float(input("Digita el valor de c:"))

#PROCESOS(Calculos u operaciones matematicas y logicas)

x1= ((- b - math.sqrt(pow(b, 2) - (4 *a *c), ))) / (2 * a)
x2= ((- b + math.sqrt(pow(b, 2) - (4 *a *c),))) / (2 * a)

#RESULTADOS 

print(f"El valor de x1 es igual a = {x1}")
print(f"El valor de x2 es igual a = {x2}")
