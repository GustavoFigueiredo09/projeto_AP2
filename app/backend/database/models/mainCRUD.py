import _sqlite3 as sq3 

class BaseCRUD:

    def __init__(self, tabela, database='app/backend/database/database.db'): 
        self.tabela = tabela
        self.database = database
    
    # Inicia Conexão
    def _conectar(self):
        conn = sq3.connect(self.database)
        conn.execute('PRAGMA foreign_keys = OFF;')
        return conn

    # Insere Dados
    def create(self, dados_dict):
        colunas = ', '.join(dados_dict.keys())
        valores = ', '.join(['?' for i in dados_dict])
        with self._conectar() as conn:
            cursor = conn.cursor()
            cursor.execute(f'INSERT INTO {self.tabela} ({colunas}) VALUES ({valores})', tuple(dados_dict.values()))

    # Lê dados
    def read(self, info='*', filtro=None):  # Se quiser todos os dados da tabela, deixe info e filtro vazio
        comando_sql = f'SELECT {info} FROM {self.tabela} '
        if filtro:
            comando_sql += f'WHERE {filtro}'
        try:
            with self._conectar() as conn:
                cursor = conn.cursor()
                cursor.execute(comando_sql)
                retorno = cursor.fetchall()

                colunas = [desc[0] for desc in cursor.description]
                dados_formatados = [dict(zip(colunas, linha)) for linha in retorno]

                return dados_formatados
        except Exception as e:
            print(f'Erro no método read: {e}')
            return None  # Retorna lista vazia em caso de erro

    # Atualiza
    def update(self, dados_dict, filtro):
        atualizacoes = ', '.join([f'{coluna} = ?' for coluna in dados_dict])
        comando_sql = f'UPDATE {self.tabela} SET {atualizacoes} WHERE {filtro}'

        with self._conectar() as conn:
            cursor = conn.cursor()
            cursor.execute(comando_sql, tuple(dados_dict.values()))
            conn.commit()
            return cursor.rowcount
    
    # Apaga
    def delete(self, filtro):
        comando_sql = f'DELETE FROM {self.tabela} WHERE {filtro}'
        with self._conectar() as conn:
            cursor = conn.cursor()
            cursor.execute(comando_sql)
            conn.commit()

    # Comando customizado para demais tarefas
    def custom_command(self, comando, parametros=None):
        with self._conectar() as conn:
            cursor = conn.cursor()
            cursor.execute(comando, parametros or ())
        if comando.strip().upper().startswith("SELECT"):
            return cursor.fetchall()
        else:
            conn.commit()
            return None

if __name__ == '__main__':

    # Exemplo de uso: 

    class usuarios(BaseCRUD):
        def __init__(self, tabela):
            super().__init__(tabela)
    
    # Criar quaisquer dados desejar para facilitar manipulação da tabela especifica.

    usuario = usuarios('usuarios')
    
    usuario.create({'id_arquivos': 1, 
                     'nome': 'Carlos', 
                     'email': 'carlosmaia@gmail.com', 
                     'login': 'carlos.maia05',
                     'senha': 1235,
                     'admin': 1})


    retorno = usuario.read()
    '''

     Retorno:  [{'coluna1': #, 'coluna2': #},
                {'coluna1': #, 'coluna2': #}]
    '''
    for val in retorno:
        print(val)
    
    usuario.update({'id_arquivos': 3, 
                     'nome': 'Maria', 
                     'email': 'mariaCarla@hotmail.com', 
                     'login': 'maria.carla53',
                     'senha': 26820,
                     'admin': 0}, 'id_usuario = 2')

    usuario.delete('id_usuario = 1')