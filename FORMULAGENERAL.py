#ENTRADA DE DATOS

a=float(input("Digita el valor de a:"))
b=float(input("Digita el valor de b:"))
c=float(input("Digita el valor de c:"))

#PROCESOS(Calculos u operaciones matematicas y logicas)

x1= ((- b - pow (pow(b, 2) - (4 *a *c), 1/2))) / (2 * a)
x2= ((- b + pow (pow(b, 2) - (4 *a *c), 1/2))) / (2 * a)

#RESULTADOS 

print("El valor de X1 es igual a:", x1)
print("El valor de X2 es igual a:", x2)

