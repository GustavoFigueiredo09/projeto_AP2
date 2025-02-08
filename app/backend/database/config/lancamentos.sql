DELETE FROM lancamentos;
DELETE FROM sqlite_sequence WHERE name = 'lancamentos';


INSERT INTO lancamentos (codigo, data, valor_total, valor_pago, impostos, tipo_operacao, emitente, operacao, descricao) 
VALUES (1234567890123, '2025-04-12', 52.00, 52.00, 2.60, 'entrada', 'Robson Souza', 'Compra de matéria-prima', 'Compra de mesas de café para o refeitório');

INSERT INTO lancamentos (codigo, data, valor_total, valor_pago, impostos, tipo_operacao, emitente, operacao, descricao) 
VALUES (1234567890124, '2025-04-15', 120.50, 120.50, 6.02, 'entrada', 'Maria Oliveira', 'Venda de produto', 'Venda de cadeiras para escritório');

INSERT INTO lancamentos (codigo, data, valor_total, valor_pago, impostos, tipo_operacao, emitente, operacao, descricao) 
VALUES (1234567890125, '2025-04-18', 300.00, 200.00, 15.00, 'saida', 'João Pereira', 'Pagamento de fornecedor', 'Pagamento parcial de insumos');

INSERT INTO lancamentos (codigo, data, valor_total, valor_pago, impostos, tipo_operacao, emitente, operacao, descricao) 
VALUES (1234567890126, '2025-04-20', 75.00, 75.00, 3.75, 'entrada', 'Ana Costa', 'Venda de produto', 'Venda de luminárias de LED');

INSERT INTO lancamentos (codigo, data, valor_total, valor_pago, impostos, tipo_operacao, emitente, operacao, descricao) 
VALUES (1234567890127, '2025-04-22', 500.00, 500.00, 25.00, 'saida', 'Carlos Mendes', 'Compra de equipamentos', 'Compra de um novo computador');

INSERT INTO lancamentos (codigo, data, valor_total, valor_pago, impostos, tipo_operacao, emitente, operacao, descricao) 
VALUES (1234567890128, '2025-04-25', 450.00, 450.00, 22.50, 'entrada', 'Luciana Ribeiro', 'Venda de serviço', 'Manutenção de sistemas elétricos');

INSERT INTO lancamentos (codigo, data, valor_total, valor_pago, impostos, tipo_operacao, emitente, operacao, descricao) 
VALUES (1234567890129, '2025-04-28', 200.00, 200.00, 10.00, 'saida', 'Pedro Santos', 'Pagamento de aluguel', 'Pagamento do aluguel da loja');

INSERT INTO lancamentos (codigo, data, valor_total, valor_pago, impostos, tipo_operacao, emitente, operacao, descricao) 
VALUES (1234567890130, '2025-04-30', 100.00, 50.00, 5.00, 'saida', 'Fernanda Lima', 'Compra de material de escritório', 'Compra de papel e canetas');

INSERT INTO lancamentos (codigo, data, valor_total, valor_pago, impostos, tipo_operacao, emitente, operacao, descricao) 
VALUES (1234567890131, '2025-05-02', 600.00, 600.00, 30.00, 'entrada', 'Marcos Vinícius', 'Venda de produto', 'Venda de mesas de madeira');

INSERT INTO lancamentos (codigo, data, valor_total, valor_pago, impostos, tipo_operacao, emitente, operacao, descricao) 
VALUES (1234567890132, '2025-05-05', 350.00, 350.00, 17.50, 'saida', 'Juliana Fernandes', 'Pagamento de funcionários', 'Pagamento do salário dos funcionários');
