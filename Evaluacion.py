aciertos= 0   #ESTA VARIABLE LA USARAMOS PARA CONTAR ACIERTOS 
print("PREGUNTA1= Herramienta de programacion, parecido al lenguaje españolutilizado para crear código")

print("a-IDE")
print("b-pseudocodigo")
print("c-Compilador")
print("d-ANSI/ISO")
respuesta1=(input("digita el inciso correcto:"))

if( respuesta1 == "b"):
    print("Respuesta correcta")
    aciertos= aciertos + 1
else:
    print("respuesta incorrecta")

print("PREGUNTA2= Conjunto de simbolos, letras, numeros,imágenes,audio y video, organizadas y que son relevantes en un tiempo y forma determinados")

print("a-Información")
print("b-Datos")
print("c-Programa")
print("d-Código")
respuesta2=(input("digita el inciso correcto:"))

if( respuesta2 == "a"):
    print("Respuesta correcta")
    aciertos= aciertos + 1
else:
    print("respuesta incorrecta")

print("PREGUNTA3= Instituciones encargadas de estandizar rreglas y simbología de los diagramas de flujo")

print("a-IEEE")
print("b-IDE")
print("c-ANSI/ISO")
print("d-VSCode")
respuesta3=(input("digita el inciso correcto:"))

if( respuesta3 == "c"):
    print("Respuesta correcta")
    aciertos= aciertos + 1
else:
    print("respuesta incorrecta")

print("PREGUNTA4= Serie de pasos consecutivos,ordenados y finitos que se siguen para resolver un problema")

print("a-Proceso")
print("b-Solución")
print("c-Función")
print("d-Algoritmo")
respuesta4=(input("digita el inciso correcto:"))

if( respuesta4 == "d"):
    print("Respuesta correcta")
    aciertos= aciertos + 1
else:
    print("respuesta incorrecta")

print("PREGUNTA5= Conjunto de elemetos que se relizan para cumplir una funcion determinada")

print("a-Estructura")
print("b-Datos")
print("c-Operación")
print("d-Sistema")
respuesta5=(input("digita el inciso correcto:"))

if( respuesta5 == "d"):
    print("Respuesta correcta")
    aciertos= aciertos + 1
else:
    print("respuesta incorrecta")

print("PREGUNTA6= Componente de un IDE que se encarga de traduccir el código fuente a código máquina")

print("a-Depurador")
print("b-Editor de texto")
print("c-Terminal de Salida")
print("d-Compilador/Interprete")
respuesta6=(input("digita el inciso correcto:"))

if( respuesta6 == "d"):
    print("Respuesta correcta")
    aciertos= aciertos + 1
else:
    print("respuesta incorrecta")

print("PREGUNTA7= Elemento que se usa para almacenar una cantidad donde cambia su valor ")

print("a-Constante")
print("b-Variable")
print("c-Librería")
print("d-Tipo de dato")
respuesta7=(input("digita el inciso correcto:"))

if( respuesta7 == "b"):
    print("Respuesta correcta")
    aciertos= aciertos + 1
else:
    print("respuesta incorrecta")

print("PREGUNTA8= Conjunto de símbolos,letras,números que no tienen significado")

print("a-Datos")
print("b-Estructura")
print("c-Información")
print("d-Sistema")
respuesta8=(input("digita el inciso correcto:"))

if( respuesta8 == "a"):
    print("Respuesta correcta")
    aciertos= aciertos + 1
else:
    print("respuesta incorrecta")

print("PREGUNTA9= Disciplina que argumenta conclusiones a partir de premisas mediante un razonamiento")

print("a-Filosofía")
print("b-Sociología")
print("c-Lógica")
print("d-Argumentación")
respuesta9=(input("digita el inciso correcto:"))

if( respuesta9 == "c"):
    print("Respuesta correcta")
    aciertos= aciertos + 1
else:
    print("respuesta incorrecta")

print("PREGUNTA10= Medida, patrón, modelo o norma universal para realizar una actividad o produccir un objeto")

print("a-Evento")
print("b-Estándar")
print("c-Calidad")
print("d-Productividad")
respuesta10=(input("digita el inciso correcto:"))

if( respuesta10 == "b"):
    print("Respuesta correcta")
    aciertos= aciertos + 1
else:
    print("respuesta incorrecta")

print("PREGUNTA11= Conjunto de elementos ordenados que componen y son la base de algo físico o no físico")

print("a-Estructura")
print("b-Estándar")
print("c-Calidad")
print("d-Productividad")
respuesta11=(input("digita el inciso correcto:"))

if( respuesta11 == "a"):
    print("Respuesta correcta")
    aciertos= aciertos + 1
else:
    print("respuesta incorrecta")

print("PREGUNTA12= Conjunto de instrucciones (código) que indican a la computadora tareas a realizar")

print("a-Operaciones/Cálculos")
print("b-Sintaxis")
print("c-Programa de computadora")
print("d-Comando")
respuesta12=(input("digita el inciso correcto:"))

if( respuesta12 == "c"):
    print("Respuesta correcta")
    aciertos= aciertos + 1
else:
    print("respuesta incorrecta")

calificacion= (aciertos * 100 ) / 120

print ("Tu CALIFICACION es igual a=", calificacion)