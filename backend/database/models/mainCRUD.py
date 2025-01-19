import _sqlite3 as sq3


# COMO USAR PARA CRIAR NOVAS CLASSES
class BaseCRUD:
    # Crie uma nova classe HERDANDO a classe BaseCRUD
    '''
    EX.: 
    class Usuarios(BaseCRUD):
    def __init__(self):
        super().__init__('usuarios')        Essa parte ditará qual tabela será manipulada login/arquivos/etc
                                            
    '''

    def __init__(self, tabela, database='backend/database/database.db'): # Também tem o att database, que já tem um diretório padrão.
        self.tabela = tabela
        self.database = database
        
    def _conectar(self):
        conn = sq3.connect('backend/database/database.db')
        conn.execute('PRAGMA foreign_keys = ON;')
        return conn

    def create(self, dados_dict):                                            # Registro deve receber os valores a serem digitados em DICT
        colunas = ', '.join(dados_dict.keys())
        valores = ', '.join(['?' for i in dados_dict])
              
        with self._conectar() as conn:
            cursor = conn.cursor()
            cursor.execute(f'INSERT INTO {self.tabela} ({colunas}) VALUES ({valores})', tuple(dados_dict.values()))
    
    def read(self, filtro=None):                                            # Se quiser todos os dados da tabela, deixe o filtro vazio.
        comando_sql = f'SELECT * FROM {self.tabela} '

        if filtro:
            comando_sql += f'WHERE {filtro}'

        with self._conectar() as conn:
            cursor = conn.cursor()
            cursor.execute(comando_sql)
            return cursor.fetchall()                                        # Retorno da pesquisa:  [ linha -> (1, coluna -> 'João', 30), (2, 'Maria', 25)]

            
    def update(self, dados_dict, filtro):
        
        atualizacoes = ', '.join([f'{coluna} = ?' for coluna in dados_dict])
        sql = f'UPDATE {self.tabela} SET {atualizacoes} WHERE {filtro}'

        with self._conectar() as conn:
            cursor = conn.cursor()
            cursor.execute(sql, tuple(dados_dict.values()))
            conn.commit()
            return cursor.rowcount                                   

    def delete(self, filtro):

        sql = f'DELETE FROM {self.tabela} WHERE {filtro}'
        print(sql)
        with self._conectar() as conn:
            cursor = conn.cursor()
            cursor.execute(sql)
            conn.commit()




if __name__ == '__main__':

    class usuarios(BaseCRUD):
        def __init__(self, tabela):
            super().__init__(tabela)
    
    usuario = usuarios('usuarios')
    
    usuario.create({'id_arquivos': 1, 
                     'nome': 'Carlos', 
                     'email': 'carlosmaia@gmail.com', 
                     'login': 'carlos.maia05',
                     'senha': 1235,
                     'admin': 1})


    retorno = usuario.read(filtro='email LIKE "%mail.com"')

    for linha in retorno:
        for coluna in linha:
            print(coluna, end=' || ')
        print()    
    
    usuario.update({'id_arquivos': 3, 
                     'nome': 'Maria', 
                     'email': 'mariaCarla@hotmail.com', 
                     'login': 'maria.carla53',
                     'senha': 26820,
                     'admin': 0}, 'id_usuario = 2')

    usuario.delete('id_usuario = 1')