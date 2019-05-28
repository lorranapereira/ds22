
from conexao import ConDAO 
from deptocl import Departamento
from func import FuncDAO
from funccl import Funcionario

class DeptoDAO:
    def inserir(self,a):
        try:
            con = ConDAO().connect()
            cur = con.cursor()
            id = int(a.Gerente)
            cur.execute('insert into "Departamento" (nome,id_gerente) values (%s,%s)',[a.nome,id])
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
            cur.execute('delete from "Departamento" where id = (%s)',[id])
            con.commit()
            con.close()
            return "Deletado com sucesso"
        except ValueError as e:
            return "Erro, valor inválido:{}".format(e)
        except SyntaxError as e:
            return "Erro de sintaxe: {}".format(e) 
        except BaseException as e:
            return "Erro ao deletar: {}".format(e)

    def alterar(self,a):
        try: 

            con = ConDAO().connect()
            cur = con.cursor()
            id = int(a.id)
            cur.execute('update "Departamento" set nome = (%s) where id = (%s)',[a.nome,a.id])
            con.commit()
            con.close()
            return "Alterado com sucesso"
        except ValueError as e:
            return "Erro, valor inválido: {}".format(e)
        except SyntaxError as e:
            return "Erro de sintaxe: {}".format(e)
        except BaseException as e:
            return "Erro ao alterar: {}".format(e)

    def buscar(self,cod):
        try: 

            con = ConDAO().connect()
            cur = con.cursor()
            cod = int(cod)
            cur.execute('select *from "Departamento" where id = (%s)',[cod])
            con.commit()
            linha = cur.fetchone()
            con.close()
            dep = Departamento(linha[0])
            dep.id = linha[1]
            dep.Gerente = linha[2]
            return dep
                      
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
            cur.execute('select *from "Departamento" inner join "Funcionario" on "Funcionario".id ="Departamento".id_gerente where "Funcionario".id ="Departamento".id_gerente order by "Departamento".id')
            con.commit()
            lista = []
            for linha in cur.fetchall():
                dep = Departamento(linha[0])
                dep.id = linha[1]
                dep.Gerente = linha[2]
                lista.append(dep)
            con.close()
            return lista         
        except ValueError as e:
            return "Erro, valor inválido: {} ".format(e)
        except SyntaxError as e:
            return "Erro de sintaxe: {}".format(e)
        except BaseException as e:
            return "Erro ao buscar: {} ".format(e)

