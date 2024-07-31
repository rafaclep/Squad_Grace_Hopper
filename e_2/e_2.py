#Reverso do número. Faça uma função que retorne o reverso de um número inteiro informado. Por exemplo: 127 -> 721.

def reversao(numero):
    
    numeroInvertido = str(numero)[::-1]
    return numeroInvertido

numeroInformado=int(input("Digite um número inteiro: "))
num = reversao(numeroInformado)
print(f"O número invertido é: {num}")