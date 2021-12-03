def forca():

    print("*******------********")
    print("Bem Vindo ao Jogo de Forca")
    print("*******------********")

    palavra_secreta = "melancia".upper()
    letras_acertadas = ["_" for letra in palavra_secreta]

    enforcou = False
    acertou = False
    erros = 0

    print(letras_acertadas)

    #enquanto não false e não false
    while(not enforcou and not acertou):

        chute = input("Qual a letra?")
        chute = chute.strip().upper()

        if(chute in palavra_secreta):

            index = 0
            for letra in palavra_secreta:
                if(chute.upper() == letra.upper()):
                   letras_acertadas[index] = letra
                index += 1
        else:
            erros += 1
            print("Ops, você errou! Faltam {} tentativas.".format(6 - erros))


        enforcou = erros == 6
        acertou = "_" not in letras_acertadas

        print(letras_acertadas)

    if(acertou):
        print("Você ganhou!!! :)")
    else:
        print("Você perdeu! :(")

    print("FIM DE JOGO")

if(__name__ == "__main__"):
    forca()
