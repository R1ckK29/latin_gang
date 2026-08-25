def conteo_de_materias(nombre_de_materia_1: str, nombre_de_materia_2: str, nombre_de_materia_3: str)->int:
    
    total_de_materias = 0
    
    if nombre_de_materia_1 in ["programación", "matematica", "filosofia", "literatura"]:
       total_de_materias += 1
    
    if nombre_de_materia_2 in ["programación", "matematica", "filosofia", "literatura"]:
        total_de_materias += 1
    
    if nombre_de_materia_3 in ["programación", "matematica", "filosofia", "literatura"]:
        total_de_materias += 1
    
    return  print(total_de_materias)
    
        
nombre_de_materia_1 = input("ingrese el nombre de la primera materia: ")
nombre_de_materia_2 = input("ingrese el nombre de la segunda materia: ")
nombre_de_materia_3 = input("ingrese el nombre de la tercera materia: ")

total_de_materias = conteo_de_materias(nombre_de_materia_1, nombre_de_materia_2, nombre_de_materia_3)


