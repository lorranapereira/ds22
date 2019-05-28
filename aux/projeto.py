from projeto import Projeto
from datetime import datetime
from psycopg2 import connect
from funcionario import Funcionario
from departamento import Departamento
from funcionariodao import funcionarioDao
from departamentodao import departamentoDao
class ProjetoDao:
    def __init__(self):
       self._dados_con = "dbname=aulahoje host=localhost user=postgres password=postgres"

    def salvar(self,projeto):
        daoprojeto = ProjetoDao()
        if(projeto.codigo == None):
            daoprojeto.inserir(projeto)
        else:
            daoprojeto.alterar(projeto)

    def inserir(self,projeto):
        with connect(self._dados_con) as conn:
            cur = conn.cursor()
            cur.execute('INSERT INTO projeto (nome,"dataPrevista") VALUES (%s,%s) RETURNING id',[projeto.nome,projeto.data])
            linhaid = cur.fetchone()[0]
            projeto.codigo = linhaid
            conn.commit()
            cur.close()

    def listar(self):
        vet = []
        with connect(self._dados_con) as conn:
            cur = conn.cursor()
            cur.execute('SELECT * FROM projeto')
            for linha in cur.fetchall():
                print(linha)
                projeto = Projeto(linha[0], linha[2])
                projeto.codigo = linha[1]
                projeto.data = linha[2]
                vet.append(projeto)
            conn.commit()
            cur.close()
            return vet

    def deletar(self,cod):
        with connect (self._dados_con) as conn:
            cur = conn.cursor()
            cur.execute("DELETE FROM projeto WHERE id=%s",[cod])
            conn.commit()
            cur.close()

    def buscar(self,cod):
        with connect (self._dados_con) as conn:
            cur = conn.cursor()
            cur.execute('SELECT  p.id as id_projeto, p.nome as nome_projeto, p."dataPrevista", f.admin,f.email, f.login,f.nome as nome_funcionario, f.id as id_funcionario FROM projeto as p LEFT JOIN funcproj  as fp ON p.id = fp."idProjeto" LEFT JOIN funcionario as f ON fp."idFuncionario" = f.id WHERE p.id = %s',[cod])
            linha = cur.fetchall()
            projeto = Projeto(linha[0][1],linha[0][2])
            projeto.codigo = linha[0][0]
            if(linha[0][7] == None):
                return projeto
            else:
                for l in linha:
                    funcionario = Funcionario(l[6],l[4],l[5])
                    funcionario.codigo = l[7]
                    projeto.addFunc(funcionario)
            conn.commit()
            cur.close()
            return projeto
    def vincularFunc(self,projeto):
        with connect(self._dados_con) as conn:
            cur = conn.cursor()
            cur.execute('SELECT "idFuncionario" FROM funcproj WHERE "idProjeto"=%s', [projeto.codigo])
            vet = []
            for linha in cur.fetchall():
                l = linha[0]
                vet.append(l)
            for f in projeto.funcs:
                if(not vet.__contains__(f.codigo)):
                    sql = cur.execute('INSERT INTO funcproj("idProjeto", "idFuncionario") VALUES (%s, %s)',[projeto.codigo, f.codigo])

    def alterar(self,projeto):
        with connect(self._dados_con) as conn:
            cur = conn.cursor()
            cur.execute('UPDATE projeto SET nome = %s, "dataPrevista" = %s WHERE id = %s',[projeto.nome,projeto.data,projeto.codigo])
            conn.commit()
            cur.close()
        

if __name__ == '__main__':
    dao = ProjetoDao()
    p = dao.buscar(3)
    print(p)
