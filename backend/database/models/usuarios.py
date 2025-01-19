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
    
    def buscar_login_e_senha(self, login, senha):
        return super().read(filtro=f'login = "{login}" AND senha = {senha}')

if __name__ == '__main__':
    # Exemplo de Uso, basta colocar o login e senha
    usuario = Usuario()
    dados_dict = usuario.buscar_login_e_senha('maria.carla53', 26820)
    print(dados_dict)
