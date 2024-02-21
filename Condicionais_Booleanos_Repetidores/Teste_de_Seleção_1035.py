entrada = input("")

A, B , C , D = entrada.split()

A = int(A)
B = int(B)
C = int(C)
D = int(D)



if B > C :
    if D > A :
     soma1 = C + D 
     soma2 = A + B
     if soma1 > soma2 :
        if C > 0 and D > 0 :
          resto = A % 2 
          if resto == 0 :
            print(f"Valores aceitos")
        else :
            print(f"Valores nao aceitos") 