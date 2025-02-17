class SessaoUsuario:
    _instance = None # Variável que irá instanciar o usuário logado

    def __new__(cls):
        if cls._instance is None: # cria uma instancia caso não exista uma ainda
            cls._instance = super(SessaoUsuario, cls).__new__(cls)
            cls._instance.usuario = None 
        return cls._instance # retorna a mesma instancia pra qualquer chamada

    def set_usuario(self, usuario):
        self.usuario = usuario # Armamzena os dados do usuário logado

    def get_usuario(self):
        return self.usuario # Retorna os dados do usuário logado