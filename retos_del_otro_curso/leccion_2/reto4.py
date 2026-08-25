def conteo_de_materias(nombre_de_materia_1: str, nombre_de_materia_2: str, nombre_de_materia_3: str)->str:
    
    
    if "programación" or "matematica" or "filosofia" or "literatura" in nombre_de_materia_1:
        print("es una materia que le gustaria a Pedro")
    else:
        print("no es una materia que le gustaria a Pedro")
    
    if "programación" or "matematica" or "filosofia" or "literatura" in nombre_de_materia_2:
        print("es una materia que le gustaria a Pedro")
    else:
        print("no es una materia que le gustaria a Pedro")
    
    if "programación" or "matematica" or "filosofia" or "literatura" in nombre_de_materia_3:
        print("es una materia que le gustaria a Pedro")
    else:
        print("no es una materia que le gustaria a Pedro")
        
nombre_de_materia_1 = input("ingrese el nombre de la primera materia: ")
nombre_de_materia_2 = input("ingrese el nombre de la segunda materia: ")
nombre_de_materia_3 = input("ingrese el nombre de la tercera materia: ")

total_de_materias = conteo_de_materias(nombre_de_materia_1, nombre_de_materia_2, nombre_de_materia_3)


