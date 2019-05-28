
from conexao import ConDAO 
from funccl import Funcionario
from deptocl import Departamento
class FuncDAO:
    def inserir(self,val):
        try:
            con = ConDAO().connect()
            cur = con.cursor()
            cur.execute('insert into "Funcionario" (nome, "idDepto") values (%s,%s)',[val.nome,val.depto.id])
            con.commit()
            con.close()
            return "Inserido com sucesso"
  
        except TypeError as e:
            return "Erro no valor inserido: {}".format(e) 
        except SyntaxError as e:
            return "Erro de sintaxe: {}".format(e)
        except BaseException as e:
            return "Erro ao inserir: {}".format(e)

    def deletar(self,id):
        try: 
            con = ConDAO().connect()
            cur = con.cursor()
            id = int(id)
            cur.execute('delete from "Funcionario" where id = (%s)',[id])
            con.commit()
            con.close()
            return "Deletado com sucesso"
        except ValueError as e:
            return "Erro, valor inválido:{}".format(e)
        except SyntaxError as e:
            return "Erro de sintaxe: {}".format(e) 
        except BaseException as e:
            return "Erro ao deletar: {}".format(e)

    def alterar(self,val):
        try: 

            con = ConDAO().connect()
            cur = con.cursor()
            id = int(a.id)
            cur.execute('update "Funcionario" set nome = (%s), "idDepto"=(%s) where id = (%s)',[val.nome,val.depto.id,val.id])
            con.commit()
            con.close()
            return "Alterado com sucesso"
        except ValueError as e:
            return "Erro, valor inválido: {}".format(e)
        except SyntaxError as e:
            return "Erro de sintaxe: {}".format(e)
        except BaseException as e:
            return "Erro ao alterar: {}".format(e)

    def buscar(self,id):
        try: 

            con = ConDAO().connect()
            cur = con.cursor()
            id = int(id)
            cur.execute('select *from "Funcionario" where id = (%s)',[id])
            con.commit()
            linha = cur.fetchone()
            con.close()
            func = Funcionario(linha[0],linha[1])
            from depto import DeptoDAO
            func.Depto = DeptoDAO().buscar(linha[2])
            return func
                      
        except ValueError as e:
            return "Erro, valor inválido: {} ".format(e)
        except SyntaxError as e:
            return "Erro de sintaxe: {}".format(e)
        except BaseException as e:
            return "Erro ao buscar: {} ".format(e)

    
    def funcNaoGerente(self):
        try: 
            con = ConDAO().connect()
            cur = con.cursor()
            cur.execute('select *from "Funcionario" LEFT OUTER JOIN "Departamento" on "Funcionario".id = "Departamento".id_gerente WHERE "Departamento".id_gerente IS NULL order by "Funcionario".id')
            con.commit()
            lista = []
            from depto import DeptoDAO
            for linha in cur.fetchall():
                func = Funcionario(linha[0])
                func.id = linha[1]
                func.Depto = DeptoDAO().buscar(linha[2])
                lista.append(func)    
            con.close()
            return lista
                      
        except SyntaxError as e:
            return "Erro de sintaxe: {}".format(e)
        except BaseException as e:
            return "Erro ao buscar: {} ".format(e)

    def verificarFunc(self,email,senha,admin):
        try: 
            con = ConDAO().connect()
            cur = con.cursor()
            senha = int(senha)
            cur.execute('select email from "Funcionario" where email = (%s) and senha = (%s) and admin=(%s)',[email,senha,admin])
            con.commit()
            lista = []
            linha = cur.fetchone()
            return linha       
        except ValueError as e:
            return "Erro, valor inválido: {} ".format(e)
        except SyntaxError as e:
            return "Erro de sintaxe: {}".format(e)
        except BaseException as e:
            return "Erro ao buscar: {} ".format(e)
    
    

    def listar(self):
        try: 
            con = ConDAO().connect()
            cur = con.cursor()
            cur.execute('select *from "Funcionario" order by id')
            con.commit()
            lista = []
            from depto import DeptoDAO
            for linha in cur.fetchall():
                func = Funcionario(linha[0],linha[1])
                func.Depto = DeptoDAO().buscar(linha[2])
                lista.append(func)
            con.close()
            return lista
                      
        except SyntaxError as e:
            return "Erro de sintaxe: {}".format(e)
        except BaseException as e:
            return "Erro ao listar: {} ".format(e)


