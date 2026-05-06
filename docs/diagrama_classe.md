@startuml
skinparam classAttributeIconSize 0

class Cinema {
    nome
    endereco
    capacidadeTotal
}

class Filme {
    titulo
    genero
    duracao
    diretor
    elenco
}

class Sessao {
    dataHora
    sala
    publicoRegistrado
}

Cinema "1" -- "*" Sessao : possui
Filme "1" -- "*" Sessao : é exibido em
@enduml

