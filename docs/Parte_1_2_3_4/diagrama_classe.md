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

<img width="270" height="324" alt="image" src="https://github.com/user-attachments/assets/fb237c08-1a76-4709-a8ea-b3ec028cf2bf" />
