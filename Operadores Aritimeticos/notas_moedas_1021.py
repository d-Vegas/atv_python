valor = float(input())

notaDeCem = valor // 100
resto = valor % 100

notaDeCinquenta = resto // 50
resto = resto % 50

notaDeVinte = resto // 20 
resto = resto % 20
 
notaDeDez = resto // 10 
resto = resto % 10

notaDeCinco = resto // 5
resto = resto % 5

notaDeDois = resto // 2 
resto = resto % 2

moedaDeUm = int(resto // 1)
resto = resto % 1

moedaDeCinco = int(resto // 0.50)
resto = resto % 0.50

moedaDeVinteCinco = int(resto // 0.25)
resto = resto % 0.25

moedaDeDez = int(resto // 0.10)
resto = resto % 0.10

moedaDeZeroCinco = int(resto // 0.05)
resto = resto % 0.05


moedaDeZeroUm = int(round(resto / 0.01))
resto = resto % 0.01


print("NOTAS:")
print(f"{notaDeCem:.0f} nota(s) de R$ 100.00")
print(f"{notaDeCinquenta:.0f} nota(s) de R$ 50.00")
print(f"{notaDeVinte:.0f} nota(s) de R$ 20.00")
print(f"{notaDeDez:.0f} nota(s) de R$ 10.00")
print(f"{notaDeCinco:.0f} nota(s) de R$ 5.00")
print(f"{notaDeDois:.0f} nota(s) de R$ 2.00")
print("MOEDAS:")
print(f"{moedaDeUm:.0f} moeda(s) de R$ 1.00")
print(f"{moedaDeCinco:.0f} moeda(s) de R$ 0.50")
print(f"{moedaDeVinteCinco:.0f} moeda(s) de R$ 0.25")
print(f"{moedaDeDez:.0f} moeda(s) de R$ 0.10")
print(f"{moedaDeZeroCinco:.0f} moeda(s) de R$ 0.05")
print(f"{moedaDeZeroUm:.0f} moeda(s) de R$ 0.01")