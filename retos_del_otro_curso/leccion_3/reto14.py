def hacer_la_vaca (salon: list, vaca: str)-> list:
    numero_mayor = float('-inf')
    lista = []
    for i in range (0, len(salon)):
        sumas = 0
        for j in range(0, len(salon[0])):
            sumas = salon[i][j]
    
    if vaca == "pastel":
        if sumas < 35000:
            lista.append("No alcanza")
        else:
            lista.append("Hay pastel") 
        
    if vaca == "botella":
        if sumas < 120000:
            lista.append("No alcanza")
        else:
            lista.append("Hay botella")
    
        
    for i in range(len(salon)):
        for j in range(len(salon[0])):
            numero_actual = salon[i][j]
            if numero_actual > numero_mayor:
                numero_mayor = numero_actual
                coordenadas_mayor = (i, j)
                
    lista.append(coordenadas_mayor)
    
    return lista

salon = [[10000, 2000, 5000], 
         [10000, 1000, 90000], 
         [5000, 50, 1000000]]
vaca = "pastel"

resultado = hacer_la_vaca(salon, vaca)
print(resultado)