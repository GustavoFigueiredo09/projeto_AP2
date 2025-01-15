import sqlite3 as sq3


def banco_inicializador():
    # Inicialização
    conn = sq3.connect('backend/database/database.db')
    cursor = conn.cursor()
    conn.execute('PRAGMA foreign_keys = ON;')       # Habilita chaves estrangeiras

    try:
        # Tabela usuarios
        cursor.execute(''' 
        CREATE TABLE IF NOT EXISTS usuarios (
                    id_usuario INTEGER PRIMARY KEY AUTOINCREMENT,
                    id_arquivos INTEGER,
                    nome TEXT NOT NULL,
                    email TEXT NOT NULL,
                    login TEXT NOT NULL,
                    senha INTERGER NOT NULL,
                    admin INTEGER NOT NULL); ''')
        
        # Tabela Terceiros
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS terceiros (
                    id_terceiros INTEGER PRIMARY KEY AUTOINCREMENT,
                    razao TEXT NOT NULL,
                    nome_fantasia TEXT NOT NULL,
                    cpf_cpnj TEXT NOT NULL,
                    email TEXT NOT NULL,
                    telefone INTEGER,
                    categoria TEXT NOT NULL);''')

        # Tabela Lançamentos
        # OBS.: Explicar um pocuo melhor sobre quem o emitente vai referenciar
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS lancamentos (
                    id_lancamentos INTEGER PRIMARY KEY AUTOINCREMENT,
                    data TEXT NOT NULL,
                    valor_total REAL NOT NULL,
                    valor_pago REAL NOT NULL,
                    operacao TEXT NOT NULL,
                    emitente INTEGER,
                    tipo_operacao TEXT NOT NULL,
                    descricao TEXT);''')

        # Tabela arquivos
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS arquivos (
                    id_arquivo INTEGER NOT NULL,
                    arquivo BLOB NOT NULL,
                    FOREIGN KEY (id_arquivo) REFERENCES users(id_arquivos));''')

    except Exception as e:
        print(f'Log: falha ao gerar tabela usuarios: {e}')
        conn.close()
        return f'Log: falha ao gerar tabela usuarios: {e}'
    
    conn.close()

# Só para testes, chamar função na inicialização
if __name__ == '__main__':
    banco_inicializador()