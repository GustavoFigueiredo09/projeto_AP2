DELETE FROM lancamentos;
DELETE FROM sqlite_sequence WHERE name = 'lancamentos';

INSERT INTO lancamentos (codigo, data, valor_total, valor_pago, impostos, tipo_operacao, emitente, operacao, banco, descricao) 
VALUES
('43210512345678000123550010000000012345678901', '2025-04-12', 52.00, 52.00, 2.60, 'entrada', 'Robson Souza', 'Compra de matéria-prima', 'PicPay', 'Compra de mesas de café para o refeitório'),
('43210598765432000123550020000000023456789012', '2025-04-15', 120.50, 120.50, 6.02, 'entrada', 'Maria Oliveira', 'Venda de produto', 'Nubank', 'Venda de cadeiras para escritório'),
('43210545678901000123550030000000034567890123', '2025-04-18', 300.00, 200.00, 15.00, 'saida', 'João Pereira', 'Pagamento de fornecedor', 'Bradesco', 'Pagamento parcial de insumos'),
('43210578901234000123550040000000045678901234', '2025-04-20', 75.00, 75.00, 3.75, 'entrada', 'Ana Costa', 'Venda de produto', 'Itaú', 'Venda de luminárias de LED'),
('43210532165498000123550050000000056789012345', '2025-04-22', 500.00, 500.00, 25.00, 'saida', 'Carlos Mendes', 'Compra de equipamentos', 'Santander', 'Compra de um novo computador'),
('43210515975368000123550060000000067890123456', '2025-04-25', 450.00, 450.00, 22.50, 'entrada', 'Luciana Ribeiro', 'Venda de serviço', 'Inter', 'Manutenção de sistemas elétricos'),
('43210585274196000123550070000000078901234567', '2025-04-28', 200.00, 200.00, 10.00, 'saida', 'Pedro Santos', 'Pagamento de aluguel', 'Caixa', 'Pagamento do aluguel da loja'),
('43210535795148000123550090000000089012345678', '2025-05-02', 600.00, 600.00, 30.00, 'entrada', 'Marcos Vinícius', 'Venda de produto', 'BTG', 'Venda de mesas de madeira'),
('43210565485237000123550100000000090123456789', '2025-05-05', 350.00, 350.00, 17.50, 'saida', 'Juliana Fernandes', 'Pagamento de funcionários', 'Neon', 'Pagamento do salário dos funcionários'),
('123456', '2025-04-30', 100.00, 50.00, 5.00, 'saida', 'Fernanda Lima', 'Compra de material de escritório', 'Original', 'Compra de papel e canetas');
