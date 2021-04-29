#declarando variables
num = 10
num1 = 5
 
#operador de igualdad
igual = num == num1
print(igual) #el resultado es un true o false dependiendo si son iguales o no 

#operador de diferencia 
diferente = num != num1
print(diferente) #el resultado es un true o false dependiendo si son diferentes o no 

#operadores de si es mayor o menor
mayor = num > num1
menor = num < num1 #el resultado es un true o false dependiendo si es mayor o menor 
print(menor)
print(mayor)

#operadores juntos
igualymayor =  num >= num1 #se pregunta si es mayor y si es gual al mismo tiempo
print(igualymayor)

#caso de uso 
if num%2 == 0: 
    print("es un numero par")
else:
    print("es impar")

#caso de uso 2
mayor = 18 
edad = int(input("escribeme tu edad: "))
if edad >= mayor:
    print("eres mayor de edad que viejo estas")
else:
    print("eres menor de edad aun")
