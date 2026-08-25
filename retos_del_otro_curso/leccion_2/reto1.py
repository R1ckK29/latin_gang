def es_divisible (n: int, d: int)->int:
    
    d_1 = n%d
    d_2 = n%(d * 2)
    
    if d_2 == 0:
        print(2)
    elif d_1 == 0:
        print(1)
    else:
        print(0)
        
        
n = int(input("ingrese el primer numero: "))
d = int(input("ingrese el segundo numero: "))
division = es_divisible(n, d)        

