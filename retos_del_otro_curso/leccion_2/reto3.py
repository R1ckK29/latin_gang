# -*- coding: utf-8 -*-
def movimiento_robot(orientación_actual: str, giro_1: str, giro_2: str, giro_3: str)->str:
    
    orientación_actual_int = int(orientación_actual)
    
    if giro_1 == "L":
        orientación_actual_int -= 1 
    elif giro_1 == "R":
        orientación_actual_int += 1
    elif giro_1 == "H":
        orientación_actual_int += 2
    elif giro_1 == ".":
        orientación_actual_int += 0
        
    if giro_2 == "L":
        orientación_actual_int -= 1
    elif giro_2 == "R":
        orientación_actual_int += 1
    elif giro_2 == "H":
       orientación_actual_int += 2
    elif giro_2 == ".":
       orientación_actual_int += 0
        
    if giro_3 == "L":
        orientación_actual_int -= 1
    elif giro_3 == "R":
       orientación_actual_int += 1
    elif giro_3 == "H":
        orientación_actual_int += 2
    elif giro_3 == ".":
        orientación_actual_int += 0
        
    orientación_actual_int = orientación_actual_int % 4
    
        
    if orientación_actual_int == -3:
        print("el robot esta mirando al E")
    if orientación_actual_int == -2:
        print("el robot esta mirando al S")
    if orientación_actual_int == -1:
        print("el robot esta mirando al W")
    if orientación_actual_int == 0:
        print("el robot esta mirando al N")
    if orientación_actual_int == 1:
        print("el robot esta mirando al E")
    if orientación_actual_int == 2:
        print("el robot esta mirando al S")
    if orientación_actual_int == 3:
        print("el robot esta mirando al W")
    if orientación_actual_int == 4:
        print("el robot esta mirando al S")
    if orientación_actual_int == 5:
        print("el robot esta mirando al E")
    if orientación_actual_int == 6:
        print("el robot esta mirando al N")
        
    return str(orientación_actual_int)

orientación_actual = 0
giro_1 = input(""""ingrese lo que va a hacer el robot 
(si quiere girarlo a la izquierda escriba L
 si quiere girarlo a la derecha escriba R
 si quiere que de media vuelta escriba H
 y si quiere que se mantenga en la misma posición escriba .): """)

giro_2 = input(""""ingrese lo que va a hacer el robot: """)
               
giro_3 = input(""""ingrese lo que va a hacer el robot: """)
               
orienta_robot = movimiento_robot(orientación_actual, giro_1, giro_2, giro_3)
    
 
         
        
        
    
        
    
    
   
   
   
  
   
   
