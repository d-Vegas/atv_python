tempo = int(input("Coloque os segundos: "))

minutos = tempo // 60
segundos = tempo % 60
horas = minutos // 60
minutos = minutos % 60

print(f"{horas}:{minutos}:{segundos}")