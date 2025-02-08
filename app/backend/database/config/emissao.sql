DELETE FROM emissoes;
DELETE FROM sqlite_sequence WHERE name = 'emissoes';

INSERT INTO emissoes (cfop, produto_servico, valor_produto, tributacao_icms, valor_icms, valor_ipi, valor_pis, descontos, observacoes) 
VALUES
(5102, 'Venda de cadeiras', 250.00, 'ICMS 18%', 45.00, 12.50, 5.00, 10.00, 'Entrega em 5 dias úteis'),
(6102, 'Venda de mesas', 600.00, 'ICMS 12%', 72.00, 25.00, 8.00, 20.00, 'Frete incluso'),
(1102, 'Compra de matéria-prima', 450.00, 'ICMS 7%', 31.50, 18.00, 6.50, 15.00, 'Compra realizada para produção de móveis'),
(2102, 'Compra de equipamentos', 1200.00, 'ICMS 4%', 48.00, 36.00, 12.00, 30.00, 'Equipamentos adquiridos de outro estado'),
(5101, 'Prestação de serviços de instalação', 800.00, 'ICMS 5%', 40.00, 0.00, 8.00, 0.00, 'Serviço realizado no cliente final'),
(6101, 'Venda de luminárias', 320.00, 'ICMS 18%', 57.60, 16.00, 6.40, 10.00, 'Entrega para outro estado'),
(1101, 'Compra de insumos', 200.00, 'ICMS 7%', 14.00, 8.00, 3.00, 5.00, 'Insumos para linha de produção'),
(2101, 'Compra de ferramentas', 750.00, 'ICMS 4%', 30.00, 22.50, 7.50, 10.00, 'Adquirido de fornecedor em outro estado'),
(5103, 'Venda de acessórios', 100.00, 'ICMS 18%', 18.00, 5.00, 2.00, 0.00, 'Acessórios para acabamento'),
(6103, 'Venda de aparelhos eletrônicos', 1500.00, 'ICMS 12%', 180.00, 50.00, 15.00, 50.00, 'Venda com garantia estendida de 1 ano');
