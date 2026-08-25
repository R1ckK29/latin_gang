def sumas_vectorial (vector_1: tuple, vector_2: tuple)->tuple:
    
    
    x, y, z = vector_1
    x_1, y_1, z_1 = vector_2
    vector_resultante = x + x_1, y + y_1, + z + z_1
    
    return vector_resultante

vector_1 = (1.0, 2.0, 3.0)
vector_2 = (4.0, 5.0, 6.0)
resultado = sumas_vectorial(vector_1, vector_2)
print(resultado)