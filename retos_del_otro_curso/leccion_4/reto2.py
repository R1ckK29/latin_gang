def analizar_texto(texto: str, caracteres_permitidos: list) -> dict:
    diccionario = {}
    texto_minusculas = texto.lower()

    palabras = texto_minusculas.split()

    for palabra in palabras:
        if all(caracter in caracteres_permitidos for caracter in palabra):
            if palabra in diccionario:
                diccionario[palabra][0] += 1
                diccionario[palabra][2] = palabras.index(palabra)
            else:
                diccionario[palabra] = 1
                diccionario[palabra] = [1, palabras.index(palabra), palabras.index(palabra)]
                
    return diccionario
            
        
texto = "Muchos años después, frente al pelotón de fusilamiento, el coronel Aureliano Buendía había de recordar aquella tarde remota en que su padre lo llevó a conocer el hielo."
caracteres_permitidos = "abcdefghijklmnopqrstuvwxyzáéíóúüABCDEFGHIJKLMNOPQRSTUVWXYZÁÉÍÓÚÜ"

resultado = analizar_texto(texto, caracteres_permitidos)
print(resultado)           
    
    
    