#declarando variables
num = 50
num1 = -5

#uso del and se hacen dos operacion conjuntas si dan lo mismo se da un solo resultado 
#si los resultados son diferentes se muestran los dos resultados
mini = 0
maxi = 20
rango = num <= maxi and num >= mini
print(rango)

#uso del or se hacen dos operaciones si algunas de las dos es true el resultado sera true sin importar
#que el otro sea falso soolo es falso cuando los dos resultados dan falso 
num = 7
num1 = 6
par = num%2 == 0 or num1%2 == 0 
print(par)

#not hace que los valores booleanos sean contrios osea si antes era trua con el not sera false
print(not(par))

