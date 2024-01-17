num = input()

A , B = num.split(" ")

A = int(A)
B = int(B)

if A % B == 0 or B % A == 0: 
 print(f"Sao Multiplos")
else:
 print(f"Nao sao Multiplos")