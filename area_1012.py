area = input("Coloque as areas que deseja calcular: ")
a, b, c = area.split()

a_float = float(a)
b_float = float(b)
c_float = float(c)
pi = 3.14159

triangulo = (a_float * c_float) / 2 
circulo = pi * c_float ** 2
trapezio = (a_float + b_float) * c_float / 2 
quadrado = b_float ** 2
retangulo = a_float * b_float


print(f"TRIANGULO: {triangulo:.3f}")
print(f"CIRCULO: {circulo:.3f}")
print(f"TRAPEZIO: {trapezio:.3f}")
print(f"QUADRADO: {quadrado:.3f}")
print(f"RETANGULO: {retangulo:.3f}")