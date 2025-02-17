-- DROP TABLE usuarios;
-- DROP TABLE arquivos;
-- DROP TABLE terceiros;
DROP TABLE lancamentos;

CREATE TABLE IF NOT EXISTS usuarios (
                        id_usuario INTEGER PRIMARY KEY AUTOINCREMENT,
                        nome TEXT NOT NULL,
                        email TEXT NOT NULL,
                        login TEXT NOT NULL UNIQUE,
                        senha INTERGER NOT NULL,
                        adm INTEGER NOT NULL);

CREATE TABLE IF NOT EXISTS terceiros (
                        id_terceiros INTEGER PRIMARY KEY AUTOINCREMENT,
                        razao TEXT NOT NULL,
                        nome_fantasia TEXT NOT NULL,
                        cpf_cnpj TEXT NOT NULL,
                        email TEXT NOT NULL,
                        telefone INTEGER,
                        categoria TEXT NOT NULL);

CREATE TABLE IF NOT EXISTS lancamentos (
                        id_lancamentos INTEGER PRIMARY KEY AUTOINCREMENT,
                        codigo TEXT NOT NULL UNIQUE,
                        data TEXT NOT NULL,
                        valor_total REAL NOT NULL,
                        valor_pago REAL NOT NULL,
                        impostos REAL NOT NULL,
                        operacao TEXT NOT NULL,
                        emitente TEXT NOT NULL,
                        tipo_operacao TEXT NOT NULL,
                        banco TEXT NOT NULL,
                        descricao TEXT);

CREATE TABLE IF NOT EXISTS arquivos (
                        id_arquivo INTEGER NOT NULL,
                        nome_arquivo TEXT NOT NULL,
                        arquivo BLOB NOT NULL,
                        FOREIGN KEY (id_arquivo) REFERENCES usuarios(id_usuario));



