#Entrada de datos

calificacion1= float(input("Digite el valor de la calificacion del 1er departamental:"))
calificacion2= float(input("Digite el valor de la calificacion del 2do departamental:"))
calificacion3=  float(input("Digite el valor de la calificacion del 3er departamental:"))

#PROCESOS(calculos, operaciones)

promedio= (calificacion1 + calificacion2 + calificacion3 ) / 3

#SALIDA DE DATOS 

print ("Tu promedio es igual a=", promedio)

if promedio < 6:
        print ("usted a reprobado")
else:
        print ("Felicidades usted a aprovado")
