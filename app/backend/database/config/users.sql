DELETE FROM usuarios;
DELETE FROM sqlite_sequence WHERE name = 'usuarios';


INSERT INTO usuarios (nome, email, login, senha, adm) VALUES ('João Silva', 'joao.silva@email.com', 'joao.silva34', 873194625, 1);
INSERT INTO usuarios (nome, email, login, senha, adm) VALUES ('Maria Oliveira', 'maria.oliveira@email.com', 'maria.oliveira67', 453216789, 0);
INSERT INTO usuarios (nome, email, login, senha, adm) VALUES ('Carlos Pereira', 'carlos.pereira@email.com', 'carlos.pereira89', 192874536, 1);
INSERT INTO usuarios (nome, email, login, senha, adm) VALUES ('Ana Costa', 'ana.costa@email.com', 'ana.costa45', 687543219, 0);
INSERT INTO usuarios (nome, email, login, senha, adm) VALUES ('Felipe Santos', 'felipe.santos@email.com', 'felipe.santos23', 947162835, 1);
INSERT INTO usuarios (nome, email, login, senha, adm) VALUES ('Julia Rodrigues', 'julia.rodrigues@email.com', 'julia.rodrigues78', 381475692, 0);
INSERT INTO usuarios (nome, email, login, senha, adm) VALUES ('Pedro Almeida', 'pedro.almeida@email.com', 'pedro.almeida12', 528193746, 1);
INSERT INTO usuarios (nome, email, login, senha, adm) VALUES ('Fernanda Lima', 'fernanda.lima@email.com', 'fernanda.lima56', 762894315, 0);
INSERT INTO usuarios (nome, email, login, senha, adm) VALUES ('Ricardo Souza', 'ricardo.souza@email.com', 'ricardo.souza92', 319682547, 1);
INSERT INTO usuarios (nome, email, login, senha, adm) VALUES ('Larissa Martins', 'larissa.martins@email.com', 'larissa.martins34', 874513926, 0);

INSERT INTO usuarios (nome, email, login, senha, adm) VALUES ('Administrador', 'adm@cactus.fiscal.br', 'admin', 1234, 1);
INSERT INTO usuarios (nome, email, login, senha, adm) VALUES ('Usuário', 'usuario@cactus.fiscal.br', 'user', 1234, 0);
