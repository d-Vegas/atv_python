entrada = input()

a, b , c , d = entrada.split()

a = int(a)
b = int(b)
c = int(c)
d = int(d)

inicio_minutos = a * 60 + b
final_minutos = c * 60 + d
duracao_minutos = final_minutos - inicio_minutos

if duracao_minutos < 1:
    duracao_minutos += 24 * 60
elif duracao_minutos > 24 * 60:
    duracao_minutos %= 24 * 60

duracao_horas = duracao_minutos // 60
duracao_minutos = duracao_minutos % 60

print(f"O JOGO DUROU {duracao_horas} HORA(S) E {duracao_minutos} MINUTO(S)")