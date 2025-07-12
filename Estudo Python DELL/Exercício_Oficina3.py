cursos = [
    'Engenharia de Software',
    'Python para Data Science',
    'Introdução a Java'
]

respostas = [1, 2, 0, 1, 1, 1, 1, 0, 0, 2, 2, 0, 1, 1,
             1, 1, 2, 0, 1, 1, 0, 1, 0, 2, 1, 1, 0, 2,
             2, 1, 0, 1, 1, 0, 0, 0, 1, 1, 2, 1]

votos = [0] * len(cursos) 

for resposta in respostas:
    votos[resposta] += 1  

total_votos = sum(votos)

print("Resultados da pesquisa:")
for i, curso in enumerate(cursos):
    porcentagem = (votos[i] / total_votos) * 100 if total_votos > 0 else 0
    print(f"{curso}: {votos[i]} votos ({porcentagem:.2f}%)")

curso_escolhido = cursos[votos.index(max(votos))]
print(f"\nCurso escolhido: {curso_escolhido}")
