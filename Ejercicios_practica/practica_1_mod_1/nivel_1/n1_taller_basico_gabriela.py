#NIVEL 1
#Objetivo: Practicar tipos de datos, entrada y salida, concatenación y operaciones básicas.

 
#EJERCICIO 
#    Hola usuario: pide al usuario su nombre y edad. Luego imprime un mensaje: "Hola [nombre], tienes [edad] años."
#SOLUCION
# Pedirle al usuario el nombre y que obligatoriamente sea con letras
nombre = str(input("¿Como te llamas? "))
# mostrar el nombre
print (f"Hola {nombre}")
# pedirle la edad al usuario y que obligatoriamente sea numeros 
edad = int(input("¿Cual es tu edad? ")) 
# mostrar el nombre y la edad
print (f"Hola {nombre}, tienes {edad} años")

#EJERCICIO
#    Suma de dos números.
#SOLUCION
#Pedirle al usuario que ingrese un numero
n1 = int(input("Ingrese un numero: "))
#Pedirle al usuario que ingrese otro numero
n2 = int(input("Ingrese otro numero: "))
#Hacer la suma de los dos numeros ingresados
suma = n1 + n2
#Mostrar la respuesta en dond diga cuales fueron los numeros ingrsados y el resultado de la suma 
print (f"La suma de {n1} y {n2} es {suma}")

#EJERCICIO 
#    Área del triángulo.
#SOLUCION
#Pedirle al usuario que ingrese la altura del triangulo
al= int(input("Medida de altura: "))
#Pedirle al usuario que ingrese la base del triangulo
an = int(input("Medida de base: "))
#Hacer la operacion alto x ancho /2 para hallar el area del tringulo
area = (al * an)/2
#Mostrar la respuesta en dond diga cuales fueron los numeros ingrsados y el resultado de la suma 
print (f"El area del triangulo es {area} siendo la atura {al} y la base {an}")

#EJERCICIO
#    Conversor de grados Celsius a Fahrenheit.
#SOLUCION
#Pedirle al usuario los grados Celsius
cel= int(input("Grados Celsius: "))
#Hacer la operacion de celsius a fahrenheit
grados = (cel*1.8)+32 
#Mostrar la conversion 
print (f"La temperatura {cel} Celsius es el equivalente a {grados}Fahrenheit")


#EJERCICIO
#    Tipo de dato: usar type() para mostrar el tipo de cada variable.
#SOLUCION
#Asignarle a cada variable una informacion de tipo int,str,bool,float
nombre = "Gabriela"
edad = 65
es_valido = True
promedio = 11.5
#Mostrar que tipo contenido fue asignado a la variable
print(type(nombre))
print(type(edad))
print(type(es_valido))
print(type(promedio))


#EJERCICIO
#    Edad futura: pide la edad actual y muestra cuántos años tendrá el usuario dentro de 10 años.
#SOLUCION
#Pedirle al usuario que ingrese su edad
edadActual = int(input("Ingrese su edad: "))
#Hacer la suma de 10 a la edad ingresadal
sumaEdad = edadActual + 10
#Mostrar la respuesta en donde diga su edad futura sumando 10 años
print (f"Tu edad en 10 años será {sumaEdad} años")