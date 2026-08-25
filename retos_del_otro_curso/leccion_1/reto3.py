# -*- coding: utf-8 -*-
def calcular_cambio(dinero: int)->int:
    monedas_500 = dinero // 500
    monedas_200 = (dinero % 500) // 200
    monedas_100 = ((dinero % 500) % 200) // 100
    monedas_50 = (((dinero % 500) % 200) % 100)// 50
    mensaje = str(monedas_500) + "," + str(monedas_200) + "," + str(monedas_100)+ "," + str(monedas_50)
    return mensaje

dinero_ingresado = int(input("ingrese la cantidad de dinero: "))
vueltos = calcular_cambio(dinero_ingresado)
print("sus vueltos son: "+ str(vueltos))


    

