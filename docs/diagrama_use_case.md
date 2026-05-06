@startuml
left to right direction

actor Espectador
actor "Funcionário/Administrador" as Funcionario

rectangle "Sistema Rede de Cinemas" {
  
  Espectador -- (Consultar Filmes e Sessões)
  
  Funcionario -- (Consultar Filmes e Sessões)
  Funcionario -- (Gerenciar Cadastro de Filmes)
  Funcionario -- (Gerenciar Sessões)
  Funcionario -- (Registrar e Consultar Público)

}
@enduml

<img width="509" height="361" alt="image" src="https://github.com/user-attachments/assets/7b3bb460-b5e2-4980-806a-535a10523fa3" />
