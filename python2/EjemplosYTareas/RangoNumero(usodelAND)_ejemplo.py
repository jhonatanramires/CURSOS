print("hola como te llamas?")
nombre = input("escribeme tu nombre: ")
print( nombre, "asi que asi te llamas bueno", nombre)
mini = int(input("aqui escribe un numero pequeño que no sea demasiado grande: "))
maxi = int(input("aqui un numero grande el cual sea por lo menos mas grande que el que escribiste antes: "))
print("espero que hallas seguido las instrucciones por que si no te dara error y sera tu culpa")
num = int(input("escribeme un numero el que quieras :"))
input("ok te dire si el numero que escribiste esta dentro del rango de los dos primeros que me dijiste listo?: ")
rango = num <= maxi and num >= mini
if rango == 0:
    print("el numero esta fuera del rango")
else: 
    print("el numero esta dentro del rango")
