def pintar_x (matriz: list, operacion: str)->list:
    
    if operacion == "+":
        suma = 0
        suma_total = 0
        for i in range (0, len(matriz)):
            suma += matriz[i][i]
            suma_total += matriz[i][i]
            suma_diagonal = suma + suma_total
            matriz [i][i] = suma_diagonal
            suma = 0
            suma_total = 0
            
        for i in range (0, len(matriz)):
            suma += matriz[i][len(matriz) - 1 - i]
            suma_total += matriz[i][len(matriz) - 1 - i]
            suma_diagonal = suma + suma_total
            matriz[i][len(matriz) - 1 - i] = suma_diagonal
            suma = 0
            suma_total = 0
    
    elif operacion == "-":
        resta = 0
        resta_total = 0
        for i in range (0, len(matriz)):
            resta += matriz[i][i]
            resta_total += matriz[i][i]
            resta_diagonal = resta - resta_total
            matriz [i][i] = resta_diagonal
            resta = 0
            resta_total = 0
            
        for i in range (0, len(matriz)):
            resta += matriz[i][len(matriz) - 1 - i]
            resta_total += matriz[i][len(matriz) - 1 - i]
            resta_diagonal = resta - resta_total
            matriz[i][len(matriz) - 1 - i] = resta_diagonal
            resta = 0
            resta_total = 0
            
    elif operacion == "*":
        multiplicacion = 0
        multiplicacion_total = 0
        for i in range (0, len(matriz)):
            multiplicacion += matriz[i][i]
            multiplicacion_total += matriz[i][i]
            multiplicacion_diagonal = multiplicacion * multiplicacion_total
            matriz [i][i] = multiplicacion_diagonal
            multiplicacion = 0
            multiplicacion_total = 0
            
        for i in range (0, len(matriz)):
            multiplicacion += matriz[i][len(matriz) - 1 - i]
            multiplicacion_total += matriz[i][len(matriz) - 1 - i]
            multiplicacion_diagonal = multiplicacion * multiplicacion_total
            matriz[i][len(matriz) - 1 - i] = multiplicacion_diagonal
            multiplicacion = 0
            multiplicacion_total = 0
        
    elif operacion == "/":
        division = 0
        division_total = 0
        for i in range (0, len(matriz)):
            division += matriz[i][i]
            division_total += matriz[i][i]
            division_diagonal = division / division_total
            matriz [i][i] = division_diagonal
            division = 0
            division_total = 0
            
        for i in range (0, len(matriz)):
            division += matriz[i][len(matriz) - 1 - i]
            division_total += matriz[i][len(matriz) - 1 - i]
            division_diagonal = division / division_total
            matriz[i][len(matriz) - 1 - i] = division_diagonal
            division = 0
            division_total = 0
            
    for fila in matriz:
        print(fila)
            
    return matriz

matriz = [[50, 50, 30, 20], 
         [60, 20, 20, 40], 
         [20, 20, 20, 40],
         [20, 80, 60, 20]]

operacion = "/"

resultado = pintar_x(matriz, operacion)
