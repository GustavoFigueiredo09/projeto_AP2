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


    def create(self, dados_dict):

        data_original = dados_dict['data']
        data_formatada = datetime.strptime(data_original, "%d-%m-%Y").strftime("%Y-%m-%d")

        dados_dict['data'] = data_formatada
        return super().create(dados_dict)

if __name__ == '__main__':
    b = Lancamento()
    print(b.busca_por_emitente('Robson'))
    print(b.busca_por_entrada())