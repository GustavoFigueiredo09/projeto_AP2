if __name__ == '__main__':
    from mainCRUD import BaseCRUD
else:
    from .mainCRUD import BaseCRUD
    
import os


class Arquivo(BaseCRUD):

    def __init__(self):
        super().__init__(tabela='arquivos')
    
    # Salva arquivo da pasta files no Banco de dados
    # Basta chamar metodo com o login do usuario e o path do arquivo, enviará o arquivo para o database.
    def create(self, usuario_login, nome_do_arquivo):

        # Comando customizado para pegar o ID arquivo do cliente 
        comando = f'SELECT id_arquivos FROM usuarios WHERE login LIKE ?'
        tupla_nome = (usuario_login,)

        id_arquivo = self.custom_command(comando, parametros=tupla_nome)
        caminho_arquivo = os.path.abspath(f'app/backend/files/{nome_do_arquivo}')

        with open(caminho_arquivo, "rb") as arquivo:
            arquivo_blob = arquivo.read()

        dados_dict = {'id_arquivo': id_arquivo[0][0], 'nome_arquivo': nome_do_arquivo, 'arquivo': arquivo_blob}
        return super().create(dados_dict)
        
        # Retornam vários arquivos com o mesmo nome, ou apenas 1
    def busca_nome_do_arquivo(self, usuario_login):
        comando = f'SELECT id_arquivos FROM usuarios WHERE login LIKE ?'
        tupla_nome = (usuario_login,)

        id_arquivo = self.custom_command(comando, parametros=tupla_nome)
        arquivos = self.read(info='nome_arquivo', filtro=f'id_arquivo = {id_arquivo[0][0]}')

        return arquivos
        # Tipo de retorno: [{'nome_arquivo': 'teste.png'}, ...]

        # Busca arquivo com nome especifico no banco e salva diretamente na pasta 'Files'
    def salva_arquivo_do_banco(self, usuario_login, nome_do_arquivo):
        
        comando = f'SELECT id_arquivos FROM usuarios WHERE login LIKE ?'
        tupla_nome = (usuario_login,)

        id_arquivo = self.custom_command(comando, parametros=tupla_nome)
        arquivos = self.read(filtro=f'id_arquivo = {id_arquivo[0][0]}')


        if nome_do_arquivo:
            arquivo = [a['arquivo'] for a in arquivos if a['nome_arquivo'] == nome_do_arquivo] or None
            caminho_arquivo = os.path.abspath(f'app/backend/files/{nome_do_arquivo}')

            with open(caminho_arquivo, 'wb') as f:
                f.write(arquivo[0])
        

        # Retorno da pesquisa: [{'id_arquivo': 123, 'nome_arquivo': nome.pdf, 'arquivo': ARQUIVO_BLOB}, ...]


if __name__ == '__main__':
    arq = Arquivo()
    arq.create('maria.carla53', nome_do_arquivo='testepdf.pdf')
    print(arq.busca_nome_do_arquivo('maria.carla53'))
    print(arq.salva_arquivo_do_banco('maria.carla53', 'testepdf.pdf'))