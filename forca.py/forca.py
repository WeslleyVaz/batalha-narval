import função

palavra = função.palavra_forca()
letras_usuario = []
chances = função.chances_forca()
dica = função.dica_forca()
ganhou = False

while True:
    print(" ")

    print(f"O TEMA DA FORCA É: {dica}")

    for letra in palavra:
        if letra in letras_usuario:
            print(letra, end=" ")
        else:
            print("#", end=" ")

    tentativa = input("\nEscolha uma letra: ")
    letras_usuario.append(tentativa)

    if tentativa not in palavra:
        chances = chances - 1
        print("Errou! Chances:", chances)
    else:
        print("Acertou!")

    ganhou = True

    for letra in palavra:
        if letra not in letras_usuario:
            ganhou = False

    if ganhou:
        print(f"\nParabéns, você ganhou! A palavra era: {palavra}")
        break

    if chances == 0:
        print(f"\nVocê perdeu! A palavra era: {palavra}")
        break
