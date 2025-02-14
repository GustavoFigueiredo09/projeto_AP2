from datetime import datetime

if __name__ == '__main__':
    from mainCRUD import BaseCRUD
else:
    from .mainCRUD import BaseCRUD

class Lancamento(BaseCRUD):

    def __init__(self, database='app/backend/database/database.db'):
        super().__init__('lancamentos', database)

    def busca_por_emitente(self, emitente, info_tipo='*'):
        return super().read(filtro=f'emitente LIKE "%{emitente}%"', info=info_tipo)
    
    def busca_por_entrada(self, info_tipo='*'):
        return super().read(filtro=f'operacao = "entrada"', info=info_tipo)
    
    def busca_por_saida(self, info_tipo='*'):
        return super().read(filtro=f'operacao = "saida"', info=info_tipo)

    def remove_por_codigo(self, codigo):
        super().delete(filtro=f'codigo = "{codigo}"')


    def busca_soma_entradas(self):
        comando = f"""  SELECT 
                            strftime('%Y-%m', data) AS mes,
                            SUM(valor_pago) AS total_entrada
                        FROM lancamentos
                        WHERE tipo_operacao = "entrada"
                        GROUP BY mes
                        ORDER BY mes"""

        return super().custom_command(comando=comando)
    
    def busca_soma_saidas(self):

        comando = f"""  SELECT 
                            strftime('%Y-%m', data) AS mes,
                            SUM(valor_pago) AS total_saida
                        FROM lancamentos
                        WHERE tipo_operacao = "saida"
                        GROUP BY mes
                        ORDER BY mes"""

        return super().custom_command(comando=comando)
    
    def busca_soma_impostos(self):

        comando = f"""  SELECT 
                            strftime('%Y-%m', data) AS mes,
                            SUM(impostos) AS total_imposto
                        FROM lancamentos
                        WHERE tipo_operacao = "saida"
                        GROUP BY mes
                        ORDER BY mes"""

        return super().custom_command(comando=comando)
    
    def busca_ganho_total(self):

        comando = f"""SELECT 
                            strftime('%Y-%m', data) AS mes,
                            SUM(CASE WHEN tipo_operacao = "entrada" THEN valor_pago ELSE 0 END) - 
                            SUM(CASE WHEN tipo_operacao = "saida" THEN valor_pago + impostos ELSE 0 END)  AS saldo_mensal
                            FROM lancamentos
                            GROUP BY mes
                            ORDER BY mes;"""

        return super().custom_command(comando=comando)

if __name__ == '__main__':
    b = Lancamento()
    # print(b.busca_por_emitente('Robson'))
    # print(b.busca_por_entrada())
    print(b.busca_soma_entradas())
    # print(b.busca_soma_saidas())
    # print(b.busca_soma_impostos())
    # print(b.busca_ganho_total())
    # b.remove_por_codigo(1234567)