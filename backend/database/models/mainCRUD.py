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

    def __init__(self, tabela, database='backend\database\database.db'): # Também tem o att database, que já tem um diretório padrão.
        self.tabela = tabela
        self.database = database
        
    def _conectar(self):
        conn = sq3.connect('backend\database\database.db')
        conn.execute('PRAGMA foreign_keys = ON;')
        return conn

    def create(self, dados_dict):                                            # Registro deve receber os valores a serem digitados em DICT
        colunas = ', '.join(dados_dict.keys())
        valores = ', '.join('?' for i in dados_dict)
        with self._conectar as conn:
            cursor = conn.cursor()
            cursor.execute(f'INSERT INTO {self.tabela} ({colunas}) VALUES ({valores})')
    
    def read(self, filtro=None):                                            # Se quiser todos os dados da tabela, deixe o filtro vazio.
        comando_sql = f'SELECT * FROM {self.tabela}'

        if filtro:
            sql = f'WHERE {filtro}'

        with self._conectar as conn:
            cursor = conn.cursor()
            cursor.execute(comando_sql, sql)
            return cursor.fetchall()

            
    def update(self):
        ...
        
    def delete(self):
        ...

