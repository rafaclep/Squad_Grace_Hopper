'''5. Crie uma função chamada contar_vogais que recebe uma string
como parâmetro. Implemente a lógica para contar o número de vogais
na string e retorne o total de vogais. Solicite ao usuário para inserir uma
frase e utilize a função para contar as vogais.'''

def contar_vogais(frase):
    vogais = "aeiouAEIOU"
    contador = 0
    for caracter in frase:
        if caracter in vogais:
            contador += 1
    return contador

# Solicita ao usuário para inserir uma frase
frase_usuario = input("Digite uma frase: ")

# Utiliza a função para contar as vogais na frase do usuário
total_vogais = contar_vogais(frase_usuario)

print(f"O total de vogais na frase é: {total_vogais}")
