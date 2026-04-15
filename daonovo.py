import sqlite3
from modelo import Gutin

class GutinDAO:
    def __init__(self, nome_banco = "banco_gutin.db"):
        self.nome_banco = nome_banco
        self._criar_tabela_se_nao_existe()

    def _conectar(self):
        return sqlite3.connect(self.nome_banco)

    def _criar_tabela_se_nao_existe(self):
        with self._conectar() as conexao:
            cursor = conexao.cursor()
            cursor.execute(
                '''
                CREATE TABLE IF NOT EXISTS gutinhos(
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    sabor TEXT NOT NULL,
                    localidade TEXT NOT NULL,
                    marca TEXT NOT NULL,
                    vendedor TEXT NOT NULL
                )
                '''
            )
            conexao.commit()

    def inserir(self, gutin):
        with self._conectar() as conexao:
            cursor = conexao.cursor()
            cursor.execute(
                '''
                INSERT INTO gutinhos(sabor, localidade, marca, vendedor)
                VALUES(?, ?, ?, ?)
                ''', (gutin.sabor, gutin.localidade, gutin.marca, gutin.vendedor)
            )
            conexao.commit()
            print(f"[OK] gutin de '{gutin.sabor}' inserido com sucesso.")

    def buscar_todos(self):
        with self._conectar() as conexao:
            cursor = conexao.cursor()
            cursor.execute('SELECT id, sabor, localidade, marca, vendedor FROM gutinhos')
            linhas = cursor.fetchall()
             

            lista_gutinhos =[]
            for linha in linhas:
                gutin = Gutin(id_gutin = linha[0], sabor = linha[1], localidade = linha[2], marca = linha[3], vendedor = linha[4])
                lista_gutinhos.append(gutin)

            return lista_gutinhos


    def atualizar(self,gutin):
        with self._conectar() as conexao:
            print(gutin)
            cursor = conexao.cursor()
            cursor.execute(
                '''
                UPDATE gutinhos
                SET sabor = ?, localidade = ?, marca = ?, vendedor = ?
                WHERE id = ?
                ''', (gutin.sabor, gutin.localidade, gutin.marca, gutin.vendedor, gutin.id_gutin)
            )
            conexao.commit()
            print(f"[OK] gutin de '{gutin.sabor}' trocado com sucesso.")


    def comer(self, id_gutin):
        with self._conectar() as conexao:
            cursor = conexao.cursor()
            cursor.execute('DELETE FROM gutinhos WHERE id = ?', (id_gutin,))
            conexao.commit()
            print(f"[OK] Gutin de  id '{id_gutin}' comido com sucesso.")                 
