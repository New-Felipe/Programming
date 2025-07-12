livraria = {}

def adicionar_livro(titulo, genero, subgenero, editora, num_copias, valor):
    # Adiciona o livro à estrutura de dados
    if genero not in livraria:
        livraria[genero] = {}
    if subgenero not in livraria[genero]:
        livraria[genero][subgenero] = []
    
    livro = {
        'titulo': titulo,
        'editora': editora,
        'num_copias': num_copias,
        'valor': valor
    }
    livraria[genero][subgenero].append(livro)

def apresentar_livros():
    for genero in sorted(livraria.keys()):
        print(f"--- {genero} ---")
        for subgenero in sorted(livraria[genero].keys()):
            print(f"------ {subgenero} ------")
            livros_ordenados = sorted(livraria[genero][subgenero], key=lambda x: x['num_copias'])
            for livro in livros_ordenados:
                print(livro['titulo'])

# Exemplo de uso
adicionar_livro("Livro 01", "Gênero A", "Subgênero A.1", "Editora A", 5, 29.90)
adicionar_livro("Livro 02", "Gênero A", "Subgênero A.1", "Editora B", 3, 39.90)
adicionar_livro("Livro 03", "Gênero A", "Subgênero A.2", "Editora C", 10, 19.90)
adicionar_livro("Livro 04", "Gênero B", "Subgênero B.1", "Editora D", 2, 49.90)
adicionar_livro("Livro 05", "Gênero B", "Subgênero B.2", "Editora E", 7, 25.90)
adicionar_livro("Livro 06", "Gênero B", "Subgênero B.2", "Editora F", 1, 15.90)

apresentar_livros()
