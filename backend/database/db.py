import sqlite3 as sq3


# Add Try Except depois
def banco_inicializador():
    # Inicialização
    conn = sq3.connect('backend/database/database.db')
    cursor = conn.cursor()
    conn.execute('PRAGMA foreign_keys = ON;')       # Habilita chaves estrangeiras

    # obs.: SQLite3 não possui datatype booleano, melhor fazer com 0 ou 1

    # Tabela usuarios
    cursor.execute(''' 
    CREATE TABLE IF NOT EXISTS users (
                id_usuario INTEGER PRIMARY KEY AUTOINCREMENT,
                id_arquivos INTEGER,
                usuario TEXT NOT NULL,
                admin INTEGER NOT NULL); 
                ''')
    
    # Tabela arquivos
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS files (
                id_arquivo INTEGER NOT NULL,
                arquivo BLOB NOT NULL,
                FOREIGN KEY (id_arquivo) REFERENCES users(id_arquivos));'''
                   )
    conn.close()



# Só para testes, chamar função na inicialização
if __name__ == '__main__':
    banco_inicializador()