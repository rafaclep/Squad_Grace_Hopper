'''Vamos construir um jogo de forca. O programa escolherá aleatoriamente uma palavra secreta de uma lista predefinida. A palavra secreta será representada por espaços em branco, um para cada letra
da palavra. O jogador terá um número limitado de 6 tentativas. Em cada tentativa, o jogador pode fornecer uma letra. Se a letra estiver presente na palavra secreta, ela será revelada nas posições correspondentes. Se
a letra não estiver na palavra, uma mensagem de erro deverá ser informada. Após um número máximo de erros, o jogador perde. O jogo continua até que o jogador adivinhe a palavra ou exceda o número
máximo de tentativas.
Dica: Você precisará importar uma biblioteca para resolver esse
exercício'''

import random

palavrasForca = ["exceto", "cinico", "utopia", "habito", "remoto", "amor", "fato", "vovo", "doce", "cela"]
letraDigitada = []

def escolhaPalavra(palavrasForca):
    return random.choice(palavrasForca)

def digitaLetra():
    while True:
        letra = str(input("Digite uma letra: ")).lower()
        if len(letra) != 1:
            print ("EI, não vale digitar mais de uma letra!")
        elif letra in letraDigitada:
            print("Você já digitou essa letra!")
        else:
            letraDigitada.append(letra)
            return letra

def escondePalavra(palavra):

    palavraSecreta = ""
    for letra in palavra:
        if letra in letraDigitada:
            palavraSecreta += letra
        else:
            palavraSecreta += " _ "
    return palavraSecreta

def jogoForca():
    palavraEscolhida = escolhaPalavra(palavrasForca)
    tentativasRestantes = 6 

    palavraEscondida = escondePalavra(palavraEscolhida)
    print("A palavra secreta está assim: " + palavraEscondida)

    while tentativasRestantes > 0:
        print(f"Você ainda tem {tentativasRestantes} tentativa(s)\n")

        letra = digitaLetra()

        if letra in palavraEscolhida:
            print(f"Isso aí! A letra {letra} está na palavra.")
        else:
            tentativasRestantes -= 1
            print(f"Que pena, a letra {letra} não está na palavra. Perdeu uma tentativa.")

        
        palavraEscondida = escondePalavra(palavraEscolhida)
        print("A palavra secreta está assim: " + palavraEscondida)

        if "_" not in palavraEscondida:
            print(f"Parabéns! Você adivinhou a palavra: {palavraEscolhida}")
            break
    else:
        print(f"Que pena! Você não adivinhou a palavra. A palavra era: {palavraEscolhida}")

jogoForca()