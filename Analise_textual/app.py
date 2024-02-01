class TratadorDeTextos:
    def __init__(self, texto):
        self.texto = texto.lower()
        self.palavras = self.texto.split()

    def contar_palavras(self):
        return len(self.palavras)

    def contar_ocorrencias_palavra(self, palavra):
        return self.palavras.count(palavra.lower())

    def substituir_palavra(self, palavra_original, palavra_nova):
        self.texto = self.texto.replace(palavra_original.lower(), palavra_nova.lower())
        self.palavras = self.texto.split()

    def mostrar_texto(self):
        return self.texto

texto_usuario = input("Digite um texto: ")

tratador = TratadorDeTextos(texto_usuario)

print("Quantidade de palavras no texto:", tratador.contar_palavras())

palavra_alvo = input("Digite a palavra para contar as ocorrências: ")
print(f"Ocorrências da palavra '{palavra_alvo}':", tratador.contar_ocorrencias_palavra(palavra_alvo))

palavra_substituir_original = input("Digite a palavra a ser substituída: ")
palavra_substituir_nova = input("Digite a nova palavra: ")
tratador.substituir_palavra(palavra_substituir_original, palavra_substituir_nova)
print("Texto após substituição:", tratador.mostrar_texto())
