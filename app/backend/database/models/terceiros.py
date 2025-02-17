if __name__ == '__main__':
    from mainCRUD import BaseCRUD
else:
    from .mainCRUD import BaseCRUD

class Terceiros(BaseCRUD):
    def __init__(self):
        super().__init__(tabela='terceiros')

    def buscar_por_nome(self, filtro=None):
        """Busca terceiros filtrando por razão social ou nome fantasia."""
        condicao = f"razao LIKE '%{filtro}%' OR nome_fantasia LIKE '%{filtro}%'" if filtro else None
        return super().read(filtro=condicao)

    def create_terceiro(self, dados):
        """Insere um novo terceiro no banco de dados."""
        try:
            return self.create(dados)
        except Exception as e:
            print(f"Erro ao cadastrar terceiro: {e}")
            return None
