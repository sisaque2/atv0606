
@startuml
title Processo: Cadastrar nova sessão
start

:Selecionar Unidade de Cinema;
:Selecionar Filme em Cartaz;
:Definir Sala e Horário;
:Validar Disponibilidade (RN01);

if (Horário Disponível?) then (Sim)
    :Confirmar Agendamento;
    :Salvar Sessão no Sistema;
    stop
else (Não)
    :Exibir Alerta de Conflito;
    end
endif
@enduml

<img width="392" height="491" alt="image" src="https://github.com/user-attachments/assets/13be8749-86b9-4575-8430-aef70006f285" />

---

@startuml
title Processo: Registrar público da sessão
start

:Listar Sessões do Dia;
:Selecionar Sessão Realizada;
:Inserir Quantidade de Espectadores;
:Validar Capacidade da Sala (RN02);

if (Público Válido?) then (Sim)
    :Atualizar Registro de Público;
    :Persistir Dados (SQLite);
    stop
else (Não)
    :Notificar Erro de Capacidade;
    end
endif
@enduml

<img width="440" height="491" alt="image" src="https://github.com/user-attachments/assets/56c85f72-bb5d-4871-8408-7c6bdd39847e" />
