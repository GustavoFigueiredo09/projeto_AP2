if __name__ == '__main__':
    from mainCRUD import BaseCRUD
else:
    from .mainCRUD import BaseCRUD
    
import os


class Arquivo(BaseCRUD):
    def __init__(self):
        super().__init__(tabela='arquivos')
    
    def create(self, usuario_login, nome_do_arquivo, arquivo_blob):
        id_usuario = self.custom_command(f'SELECT id_usuario FROM usuarios WHERE login = "{usuario_login}"')
        if not id_usuario:
            print(f"Usuário {usuario_login} não encontrado.")
            return None
        
        id_usuario = id_usuario[0][0]
        dados_dict = {'id_arquivo': id_usuario, 'nome_arquivo': nome_do_arquivo, 'arquivo': arquivo_blob}
        print("Resultado da consulta:", id_usuario)
        return super().create(dados_dict)

    # Retorna varios arquivos para o usuario informado    
    def busca_nome_do_arquivo(self, usuario_login):
        id_usuario = self.custom_command(f'SELECT id_usuario FROM usuarios WHERE login = "{usuario_login}"')
        if not id_usuario:
            print(f"Usuário {usuario_login} não encontrado.")
            return None
        
        id_usuario = id_usuario[0][0]
        arquivos = self.read(info='*', filtro=f'id_arquivo = {id_usuario}')
        return arquivos

    def salva_arquivo_do_banco(self, usuario_login, nome_do_arquivo):
        comando = f'SELECT id_usuario FROM usuarios WHERE login LIKE ?'
        tupla_nome = (usuario_login,)
        id_usuario = self.custom_command(comando, parametros=tupla_nome)
        if not id_usuario:
            print(f"Usuário {usuario_login} não encontrado.")
            return None
        
        id_usuario = id_usuario[0][0]
        arquivos = self.read(filtro=f'id_arquivo = {id_usuario}')
        
        if nome_do_arquivo:
            arquivo = [a['arquivo'] for a in arquivos if a['nome_arquivo'] == nome_do_arquivo] or None
            if arquivo:
                caminho_arquivo = os.path.abspath(f'app/backend/files/{nome_do_arquivo}')
                with open(caminho_arquivo, 'wb') as f:
                    f.write(arquivo[0])
                print(f"Arquivo {nome_do_arquivo} salvo com sucesso.")
            else:
                print(f"Arquivo {nome_do_arquivo} não encontrado.")
    
    # Exclui o(s) arquivo(s) selecionado(s)
    def excluir_arquivo(self, nome_do_arquivo):
        # Verifica se o arquivo existe no banco
        arquivos = self.read(filtro=f"nome_arquivo = '{nome_do_arquivo}'")
        if not arquivos:
            print(f"Arquivo {nome_do_arquivo} não encontrado no banco.")
            return
        
        # Executa o comando de exclusão do banco de dados
        comando = f"DELETE FROM arquivos WHERE nome_arquivo = ?"
        parametros = (nome_do_arquivo,)
        
        # Chamando o método de execução do comando DELETE
        resultado = self.custom_command(comando, parametros=parametros)
        
        # Verifica se a exclusão foi feita com sucesso
        if resultado:
            print(f"Arquivo {nome_do_arquivo} excluído com sucesso do banco de dados.")
            self.commit()  # Garantido que a exclusão permanessa
        else:
            print(f"Falha ao excluir o arquivo {nome_do_arquivo}.")
        
        # Verifica se o arquivo ainda existe no sistema de arquivos
        caminho_arquivo = os.path.abspath(f'app/backend/files/{nome_do_arquivo}')
        if os.path.exists(caminho_arquivo):
            os.remove(caminho_arquivo)  # Excluindo o arquivo do sistema
            print(f"Arquivo {nome_do_arquivo} excluído do sistema de arquivos.")
        else:
            print(f"O arquivo {nome_do_arquivo} não foi encontrado no sistema de arquivos.")

        # Retorno da pesquisa: [{'id_arquivo': 123, 'nome_arquivo': nome.pdf, 'arquivo': ARQUIVO_BLOB}, ...]

if __name__ == '__main__':
    arq = Arquivo()
    # arq.create('maria.carla53', nome_do_arquivo='testepdf.pdf')
    print(arq.busca_nome_do_arquivo('maria.carla53'))