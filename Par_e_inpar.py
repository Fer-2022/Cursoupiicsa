#ENTRADA DE DATOS 

numero=float(input("Ingresa un numero:"))

módulo= (numero % 2)

if(módulo ==0):
    print("EL NUMERO QUE INGRESO ES PAR")
elif(módulo > 0 or módulo != 0):
    print("EL NUMERO QUE INGRESO ES IMPAR")

