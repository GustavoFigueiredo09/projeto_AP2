DELETE FROM terceiros;
DELETE FROM sqlite_sequence WHERE name = 'terceiros';

INSERT INTO terceiros (razao, nome_fantasia, cpf_cnpj, email, telefone, categoria)
VALUES ('João da Silva LTDA', 'JS Transportes', '12345678000195', 'contato@jstransportes.com', 11987654321, 'transportadora');

INSERT INTO terceiros (razao, nome_fantasia, cpf_cnpj, email, telefone, categoria)
VALUES ('Maria e Filhos ME', 'Maria Doces', '98765432000120', 'maria@mariadoce.com', 21976543210, 'cliente');

INSERT INTO terceiros (razao, nome_fantasia, cpf_cnpj, email, telefone, categoria)
VALUES ('Carlos Construções SA', 'Construcarlos', '45678912000130', 'contato@construcarlos.com', 31983456789, 'fornecedor');

INSERT INTO terceiros (razao, nome_fantasia, cpf_cnpj, email, telefone, categoria)
VALUES ('Transportadora Velocidade', 'Velocidade', '11222333000188', 'contato@velocidade.com', 31999887766, 'transportadora');

INSERT INTO terceiros (razao, nome_fantasia, cpf_cnpj, email, telefone, categoria)
VALUES ('Padaria Pão Quente', 'Pão Quente', '77889966000122', 'contato@paoquente.com', 1133224455, 'cliente');

INSERT INTO terceiros (razao, nome_fantasia, cpf_cnpj, email, telefone, categoria)
VALUES ('Fornecedora de Alimentos LTDA', 'ForneceAlimentos', '33445566000177', 'vendas@fornecealimentos.com', 41988776655, 'fornecedor');

INSERT INTO terceiros (razao, nome_fantasia, cpf_cnpj, email, telefone, categoria)
VALUES ('Express Transportes LTDA', 'Express', '66778899000144', 'contato@expresstransportes.com', 21999887744, 'transportadora');

INSERT INTO terceiros (razao, nome_fantasia, cpf_cnpj, email, telefone, categoria)
VALUES ('João dos Pães ME', 'João Pães', '11002233000166', 'contato@joaopaes.com', 31988774455, 'cliente');

INSERT INTO terceiros (razao, nome_fantasia, cpf_cnpj, email, telefone, categoria)
VALUES ('Madeireira Central', 'Central Madeira', '44556677000133', 'vendas@madeireiracentral.com', 42999887766, 'fornecedor');

INSERT INTO terceiros (razao, nome_fantasia, cpf_cnpj, email, telefone, categoria)
VALUES ('Transportes Rápidos', 'Rápido Cargo', '99887766000122', 'atendimento@rapidocargo.com', 11987655443, 'transportadora');
