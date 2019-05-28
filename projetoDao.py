
from conexao import ConDAO 
from projeto import Projeto

class ProjDAO:
    def inserir(self,obj):
        try:
            con = ConDAO().connect()
            cur = con.cursor()
            cur.execute('insert into "Projeto" (nome,"dataPrevista") values (%s,%s)',[obj.nome,obj.dataPrevista])
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
            cod = int(id)
            cur.execute('delete from "Projeto" where id = (%s)',[cod])
            con.commit()
            con.close()
            return "Deletado com sucesso"
        except ValueError as e:
            return "Erro, valor inválido:{}".format(e)
        except SyntaxError as e:
            return "Erro de sintaxe: {}".format(e) 
        except BaseException as e:
            return "Erro ao deletar: {}".format(e)

    def alterar(self,obj):
        try: 

            con = ConDAO().connect()
            cur = con.cursor()
            cod = int(a.id)
            cur.execute('update "Projeto" set nome = (%s), "dataPrevista"=(%s) where id = (%s)',[obj.nome,obj.dataPrevista,cod])
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
            cur.execute('select *from "Projeto" where id = (%s)',[cod])
            con.commit()
            linha = cur.fetchone()
            con.close()
            proj = Projeto(linha[0])
            proj.id = linha[1]
            proj.dataPrevista = linha[2]
            return proj
                      
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
            cur.execute('select *from "Projeto" order by id')
            con.commit()
            lista = []
            for linha in cur.fetchall():
                proj = Projeto(linha[0])
                proj.id = linha[1]
                proj.dataPrevista = linha[2]
                lista.append(proj)
            con.close()
            return lista         
        except ValueError as e:
            return "Erro, valor inválido: {} ".format(e)
        except SyntaxError as e:
            return "Erro de sintaxe: {}".format(e)
        except BaseException as e:
            return "Erro ao buscar: {} ".format(e)

