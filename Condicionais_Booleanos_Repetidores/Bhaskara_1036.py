entrada = input("")

A, B, C = entrada.split()

A = float(A)
B = float(B)
C = float(C)

delta = B**2 - 4*A*C

if A == 0 or delta < 0:
    print("Impossivel calcular")
else:
    raiz1 = (-B + (delta ** 0.5)) / (2*A)
    raiz2 = (-B - (delta ** 0.5)) / (2*A)

    print(f"R1 = {raiz1:.5f}")
    print(f"R2 = {raiz2:.5f}")