def promedio_fila (matriz: list, fila: int)->float:
    
    contador = 0
    suma = 0
    
    if fila == 1:
        fila = 0
        for num_col in range(0, len(matriz[1])):
            suma += matriz [fila] [num_col]

        for num_col in range(0, len(matriz[1])):
            if matriz [fila] [num_col] != 0:
                contador += 1
                
                
    elif fila == 2:
        fila = 1
        for num_col in range(0, len(matriz[0])):
            suma += matriz [fila] [num_col]

        for num_col in range(0, len(matriz[0])):
            if matriz [fila] [num_col] != 0:
                contador += 1
                
                
    elif fila == 3:
        fila = 2
        for num_col in range(0, len(matriz[2])):
            suma += matriz [fila] [num_col]

        for num_col in range(0, len(matriz[2])):
            if matriz [fila] [num_col] != 0:
                contador += 1
   
            
    promedio = suma / contador
    return round(promedio, 2)

matriz = [[30, 30, 30], 
         [60, 60, 60], 
         [20, 20, 20]]

fila = 3

resultado = promedio_fila(matriz, fila)
print(resultado)