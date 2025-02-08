if __name__ == '__main__':
    from mainCRUD import BaseCRUD
else:
    from .mainCRUD import BaseCRUD


class Emissoes(BaseCRUD):

    def __init__(self):
        super().__init__(tabela='emissoes')

    
    def busca_por_cfop(self, cfop, info_tipo='*'):
        return super().read(info=info_tipo, filtro=f'cfop = {cfop}')
    
    def busca_por_valor_prod(self, valor):
        return super().read(filtro=f'valor_produto = {valor}')
    
    # Deem olhada no tipo de retorno antes de usar
    def busca_por_produtos_caros(self, info_tipo='*'):
        return super().custom_command(comando=f'SELECT {info_tipo} FROM emissoes ORDER BY valor_produto DESC LIMIT 10;')
    
    def busca_por_descontos(self, desconto):
        return super().read(filtro=f'descontos = {desconto}')
    
    def busca_por_produto_servico(self, produto_servico):
        return super().read(filtro=f'produto_servico LIKE "%{produto_servico}%"')


if __name__ == '__main__':
    emissao = Emissoes()

    print(emissao.busca_por_cfop(5102))
    print(emissao.busca_por_valor_prod(250))
    print(emissao.busca_por_produtos_caros(info_tipo='valor_produto'))
    print(emissao.busca_por_produto_servico('Venda de cadeiras'))