from mainCRUD import BaseCRUD

class Usuario(BaseCRUD):

    def __init__(self):
        super().__init__('usuarios')
    
    def busca_todos(self):
        return super().read()
    
    def busca_por_admins(self, info='*'):
        return super().read(filtro='admin = 1')
    
    def busca_por_users(self, info='*'):
        return super().read(info=info, filtro='admin = 0')
    
    def busca_por_nome(self, nome, info='*'):
        return super().read(filtro=f'nome = {nome}')
    
    def busca_por_senha(self, senha, info='*'):
        return super().read(filtro=f'senha = {senha}')

usuario = Usuario()
