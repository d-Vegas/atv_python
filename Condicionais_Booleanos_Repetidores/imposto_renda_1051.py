entrada = float(input())


if entrada <= 2000.00 :
    print(f'Isento')
elif entrada <= 3000.00:
        imposto = ( 8 * (entrada - 2000.00 )) / 100
        print(f"R${imposto: .2f}")
elif entrada <= 4500.00 : 
    imposto = ( 8 * 1000 ) / 100 + ( 18 * (entrada - 3000)) / 100
    print(f"R${imposto: .2f}")
elif entrada > 4500.00 :
    imposto = (8 * 1000) / 100 + (18 *  1500) / 100 + ( 28 * (entrada - 4500)) / 100
    print(f"R${imposto: .2f}")
else:
    print(f"Valor indisponivel para calculo de imposto")
    