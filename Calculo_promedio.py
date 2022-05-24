#Entrada de datos

calificacion1= float(input("Digite el valor de la calificacion del 1er departamental:"))
calificacion2= float(input("Digite el valor de la calificacion del 2do departamental:"))
calificacion3=  float(input("Digite el valor de la calificacion del 3er departamental:"))

#PROCESOS(calculos, operaciones)

promedio= (calificacion1 + calificacion2 + calificacion3 ) / 3

#SALIDA DE DATOS 

print ("Tu promedio es igual a=", promedio)


if (promedio > 6 and promedio <= 10):
        print("USTED A APROBADO")
elif(promedio == 6):                     
        print("USTED HA APROBADO")
elif(promedio >= 0 and promedio < 6):
        print("USTED HA REPROBADO")
elif(promedio < 0 or promedio >10):
        print("INGRESA UNA CALIFICACION VALIDA")
