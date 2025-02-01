import sqlite3 as sq3

# OBS.: Classe so deve ser chamada na inicialização ou na falta/erro de tabelas

class BancoInicializador:
    # Inicialização
    def __init__(self, databasepath):
        self.database_path = databasepath

    def _conectar(self):
        conn = sq3.connect('app/backend/database/database.db')
        conn.execute('PRAGMA foreign_keys = OFF;')
        return conn
    

    def inicializador(self):                                    
        try:
            
            sql_file_path = 'app/backend/database/config/config.sql'
            with open(sql_file_path, 'r', encoding='utf-8') as file:
                sql_script = file.read()

            with self._conectar() as conn:
                cursor = conn.cursor()
                cursor.executescript(sql_script)

            print('Banco Inicializado com sucesso!')

        except sq3.Error as e:
            print(f'Log: falha ao gerar banco: {e}')
            return f'Log: falha ao gerar banco: {e}'

    def limpa_usuarios(self):


        sql_file_path = 'app/backend/database/config/users.sql'
        with open(sql_file_path, 'r', encoding='utf-8') as file:
            sql_script = file.read()

        with self._conectar() as conn:
            cursor = conn.cursor()
            cursor.executescript(sql_script)
            

# Só para testes, chamar função na inicialização
if __name__ == '__main__':
    inicio = BancoInicializador('backend\database\database.db')
    inicio.inicializador()
    # inicio.limpa_usuarios()