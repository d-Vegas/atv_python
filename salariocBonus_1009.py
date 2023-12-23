nome = input("Qual seu nome? ")
salario = float(input("Qual seu salário? "))
vendas = float(input("Quanto você vendeu esse mês? "))

comissao = (15 * vendas) / 100

valorTotal = comissao + salario

print(f"O valor total que você recebeu esse mês foi de = R$ {valorTotal:.2f}")