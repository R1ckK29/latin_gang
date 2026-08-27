numero = int(input("ingrese un numero: "))

i = 1

for i in range(i, numero + 1):
    if i**(1/2) % 1 == 0:
        print(i)
    i += 1
