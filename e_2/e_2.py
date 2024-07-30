turnoAula = input("Digite o turno em que você estuda (M-Matutino, V-Vespertino ou N-Noturno): ")
turnoAula = turnoAula.upper()

if (turnoAula == 'M'):
   print("Bom Dia!")
elif (turnoAula == 'V'):
   print("Boa Tarde!")
elif (turnoAula == 'N'):
   print("Boa Noite!")
else:
   print("Por favor, digite uma opção válida!")
