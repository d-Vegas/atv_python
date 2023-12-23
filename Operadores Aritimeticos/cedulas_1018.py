valor = int(input("Quantos reais você tem? : "))

notasDeCem = valor // 100
resto = valor % 100

notasDeCinquenta = resto // 50
resto = resto % 50 

notasDeVinte = resto // 20
resto = resto % 20

notasDeDez = resto // 10
resto = resto % 10

notasDeCinco = resto // 5
resto = resto % 5

notasDeDois = resto // 2
resto = resto % 2

notasDeUm = resto

print(valor)
print(f"{notasDeCem} nota(s) de R$ 100,00")
print(f"{notasDeCinquenta} nota(s) de R$ 50,00")
print(f"{notasDeVinte} nota(s) de R$ 20,00")
print(f"{notasDeDez} nota(s) de R$ 10,00")
print(f"{notasDeCinco} nota(s) de R$ 5,00")
print(f"{notasDeDois} nota(s) de R$ 2,00")
print(f"{notasDeUm} nota(s) de R$ 1,00")