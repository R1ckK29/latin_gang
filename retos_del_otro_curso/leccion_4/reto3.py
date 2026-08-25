def binarizar_imagen(imagen, umbral):
    # Creamos una matriz vacía para almacenar la imagen binarizada
    imagen_binarizada = []
    
    # Iteramos sobre cada fila de la imagen original
    for fila in imagen:
        # Creamos una lista para almacenar los píxeles binarizados de la fila actual
        fila_binarizada = []
        # Iteramos sobre cada píxel en la fila
        for pixel in fila:
            # Calculamos el promedio de los componentes RGB del píxel
            promedio_color = sum(pixel) / 3
            # Binarizamos el píxel según el umbral
            if promedio_color >= umbral:
                # Si el promedio es igual o mayor al umbral, asignamos blanco (1, 1, 1)
                fila_binarizada.append((1, 1, 1))
            else:
                # Si el promedio es menor al umbral, asignamos negro (0, 0, 0)
                fila_binarizada.append((0, 0, 0))
        # Agregamos la fila binarizada a la imagen binarizada
        imagen_binarizada.append(fila_binarizada)
    
    # Retornamos la imagen binarizada
    return imagen_binarizada
