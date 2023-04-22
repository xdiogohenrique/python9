palavra = input("Insira a palavra:")

palavraCaixaAlta = palavra.upper()
palavraCaixaBaixa = palavra.lower()

print("O tamanho da palvra é:", len(palavra))
print(palavraCaixaAlta,"\n",palavraCaixaBaixa)

palavraCopiada = palavra
cont = 0

for i in range (0, len(palavra), 1):
    for j in range (0, len(palavra),1):
        if palavraCopiada[i] == palavra [j]:
            cont = cont + 1
    print("A letra ", palavraCopiada[i], "aparece", cont, "vezes")
    cont = 0       