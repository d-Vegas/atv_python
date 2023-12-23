p1 = input("Coloque a primeira distancia")
p2 = input("Coloque a segunda distancia")

x1, y1 = p1.split()
x2, y2 = p2.split()

x1Float = float(x1)
y1Float = float(y1)

x2Float = float(x2)
y2Float = float(y2)

distancia = ((x2Float - x1Float) ** 2 + (y2Float - y1Float) ** 2) ** 0.5

print(f"{distancia:.4f}")