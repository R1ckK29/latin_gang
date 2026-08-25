# -*- coding: utf-8 -*-
def BMII (peso: float, altura: float)-> float:
    return peso / (altura**2)

peso1 = float(input("ingrese su peso en libras: "))
print("su peso en kilogramos es: ", (peso1 / 2.205))

altura1 = float(input("ingrese su altura en pulgadas: "))
print("su altura en metros es: ", (altura1 / 39.37))

BMI = BMII(peso1, altura1)
print("Su BMI es: "+ str(BMI))
