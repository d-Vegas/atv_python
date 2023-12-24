robo = input("Como está o tempo? (Normal/Calor/Neve/Chuva) \n")

if robo == "Chuva":
    tipo = input("Qual o tipo da chuva? (Granizo/Chuva Torrencial/Normal)")
    if tipo == "Granizo":
        print("Coloque uma capa de borracha e boa aula")
    elif tipo == "Chuva Torrencial":
        print("NÃO SAIA DE CASA , PERIGO!")
    elif tipo == "Normal":
        print("Pegue o guarda-chuva e boa aula")
    else:
        print("Não saia de casa sem saber o tipo da Chuva")
        
elif robo == "Calor":
    print("Ative a ventilação dupla, e vá para escola")
elif robo == "Neve":
    print("Ative o aquecimento interno, e vá para escola")
elif robo == "Normal":
    print("Temperatura normal , pode sair e ir para a escola")
else:
    print("Não consegui indentificar o tempo, Não saia!")