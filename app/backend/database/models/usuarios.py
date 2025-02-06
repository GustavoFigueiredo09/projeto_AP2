if __name__ == '__main__':
    from mainCRUD import BaseCRUD
else:
    from .mainCRUD import BaseCRUD

class Usuario(BaseCRUD):

    def __init__(self):
        super().__init__('usuarios')
    
    def busca_todos(self):
        return super().read()
    
    def busca_por_admins(self, info_tipo='*'):
        return super().read(filtro='admin = 1', info=info_tipo)
    
    def busca_por_users(self, info_tipo='*'):
        return super().read(filtro='admin = 0', info=info_tipo)
    
    def busca_por_nome(self, nome, info_tipo='*'):
        return super().read(filtro=f'nome LIKE "%{nome}%"', info=info_tipo)
    
    def busca_por_senha(self, senha, info_tipo='*'):
        return super().read(filtro=f'senha = {senha}', info=info_tipo)
    
    def buscar_login_e_senha(self, login, senha):
        return super().read(filtro=f'login = "{login}" AND senha = {senha}')
    
    def registra_usuarios(self, dados_dict):
        super().create(dados_dict)
        
    def registra_multiplos_usuarios(self, usuarios):
        for usuario in usuarios:
            super().create(usuario)
          
    # OBS.: TODOS os metodos retornam uma lista com dicionarios ex: [{maria, 12, 55, admin}, {carlos, 23, 44, user}, ...]

if __name__ == '__main__':
    # Exemplo de Uso, basta colocar o login e senha
    usuario = Usuario()
    usuario.create({
    "nome": "Joãof",
    "email": "joao.va@email.com",
    "login": "joao.si34",
    "senha": 8625,
    "adm": 1},
)