from repositori.repositori import FilmeRepository
from service.service import FilmeService
from controler.controler import FilmeController 
from view.view import FilmeView

def main():
    repository = FilmeRepository()
    repository.criar_tabela()
    
    service = FilmeService(repository)
    controller = FilmeController(service)
    view = FilmeView(controller)

    view.menu()

if __name__ == "__main__":
    main()