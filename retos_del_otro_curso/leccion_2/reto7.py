def mejor_del_salon(estudiante_1: dict, estudiante_2: dict, estudiante_3: dict, estudiante_4: dict, estudiante_5: dict)->str:
    estudiante_1 = {"nombre": "B",
                    "matematicas": 1.0,
                    "español": 1.0,
                    "ciencias": 1.0,
                    "literatura": 1.0,
                    "arte": 1.0} 
                    

    # Acceder a los valores numéricos y calcular el promedio
    promedio_estudiante_1 = (estudiante_1["matematicas"] + estudiante_1["español"] +
                estudiante_1["ciencias"] + estudiante_1["literatura"] +
                estudiante_1["arte"]) / 5
    
    estudiante_2 = {"nombre": "a",
                    "matematicas": 1.0,
                    "español": 1.0,
                    "ciencias": 1.0,
                    "literatura": 1.0,
                    "arte": 1.0}

    # Acceder a los valores numéricos y calcular el promedio
    promedio_estudiante_2 = (estudiante_2["matematicas"] + estudiante_2["español"] +
                estudiante_2["ciencias"] + estudiante_2["literatura"] +
                estudiante_2["arte"]) / 5
    
    estudiante_3 = {"nombre": "c",
                    "matematicas": 1.0,
                    "español": 1.0,
                    "ciencias": 1.0,
                    "literatura":1.0,
                    "arte": 1.0}

    # Acceder a los valores numéricos y calcular el promedio
    promedio_estudiante_3 = (estudiante_3["matematicas"] + estudiante_3["español"] +
                estudiante_3["ciencias"] + estudiante_3["literatura"] +
                estudiante_3["arte"]) / 5
    
    estudiante_4 = {"nombre": "d",
                    "matematicas": 1.0,
                    "español": 1.0,
                    "ciencias": 1.0,
                    "literatura":1.0,
                    "arte": 1.0}

    # Acceder a los valores numéricos y calcular el promedio
    promedio_estudiante_4 = (estudiante_4["matematicas"] + estudiante_4["español"] +
                estudiante_4["ciencias"] + estudiante_4["literatura"] +
                estudiante_4["arte"]) / 5
    
    estudiante_5 = {"nombre": "e",
                    "matematicas": 1.0,
                    "español": 1.0,
                    "ciencias": 1.0,
                    "literatura":1.0,
                    "arte": 1.0}

    # Acceder a los valores numéricos y calcular el promedio
    promedio_estudiante_5 = (estudiante_5["matematicas"] + estudiante_5["español"] +
                estudiante_5["ciencias"] + estudiante_5["literatura"] +
                estudiante_5["arte"]) / 5
    
    nombre_minusculas_1 = estudiante_1["nombre"].lower()
    nombre_minusculas_2 = estudiante_2["nombre"].lower()
    nombre_minusculas_3 = estudiante_3["nombre"].lower()
    nombre_minusculas_4 = estudiante_4["nombre"].lower()
    nombre_minusculas_5 = estudiante_5["nombre"].lower()
    
    nombre_mayor = nombre_minusculas_1
    
    if nombre_minusculas_2 < nombre_mayor:
        nombre_mayor = nombre_minusculas_2
        
    if nombre_minusculas_3 < nombre_mayor:
        nombre_mayor = nombre_minusculas_3
    
    if nombre_minusculas_4 < nombre_mayor:
        nombre_mayor = nombre_minusculas_4
        
    if nombre_minusculas_5 < nombre_mayor:
        nombre_mayor = nombre_minusculas_5
        
    
  
        
    if promedio_estudiante_1 == promedio_estudiante_2 and  promedio_estudiante_1 == promedio_estudiante_3 and  promedio_estudiante_1 == promedio_estudiante_4 and  promedio_estudiante_1 == promedio_estudiante_5 and promedio_estudiante_2 == promedio_estudiante_3 and promedio_estudiante_2 == promedio_estudiante_4 and promedio_estudiante_2 == promedio_estudiante_5 and  promedio_estudiante_3 == promedio_estudiante_4 and promedio_estudiante_4 == promedio_estudiante_5:
       return nombre_mayor
    

    
    
        
    mayor = promedio_estudiante_1
    
    if promedio_estudiante_2 > mayor:
        mayor = promedio_estudiante_2
        
    if promedio_estudiante_3 > mayor:
        mayor = promedio_estudiante_3
        
    if promedio_estudiante_4 > mayor:
        mayor = promedio_estudiante_4
        
    if promedio_estudiante_5 > mayor:
        mayor = promedio_estudiante_5 
    
    
    
    if mayor == promedio_estudiante_1:
       mejor_promedio = estudiante_1["nombre"]
    elif mayor == promedio_estudiante_2:
       mejor_promedio = estudiante_2["nombre"]
    elif mayor == promedio_estudiante_3:
       mejor_promedio = estudiante_3["nombre"]
    elif mayor == promedio_estudiante_4:
       mejor_promedio = estudiante_4["nombre"]
    elif mayor == promedio_estudiante_5:
       mejor_promedio = estudiante_5["nombre"]
        
    return str(mejor_promedio) 


    
    

       
   
       
    

estudiante_1 = {""}
estudiante_2 = {""}      
estudiante_3 = {""}      
estudiante_4 = {""}     
estudiante_5 = {""} 

maximo_promedio = mejor_del_salon(estudiante_1, estudiante_2, estudiante_3, estudiante_4, estudiante_5)
print("el mejor promedio del salon es: " + maximo_promedio)       





