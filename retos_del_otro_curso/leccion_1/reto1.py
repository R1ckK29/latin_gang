
def sub_perimetro (l1: float, l2: float, l3: float)-> float:
    """
    

    Parameters
    ----------
    l1 : float
        lado de un tringualo (siempre tiene que ser un número igual o mayor
                              que 1).
    l2 : float
        lado de un tringualo (siempre tiene que ser un número igual o mayor
                              que 1).
    l3 : float
        lado de un tringualo (siempre tiene que ser un número igual o mayor
                              que 1).

    Returns
    -------
    float
        el resultado es el subperimetro de un triangualo este siempre va a .

    """
    return (l1+l2+l3)/2


def area_triangulo (sp: float, s1: float, s2: float, s3: float)-> float:
    return round((sp * (sp-s1) * (sp-s2) * (sp-s3))**0.5, 1)

L1 = float(input("ingrese la longitu de un lado del triangulo: "))
L2 = float(input("ingrese otra longitu del triangulo: "))
L3 = float(input("ingrese la ultima longitu del triangulo: "))

Sp = sub_perimetro(L1, L2, L3)
print("el sub perimetro del triangulo es: "+ str(Sp))

At = area_triangulo(Sp, L1, L2, L3)
print("el area del triangulo es: "+ str(At))