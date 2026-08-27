limite_inferior = int(input("ingrese el limite inferior de la integral: "))
limite_superior = int(input("ingrese el limite superior de la integral: "))
n = int(input("ingresar el numero de particiones: "))
i = 1
delta_x = (limite_superior-limite_inferior)/n
resultado = 0

def f(x):
    return x**2

for i in range(n):
    x_i = limite_inferior + (i*delta_x)
    resultado += f(x_i)*delta_x
    
print(resultado)