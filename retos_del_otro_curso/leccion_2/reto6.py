def picas_y_fijas(numero_secreto: int, intento: int) -> dict:
        diccionario = {"PICAS": 0, "FIJAS": 0}
        
        a = intento % 10
        intento = intento // 10
        b = intento % 10
        intento = intento // 10
        c = intento % 10
        intento = intento // 10
        d = intento % 10
        intento = intento // 10
        if str(a) in str(numero_secreto) and numero_secreto % 10 == intento % 10:
            diccionario["FIJAS"] += 1
        else:
            diccionario["FIJAS"] += 0
        if str(a) in str(numero_secreto) and numero_secreto % 10 != intento % 10:
            diccionario["PICAS"] += 1
        else:
            diccionario["PICAS"] += 0
        numero_secreto = numero_secreto // 10
        intento = intento // 10
        if str(b) in str(numero_secreto) and numero_secreto % 10 == intento % 10:
            diccionario["FIJAS"] += 1
        else:
            diccionario["FIJAS"] += 0
        if str(b) in str(numero_secreto) and numero_secreto % 10 != intento % 10:
            diccionario["PICAS"] += 1
        else:
            diccionario["PICAS"] += 0
        numero_secreto = numero_secreto // 10
        intento = intento // 10
        if str(c) in str(numero_secreto) and numero_secreto % 10 == intento % 10:
            diccionario["FIJAS"] += 1
        else:
            diccionario["FIJAS"] += 0
        if str(c) in str(numero_secreto) and numero_secreto % 10 != intento % 10:
            diccionario["PICAS"] += 1
        else:
            diccionario["PICAS"] += 0
        numero_secreto = numero_secreto // 10
        intento = intento // 10
        if str(d) in str(numero_secreto) and numero_secreto % 10 == intento % 10:
            diccionario["FIJAS"] += 1
        else:
            diccionario["FIJAS"] += 0
        if str(d) in str(numero_secreto) and numero_secreto % 10 != intento % 10:
            diccionario["PICAS"] += 1
        else:
            diccionario["PICAS"] += 0
        numero_secreto = numero_secreto // 10
        intento = intento // 10
        return diccionario
    
numero_secreto = 4321
intento = 1234

resultado = picas_y_fijas(numero_secreto, intento)
print(resultado)
