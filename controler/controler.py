class FilmeController:
    def __init__(self, service):
        self.service = service

    def adicionar_filme(self, titulo, genero, duracao, diretor):
        try:
            self.service.cadastrar_filme(titulo, genero, duracao, diretor)
            return {"sucesso": True, "mensagem": "Filme cadastrado com sucesso!"}
        except ValueError as erro:
            return {"sucesso": False, "erro": str(erro)}

    def listar_filmes(self):
        try:
            filmes = self.service.listar_todos_filmes()
            return {"sucesso": True, "dados": filmes}
        except Exception as erro:
            return {"sucesso": False, "erro": str(erro)}