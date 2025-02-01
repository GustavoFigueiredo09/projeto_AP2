if __name__ == '__main__':
    from mainCRUD import BaseCRUD
else:
    from .mainCRUD import BaseCRUD

class Lancamento(BaseCRUD):

    def __init__(self, database='app/backend/database/database.db'):
        super().__init__('lancamentos', database)

    def busca_por_emitente(self, emitente):
        return super().read(filtro=f'emitente LIKE "%{emitente}%"')
    
    def busca_por_entrada(self):
        return super().read(filtro=f'operacao = "entrada"')


if __name__ == '__main__':
    b = Lancamento()
    print(b.busca_por_emitente('Robson'))
    print(b.busca_por_entrada())