#ENTRADA DE DATOS 

metros= float(input("Digita el nivel del agua:"))

nivel= metros

if(nivel ==0):
    print("ENCENDER BOMBA")
elif(nivel<0 ):
    print("FUGA DE AGUA")
elif(nivel > 0 and nivel < 2):
    print("ACELERAR BOMBA DE AGUA")
elif(nivel >= 2 and nivel < 4):
    print("BOMBA TRABAJANDO")
elif(nivel >=4 and nivel < 6):
    print("DESACELERAR BOMBA DE AGUA")
elif(nivel == 6):
    print("APAGAR BOMBA")
elif(nivel >6):
    print("DESBORDAMIENTO DE AGUA EN CISTERNA")
