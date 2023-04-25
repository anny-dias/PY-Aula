#5.Solicite a quantidade de alunos de uma turma e a quantidade de notas. Para cada aluno, solicite as suas notas 
#e exiba a sua respectiva média(a média deve ser arredondada para duas casas decimais).

alunos = int(input("Insira a quantidades de alunos: "))
notas = int(input("Insira a quantidade de notas: "))

for a in range (alunos):
    soma = 0 
    for i in range (notas):
        nota = float(input("Insira a nota: "))
        soma += nota
    media = nota / (notas)
    print(f'Nota final: {round(media, 2)}')

