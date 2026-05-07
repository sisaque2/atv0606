@startuml
autonumber
skinparam maxMessageSize 150

actor "Funcionário" as Funcionario
boundary "SessaoView" as View
control "SessaoController" as Controller
entity "SessaoService" as Service
database "SessaoRepository" as Repository

Funcionario -> View : Solicita cadastro de Sessão (filme, sala, horário)
activate View

View -> Controller : cadastrarSessao(dadosSessao)
activate Controller

Controller -> Service : validarECriarSessao(dadosSessao)
activate Service

Service -> Service : Validar disponibilidade e intervalo

Service -> Repository : salvar(sessao)
activate Repository

Repository --> Service : Sessão salva com sucesso
deactivate Repository

Service --> Controller : Retorna status (Sucesso)
deactivate Service

Controller --> View : Atualiza interface
deactivate Controller

View --> Funcionario : Exibe mensagem de sucesso
deactivate View
@enduml

<img width="1005" height="548" alt="image" src="https://github.com/user-attachments/assets/4c6a5666-0a17-484b-801d-84ea21d9f6b0" />
