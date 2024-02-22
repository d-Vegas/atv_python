entrada = input()
entrada2 = input()
entrada3 = input()

if entrada == 'vertebrado' :
    if entrada2 == 'ave' :
        if entrada3 == 'carnivoro':
            print(f"aguia")
        elif entrada3 == 'onivoro':
            print(f"pomba")
    elif entrada2 == 'mamifero' :
        if entrada3 == 'onivoro':
            print(f"homem")
        elif entrada3 == 'herbivoro':
            print(f"vaca")
elif entrada == 'invertebrado' :
    if entrada2 == 'inseto' :
        if entrada3 == 'hematofago':
            print(f"pulga")
        elif entrada3 == 'herbivoro':
            print(f"lagarta")
    elif entrada2 == 'anelideo' :
        if entrada3 == 'hematofago':
            print(f"sanguessuga")
        elif entrada3 == 'onivoro':
            print(f"minhoca")