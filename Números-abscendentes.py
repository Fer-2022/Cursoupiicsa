
Numero1= int(input('Digite un numero: '))


if Numero1< 0 and Numero1 > -100:
    for i in range(-1,-100,-2):
        print(f'{i}')
elif Numero1 >0 and Numero1 < 100:
    for i in range (2,101,2):
        print(f'{i}')
else:
    print("El numero que ingreso no es valido")      