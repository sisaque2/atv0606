class FilmeService:
    def __init__(self, repository):
        self.repository = repository

    def cadastrar_filme(self, titulo, genero, duracao, diretor):
        if not titulo or not genero or not diretor:
            raise ValueError("Título, gênero e diretor são obrigatórios.")
        
        if not isinstance(duracao, int) or duracao <= 0:
            raise ValueError("A duração deve ser um número inteiro positivo em minutos.")

        self.repository.salvar(titulo, genero, duracao, diretor)

    def listar_todos_filmes(self):
        return self.repository.buscar_todos()