import função

palavra = função.palavra_forca()
letras_usuario = []
chances = função.chances_forca()
dica = função.dica_forca()
ganhou = False
letras_usadas = []

print(palavra)

while True:
    print(" ")
    print(f"O TEMA DA FORCA É: {dica}")

    for letra in palavra:
        if letra in letras_usuario:
            print(letra, end=" ")
        else:
            print("#", end=" ")

    print("\nVidas:", " ❤️" * chances)

    tentativa = input("\nEscolha uma letra: ")
    letras_usuario.append(tentativa)
    letras_usadas.append(tentativa)

    if tentativa not in palavra:
        chances = chances - 1
        print("Errou!")

        if chances > 0:
            print("\nVidas restantes:", " ❤️" * chances)

            print("Letras usadas:", ", ".join(letras_usadas))
        
        if tentativa in letras_usadas:
            print("Você já tentou essa letra!")

        else:
            print("\n💀 Suas vidas acabaram!")
            print(f"Você perdeu! A palavra era: {palavra}")
            break
    
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
