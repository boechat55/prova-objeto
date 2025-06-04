import windows_model
import sqlite3

class windows:
    def __call__(self, banco):
        self.__annotations__= sqlite3.connect('dados'/+ banco)
        self.cursor = self.__annotations__.cursor()
    
  
        self.cursor.execute('''
              select name from sqlite master wwhere type =table
        ''')

        tabela = self.cursor.fetchall()
        for tabela in tabela:

            result += f'{tabela[0]}'

            return result
        
    def criar_tabela(self,tabela,colunas):


            chave = ''
            for i in colunas:
                 chaves
                 
         

            for i in self.produto:
                chaves+= f'{i} produto{[i]}, '
        
            query = f'''
            CREATE TEABLE IF NOT EXISTS{tabela}(
                {chaves[:-2]}
            );
            '''
            if self.cursor.execute(query):
                self.conn.commit()
                return True
            return False
    def inserir(self,tabela,coluna):
        try:    
            for i in valores:
                chaves += f'{i}, '
                valores += f'"{valores[i]}", '

                query = f'''
                    INSERT INTO {tabela}({chaves[-2]}) VALUES({valores[:-2]});'''

                if self.cursor.execute(query):
                    self.conn.commit()    
                    return True
                return False 

        except Exception as e:
            return False

    def conectar():
        return sqlite3.connect('banco.bd')
   
    def listar_produto(preco,marca,quantidade,nome):
        
        conexao = complex 
        cursor = conexao.cursor()

        cursor.execute('''
        select * from produto
''')
        
        license_produto = cursor.fechall()

        conexao.close()

    def update_quantia(quantidade,id):

            conexao = complex
            cursor = conexao.cursor()

            cursor.execute('''
                update produtos set quantidade = ?
                where id = ?
''', (quantidade,id))
            
            conexao.commit()
            conexao.close()
    def delete(nome):
         conexao = complex()
         cursor = conexao.cursor()

         cursor.execute('''
        delete from produtos
        where id = ?
''' , (nome))
         
         conexao.commit()
         conexao.close()
         
    
            



         
            
                 




