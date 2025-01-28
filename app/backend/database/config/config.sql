CREATE TABLE IF NOT EXISTS usuarios (
                        id_usuario INTEGER PRIMARY KEY AUTOINCREMENT,
                        id_arquivos INTEGER,
                        nome TEXT NOT NULL,
                        email TEXT NOT NULL,
                        login TEXT NOT NULL,
                        senha INTERGER NOT NULL,
                        admin INTEGER NOT NULL);

CREATE TABLE IF NOT EXISTS terceiros (
                        id_terceiros INTEGER PRIMARY KEY AUTOINCREMENT,
                        razao TEXT NOT NULL,
                        nome_fantasia TEXT NOT NULL,
                        cpf_cpnj TEXT NOT NULL,
                        email TEXT NOT NULL,
                        telefone INTEGER,
                        categoria TEXT NOT NULL);

CREATE TABLE IF NOT EXISTS lancamentos (
                        id_lancamentos INTEGER PRIMARY KEY AUTOINCREMENT,
                        data TEXT NOT NULL,
                        valor_total REAL NOT NULL,
                        valor_pago REAL NOT NULL,
                        operacao TEXT NOT NULL,
                        emitente INTEGER,
                        tipo_operacao TEXT NOT NULL,
                        descricao TEXT);

CREATE TABLE IF NOT EXISTS arquivos (
                        id_arquivo INTEGER NOT NULL,
                        nome_arquivo TEXT NOT NULL,
                        arquivo BLOB NOT NULL,
                        FOREIGN KEY (id_arquivo) REFERENCES usuarios(id_arquivos));