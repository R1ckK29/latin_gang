import math as m

n = int(input("ingrese el n-esimo valor: "))
angulo = int(input("ingrese el angulo: "))

radianes = angulo * (m.pi/180)

sumatoria_numerador = (-1)**n * radianes**(2*n-1)

limite = 2*n-1 
sumatoria_denominador = 1


i = 1

while i <= limite:
    sumatoria_denominador = sumatoria_denominador * i
    i += 1

division = sumatoria_numerador/sumatoria_denominador

print(division)

