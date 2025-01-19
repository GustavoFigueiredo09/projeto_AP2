from mainCRUD import BaseCRUD
import os


class Arquivo(BaseCRUD):

    def __init__(self):
        super().__init__(tabela='arquivos')
    

    def create(self, usuario_nome, arquivo_path):

        # Comando customizado para pegar o ID arquivo do cliente
        comando = f'SELECT id_arquivos FROM usuarios WHERE nome LIKE ?'
        tupla_nome = (usuario_nome,)

        id_arquivo = self.custom_command(comando, parametros=tupla_nome)
        nome_arquivo = os.path.basename(arquivo_path)
        print(nome_arquivo)

        with open(arquivo_path, "rb") as arquivo:
            arquivo_blob = arquivo.read()

        dados_dict = {'id_arquivo': id_arquivo[0][0], 'nome_arquivo': nome_arquivo, 'arquivo': arquivo_blob}
        return super().create(dados_dict)
        

    def arquivos_por_usuario(self, nome):
        ...