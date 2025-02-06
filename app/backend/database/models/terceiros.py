if __name__ == '__main__':
    from mainCRUD import BaseCRUD
else:
    from .mainCRUD import BaseCRUD

class terceiros(BaseCRUD):

    def __init__(self):
        super().__init__(tabela='terceiros')

    def busca_por_cpf_cnpj(self, cpf, info_tipo='*'):
        return super().read(filtro=cpf, info=info_tipo)
    
    def busca_por_cliente(self, categoria, info_tipo='*'):
        return super().read(filtro=categoria, info=info_tipo)
    
    def busca_por_telefone(self, fone, info_tipo='*'):
        return super().read(filtro=fone, info=info_tipo)
    
    
