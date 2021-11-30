import forca
import adivinhacao

def escolhe_jogo():
    print("*******------********")
    print("Escolha o seu jogo!")
    print("*******------********")

    print("(1) Forca (2) Adivinhação")
    jogo = int(input("Qual jogo você escolhe?"))

    if(jogo == 1):
        print("Jogando forca")
        forca.forca()
    elif(jogo ==2):
        print("Jogando Adivinhação")
        adivinhacao.adivinhacao()


if(__name__ == "__main__"):
    escolhe_jogo()
