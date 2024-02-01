import random

class JogoDeCartas:
    def __init__(self):
        self.cartas = []

    def adicionar_carta(self):
        # Carta aleatória
        nova_carta = random.randint(0, 9)

        # Se já tivermos 3 cartas, removemos a menor antes de adicionar a nova
        if len(self.cartas) == 3:
            menor_carta = min(self.cartas)
            if nova_carta > menor_carta:
                self.cartas.remove(menor_carta)
                self.cartas.append(nova_carta)
        else:
            # Se tiver menos de 3 cartas, adicionamos a nova
            self.cartas.append(nova_carta)

    def calcular_pontuacao(self):
        return sum(self.cartas)

    def exibir_status(self):
        print(f"Cartas atuais: {self.cartas}")
        print(f"Pontuação: {self.calcular_pontuacao()}")

jogador = JogoDeCartas()

while True:
    jogador.adicionar_carta()
    jogador.exibir_status()

    continuar = input("Deseja adicionar mais uma carta? (s/n): ").lower()
    if continuar != 's':
        break
