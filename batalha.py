campo1 = []
campo2 = []

for lista in range(0,5):
    lista = []
    for coluna in range(0,5):
        lista.append(0)
        campo1.append(lista)
        campo2.append(lista)

    
    for linha in range(0,5):
        print(campo1[linha])
        
        
resposta = 9

while (resposta != 0):
    print("\nDigite 1 para cadrastar \n Digite 2 para atacar \nDigite 0 para sair") 
    resposta = int(input("\Digite sua opção"))

    if (resposta == 1):
        player = int(input("\n Qual jogador eu sou (1 ou 2): "))
        linha = int(input("\n Digite linha: "))
        coluna = int(input("\n Digite a coluna: "))
        if(player == 1):
            campo1[linha][coluna] = 1
        else:
            campo2[linha][coluna] =1
    elif(resposta == 2):
        player = int(input("\n Qual jogador eu sou (1 ou 2): "))
        linha = int(input("\n Digite linha: "))
        coluna = int(input("\n Digite a coluna: "))

    if(player == 1):
        if(campo2[linha][coluna] == 1):
            print("\n acertou")
            campo2[linha][coluna] = 0
        else:
            print("\n Errou")
        if (campo1[linha][coluna] == 1):
            print("\n acertou")
            campo2[linha][coluna] = 0
        else:
            print("\n Errou")

            venceu = True
        for linha in range(0,5):
            for coluna in range(0,5):
                if(campo1 [linha][coluna == 1]):
                    venceu = False

        if(venceu):
            print("\n jogador 2 venceu!")



    elif(resposta == 3):
        player = int(input("\n Qual jogador eu sou (1 ou 2): "))
        if (player == 1):
            for linha in range (0,5):
                print(campo1[linha])
            else:
                for linha in range(0,5):
                    print(campo2[linha])
    


    


