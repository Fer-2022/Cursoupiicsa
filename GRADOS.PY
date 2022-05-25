#ENTRADA DE DATOS

c= float(input("Escribe el numero de grados:"))

#PROCESOS 

kelvin= c + 273.15
celsius= kelvin - 273.15
fahrenheit= ((9 *kelvin -273.15) /5) + 32
celsius2= ((5 * fahrenheit-32)) /9
fahrenheit2= ((9*celsius)/5) + 32

#RESULTADOS

print("Los grados en KELVIN es igual a:", kelvin)
print("Los grados en CELSIUS es igual a:", celsius)
print("Los grados en FAHRENHEIT es igual a:", fahrenheit)
print("La conversion de grados FAHRENHEIT a CELSIUS es igual a:", celsius2)
print("La conversion de grados CELSIUS a FAHRENHEIT es igual a:", fahrenheit2)

