print("Bem vindo a calculadora em python!")

valor1 = float(input("Digite o primeiro número \n"))
operador = input("Escolha o operador logico { + } { - } { / } { * } \n")
valor2 = float(input("Digite o segundo número \n"))


if operador == "+" or operador == "{ + }" :
    soma = valor1 + valor2
    print(f"A soma de {valor1} + {valor2} é {soma}")
elif operador == "-" or operador == "{ - }":
    diminuicao = valor1 - valor2
    print(f"A subtração de {valor1} - {valor2} é {diminuicao}")
elif operador == "/" or operador == "{ / }":
    divisao = valor1 / valor2
    print(f"A subtração de {valor1} / {valor2} é {divisao}")
elif operador == "*" or operador == "{ * }":
    multiplicacao = valor1 * valor2
    print(f"A multiplicação de {valor1} * {valor2} é {multiplicacao}")
else:
    print("O operador logico não foi encontrado")