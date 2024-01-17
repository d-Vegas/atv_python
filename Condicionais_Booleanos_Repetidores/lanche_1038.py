order = input()

code, quant = order.split(" ")

code = int(code)
quant = int(quant)

if code == 1:
    valor = 4
    valor = quant * valor
    print(f"Total: R$ {valor:.2f}")
elif code == 2:
    valor = 4.50
    valor = quant * valor
    print(f"Total: R$ {valor:.2f}")
elif code == 3:
    valor = 5
    valor = quant * valor
    print(f"Total: R$ {valor:.2f}")
elif code == 4:
    valor = 2
    valor = quant * valor
    print(f"Total: R$ {valor:.2f}")
elif code == 5:
    valor = 1.50
    valor = quant * valor
    print(f"Total: R$ {valor:.2f}")