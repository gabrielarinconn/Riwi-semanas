#Nivel 2 — Condicionales (Decisiones)

#Objetivo: Comprender y aplicar estructuras if, elif, else.


#    Mayor de edad
#SOLUCION
#Pedirle al usuario la edad
userEdad = int(input("¿Cual es tu edad? "))
#Usar If para validar si el usuario tiene la edad minima para votar
if userEdad >= 18:
    print ("Eres mayor de edad")
else:
    print ("No eres mayor de edad")


#    Número positivo, negativo o cero
#SOLUCION
#Pedirle al usuario un número
tipoNum = int(input("Ingresa un número, puede ser positivo o negativo "))
#Validar si el numero ingresado es positivo, negativo o cero
if tipoNum > 0:
    #Mostrar el resultado de la validacion
    print (f"El número {tipoNum} es positivo")
elif tipoNum == 0:
    print (f"El número ingresado es 0")
else:
    print (f"El número {tipoNum} es negativo")


#    Par o impar
#SOLUCION
#Pedirle al usuario un numero
numeroI = int(input("Ingresa un número: "))
#Validar si el numero ingresado es par o impar
if numeroI % 2 == 0:
    print (f"El {numeroI} es par")
else:
    print (f"El {numeroI} es impar")
    


#    Calculadora básica con +, -, *, /
#SOLUCION


#Pedirle al usuario que escriba que operacion desea hacer
operacion = str(input("¿Que operación deseas realizar? Escribe alguno de estos: - , + , / , * : "))
#Pedir al usuario el primer numero que desea aplicar la operacion
nn1 = int(input("Escribe el primer número: "))
#Pedir al usuario el segundo numero que desea aplicar la operacion
nn2 = int(input("Escribe el segundo número: "))
#Declarar las operaciones de - + / *
sumar = nn1 + nn2
resta = nn1 - nn2
division = nn1 / nn2
multi = nn1 * nn2
#Realizar la operacion con los numeros ingresados
if operacion == "-":
    print(f"{nn1} - {nn2} = {resta}")
elif operacion == "+":
    print(f"{nn1} + {nn2} = {sumar}")
elif operacion == "/":
    print(f"{nn1} / {nn2} = {division}")
else:
    print(f"{nn1} * {nn2} = {multi}")



#    Clasificador de notas (Excelente, Aprobado, Reprobado)
#SOLUCION
#Pedir al usurio que ingrese su nota
nota = int(input("Ingrese su nota del 1 al 5: "))
#Mostrar respuesta segun la nota
if nota == 5:
    print("EXCELENTE")
elif nota >= 3:
    print ("APROBADO")
else:
    print("REPROBADO")


#    Comparador de tres números: mayor y menor
#SOLUCION
#Pedir al usuario tres numeros
g = float(input("Ingresa el primer numero para comparar: "))
a = float(input("Ingresa el segundo numero para comparar: "))
b = float(input("Ingresa el tercero numero para comparar: "))
#Definir el mayor y el menor
mayor = max (g,a,b)
menor = min (g,a,b)
#Mostrar el resultado de cual es el mayor y cual es el mneor entre los tres numeros
print(f"El número mayor es: {mayor}")
print(f"El número menor es: {menor}")