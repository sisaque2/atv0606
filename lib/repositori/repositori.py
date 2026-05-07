import sqlite3

class FilmeRepository:
    def __init__(self, db_name="cinema.db"):
        self.db_name = db_name

    def conectar(self):
        return sqlite3.connect(self.db_name)

    def criar_tabela(self):
        conexao = self.conectar()
        cursor = conexao.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS filmes (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                titulo TEXT NOT NULL,
                genero TEXT NOT NULL,
                duracao INTEGER NOT NULL,
                diretor TEXT NOT NULL
            )
        ''')
        conexao.commit()
        conexao.close()

    def salvar(self, titulo, genero, duracao, diretor):
        conexao = self.conectar()
        cursor = conexao.cursor()
        cursor.execute('''
            INSERT INTO filmes (titulo, genero, duracao, diretor)
            VALUES (?, ?, ?, ?)
        ''', (titulo, genero, duracao, diretor))
        conexao.commit()
        conexao.close()

    def buscar_todos(self):
        conexao = self.conectar()
        conexao.row_factory = sqlite3.Row 
        cursor = conexao.cursor()
        cursor.execute("SELECT * FROM filmes")
        linhas = cursor.fetchall()
        conexao.close()
        
        return [dict(linha) for linha in linhas]