produto1 = input("Coloque o codigo / quantidade / valor do produto: ")
produto2 = input("Coloque o codigo / quantidade / valor do segundo produto: ")

codigo, quantidade, valor = produto1.split(" ")
codigo2, quantidade2, valor2 = produto2.split(" ")

codigo1 = int(codigo)
quant1 = int(quantidade)
valor1 = float(valor)

codigo2 = int(codigo2)
quant2 = int(quantidade2)
valor2 = float(valor2)

soma = (quant1 * valor1) + (quant2 * valor2)

print(f"VALOR A PAGAR: R$ {soma:.2f}")