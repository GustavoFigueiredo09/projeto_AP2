if __name__ == '__main__':
    from mainCRUD import BaseCRUD
else:
    from .mainCRUD import BaseCRUD

class lancamento(BaseCRUD):

    def __init__(self, database='app/backend/database/database.db'):
        super().__init__('lancamentos', database)

    def busca_por_emitente(self, emitendte):
        return super().read(filtro=emitendte)