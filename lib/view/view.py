class FilmeView:
    def __init__(self, controller):
        self.controller = controller

    def menu(self):
        while True:
            print("\n" + "="*30)
            print(" SISTEMA REDE DE CINEMAS ")
            print("="*30)
            print("1. Cadastrar novo filme")
            print("2. Listar filmes em cartaz")
            print("3. Sair")
            opcao = input("\nEscolha uma opção: ")

            if opcao == '1':
                self.solicita_cadastro()
            elif opcao == '2':
                self.exibe_lista()
            elif opcao == '3':
                print("Encerrando o sistema...")
                break
            else:
                print("Opção inválida! Tente novamente.")

    def solicita_cadastro(self):
        print("\n--- Novo Cadastro de Filme ---")
        titulo = input("Título: ")
        genero = input("Gênero: ")
        try:
            duracao = int(input("Duração (minutos): "))
        except ValueError:
            duracao = 0 
        diretor = input("Diretor: ")

        resposta = self.controller.adicionar_filme(titulo, genero, duracao, diretor)
        
        if resposta.get("sucesso"):
            print(f"\n[OK] {resposta['mensagem']}")
        else:
            print(f"\n[ERRO] {resposta['erro']}")

    def exibe_lista(self):
        print("\n--- Filmes Cadastrados ---")
        resposta = self.controller.listar_filmes()
        
        if resposta.get("sucesso"):
            filmes = resposta["dados"]
            if not filmes:
                print("Nenhum filme cadastrado no momento.")
            else:
                for f in filmes:
                    print(f"[{f['id']}] {f['titulo']} ({f['genero']}) - {f['duracao']} min | Dir: {f['diretor']}")
        else:
            print(f"\n[ERRO] Falha ao buscar filmes: {resposta['erro']}")