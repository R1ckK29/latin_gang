def reflejar_imagen(imagen):
    # Calculamos el ancho de la imagen dividiendo el número de columnas por 2
    ancho = len(imagen[0])
    
    # Iteramos sobre cada fila de la imagen
    for fila in imagen:
        # Intercambiamos las columnas de píxeles hasta llegar al centro
        for i in range(ancho // 2):
            # Calculamos el índice de la columna opuesta
            columna_opuesta = ancho - 1 - i
            # Intercambiamos los valores de las columnas
            fila[i], fila[columna_opuesta] = fila[columna_opuesta], fila[i]
    
    # Retornamos la imagen reflejada
    return imagen