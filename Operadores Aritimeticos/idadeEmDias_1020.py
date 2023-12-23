idade = int(input(""))

ano = idade // 365
mesDia = idade % 365
mes = mesDia // 30
dia = mesDia % 30

print(f"{ano} ano(s)")
print(f"{mes} mes(es)")
print(f"{dia} dia(s)")