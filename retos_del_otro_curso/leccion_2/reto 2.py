

def clasificar_regalo(iD: int)->str:
    
    iD_palindromo = str(iD)[::-1]
    iD_par = iD%2
    
  
    if iD < 100 or iD > 999:
        print("haz colocado una iD erronea")
    elif iD_par == 0 and int(iD_palindromo) == iD:
        persona_regalo = "boy"
    elif iD_par != 0 and int(iD_palindromo) == iD:
        persona_regalo = "girl"
    elif iD_par == 0 and int(iD_palindromo) != iD:
       persona_regalo = "hombre"
    elif iD_par != 0 and int(iD_palindromo) != iD:
        persona_regalo = "mujer" 
    return print(persona_regalo)
    
regalo = int(input("ingrese su iD: "))
regalo = clasificar_regalo(regalo)
        
    
    

        
           
    
 