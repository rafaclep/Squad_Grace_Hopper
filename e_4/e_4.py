nota = float(input("Digite a nota do aluno entre 0 e 10: "))

if ( 10 >= nota >= 7):
    print("Aprovado")
elif (nota < 7):
    print("Reprovado")
else:
    print("Por favor, digite uma nota entre 0 e 10.")
