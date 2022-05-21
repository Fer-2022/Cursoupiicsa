#importar libreria de funciones Matematicas
import math


#ENTRADA DE DATOS
#Declarar o crear variables 

número1= float(input("Escribe un número:"))
número2= float(input("Escribe otro número:"))


#PROCESOS (calculos u operaciones Matematicas y/o Logicas)
suma = número1 + número2
resta= número1 - número2
multiplicacion= número1 * número2
division= (número1 / número2)


potencia1 = número1 ** número2
potencia2 = pow(número2, número1)
cuadrado= número1 **2
cubo= pow(número2, 3)


raiz_cuadrada1 =pow(9, 1/2) 
raiz_cuadrada2 = math. sqrt(9)
raiz_cubica = pow(27, 1/3)

módulo_residuo = número1 % número2



#SALIDA DE DATOS
print ("la SUMA es igual a=", suma) #imprimir o mostrar el resultado de la suma 
print ("la suma =" + str(suma)) #CONTANECION (union de textos)
#comentario convertir un tipo de dato en otro tipo de dato (CASTEO)
print(f"la suma = {suma}") 
print ("la resta es igual a=", resta)
print ("la multiplicacion es igual a=", multiplicacion)
print ("la division es igual a=",division)
print ("la POTENCIA1 es igual a=", potencia1)
print ("la POTENCIA2 es igual a=", potencia2)
print ("el CUADRADO es igual a=",cuadrado)
print ("el CUBO es igual a=", cubo)
print ("la RAIZ CUADRADA 1 es igual a=", raiz_cuadrada1)
print ("la RAIZ CUADRADA 2 es igual a=", raiz_cuadrada2)
print ("la RAIZ CUBICA es igual a=", raiz_cubica)
print ("el resultado del MODULO es igual a=", módulo_residuo)

