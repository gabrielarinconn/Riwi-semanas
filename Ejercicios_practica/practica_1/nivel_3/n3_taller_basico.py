#Nivel 3 — Bucles y Repetición

#Objetivo: Dominar for y while, control de iteraciones y sumatorias.

#    Contar del 1 al 10.
#SOLUCION
#Generar una lista de numeros del 1 al 10 e imprimir cada uno usando un bucle for.
for numerolist in range(1, 11):
    #Mostrar la lista de nuemros
    print(numerolist)   

#    Sumatoria del 1 al n
#SOLUCION
#Pedir al usuario un numero n
n = int(input("Ingresa un número: "))
#Inicializar la variable suma en 0
suma = 0
#Usar un bucle for para sumar los numeros del 1 al n
#range(inicio, n + 1) genera una secuencia de numeros desde 1 hasta n inclusive
for i in range(1, n + 1):
    suma += i
#Mostrar el resultado de la sumatoria
print(f"La sumatoria del 1 al, {n}, es: {suma}")

#    Tabla de multiplicar
#SOLUCION
#Pedir al usuario un numero para generar su tabla de multiplicar
numTabla = int(input("Ingresa un número para ver su tabla de multiplicar: "))
#Usar un bucle for para generar la tabla de multiplicar del numero ingresado
for j in range(1, 11):
    #Mostrar la tabla de multiplicar
    print(f"{numTabla} x {j} = {numTabla * j}")


#    Contador regresivo con while
#SOLUCION
#Pedir al usuario un numero para iniciar el contador regresivo
numRegresivo = int(input("Ingresa un número para iniciar el contador regresivo: "))
#Usar un bucle while para hacer el contador regresivo       
while numRegresivo >= 0:
    print(numRegresivo)
    numRegresivo -= 1


#    Adivina el número (usar random)
#SOLUCION
#Importar la libreria random
import random
#Generar un numero aleatorio entre 1 y 100
numeroSecreto = random.randint(1, 5)
#Inicializar la variable adivina en None
adivina = None
#Usar un bucle while para pedirle al usuario que adivine el numero secreto
while adivina != numeroSecreto:
    adivina = int(input("Adivina el número entre 1 y 5: "))
    if adivina < numeroSecreto:
        print("Demasiado bajo. Intenta de nuevo.")
    elif adivina > numeroSecreto:
        print("Demasiado alto. Intenta de nuevo.")
    else:
        print("¡Felicidades! ¡Adivinaste el número!")

#    Sumar hasta que el usuario escriba 0
#SOLUCION
#Inicializar donde se agruparan los nuemros de usuario
sumar = 0
#Pedirle al usuario numeros para sumar
numeross = int(input("Ingrese un número para sumar (0 para finalizar la suma): "))
#Acumular los numneros y hacer la suma entre ellos, hasta el usuario diga 0 
while numeross != 0:
    sumar += numeross
    numeross = int(input("Ingrese otro número para sumar (0 para finalizar la suma): "))
#cuando el usuario ponga 0 mostrar la suma
print(f"la suma de {numeross} es {sumar}")