intervalo = float(input())

if intervalo >= 0 and intervalo <= 25:
    print(f"Intervalo [0,25]")
elif intervalo > 25 and intervalo <= 50:
    print(f"Intervalo (25,50]")
elif intervalo > 50 and intervalo <= 75:
    print(f"Intervalo (50,75]")
elif intervalo > 75 and intervalo <= 100:
    print(f"Intervalo (75,100]")
else:
    print(f"Fora de intervalo")
