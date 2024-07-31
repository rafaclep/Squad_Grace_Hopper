'''7. Desenvolver um programa que solicite a idade do usuário e identifique se
ele é uma criança, um adolescente, adulto ou idoso.
'''

def classificar_idade(idade):
    if idade < 12:
        return "criança"
    elif 12 <= idade < 18:
        return "adolescente"
    elif 18 <= idade < 60:
        return "adulto"
    else:
        return "idoso"

idade_usuario = int(input("Digite sua idade: "))

classificacao = classificar_idade(idade_usuario)

print(f"Você é um(a) {classificacao}.")
