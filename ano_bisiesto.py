ano = int((input("Ingrese un año: ")))
ano_bisiesto = False
if ano % 4 == 0 and ano % 100 != 0:
    ano_bisiesto = True
elif ano % 400 == 0:
    ano_bisiesto = True

if ano_bisiesto:
    print(f"el año {ano} es bisiesto")
else:
    print(f"el año {ano} no es bisiesto ")