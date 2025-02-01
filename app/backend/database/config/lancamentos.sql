DELETE FROM lancamentos;
DELETE FROM sqlite_sequence WHERE name = 'lancamentos';


INSERT INTO lancamentos (data, valor_total, valor_pago, operacao, emitente, tipo_operacao, descricao) 
VALUES (12042025, 52.00, 52.00, 'entrada', 'Robson Souza', 'Compra de matéria-prima', 'Compra de mesas de café para o refeitório');

INSERT INTO lancamentos (data, valor_total, valor_pago, operacao, emitente, tipo_operacao, descricao) 
VALUES (12042025, 52.00, 52.00, 'entrada', 'Robson Souza', 'Compra de matéria-prima', 'Compra de mesas de café para o refeitório');

INSERT INTO lancamentos (data, valor_total, valor_pago, operacao, emitente, tipo_operacao, descricao) 
VALUES (15042025, 120.50, 120.50, 'entrada', 'Maria Oliveira', 'Venda de produto', 'Venda de cadeiras para escritório');

INSERT INTO lancamentos (data, valor_total, valor_pago, operacao, emitente, tipo_operacao, descricao) 
VALUES (18042025, 300.00, 200.00, 'saida', 'João Pereira', 'Pagamento de fornecedor', 'Pagamento parcial de insumos');

INSERT INTO lancamentos (data, valor_total, valor_pago, operacao, emitente, tipo_operacao, descricao) 
VALUES (20042025, 75.00, 75.00, 'entrada', 'Ana Costa', 'Venda de produto', 'Venda de luminárias de LED');

INSERT INTO lancamentos (data, valor_total, valor_pago, operacao, emitente, tipo_operacao, descricao) 
VALUES (22042025, 500.00, 500.00, 'saida', 'Carlos Mendes', 'Compra de equipamentos', 'Compra de um novo computador');

INSERT INTO lancamentos (data, valor_total, valor_pago, operacao, emitente, tipo_operacao, descricao) 
VALUES (25042025, 450.00, 450.00, 'entrada', 'Luciana Ribeiro', 'Venda de serviço', 'Manutenção de sistemas elétricos');

INSERT INTO lancamentos (data, valor_total, valor_pago, operacao, emitente, tipo_operacao, descricao) 
VALUES (28042025, 200.00, 200.00, 'saida', 'Pedro Santos', 'Pagamento de aluguel', 'Pagamento do aluguel da loja');

INSERT INTO lancamentos (data, valor_total, valor_pago, operacao, emitente, tipo_operacao, descricao) 
VALUES (30042025, 100.00, 50.00, 'saida', 'Fernanda Lima', 'Compra de material de escritório', 'Compra de papel e canetas');
INSERT INTO lancamentos (data, valor_total, valor_pago, operacao, emitente, tipo_operacao, descricao) 
VALUES (02052025, 600.00, 600.00, 'entrada', 'Marcos Vinícius', 'Venda de produto', 'Venda de mesas de madeira');
INSERT INTO lancamentos (data, valor_total, valor_pago, operacao, emitente, tipo_operacao, descricao) 
VALUES (05052025, 350.00, 350.00, 'saida', 'Juliana Fernandes', 'Pagamento de funcionários', 'Pagamento do salário dos funcionários');
