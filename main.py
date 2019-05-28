from flask import Flask,session,render_template,request,redirect

from depto import DeptoDAO
from deptocl import Departamento
from func import FuncDAO
from funccl import Funcionario
from projetoDao import ProjDAO
from projeto import Projeto
from datetime import datetime

app = Flask(__name__,template_folder='template')
app.secret_key = 'chave'

@app.route('/')
def home():
    return render_template('login.html')

@app.route('/login',methods = ['POST','GET'])
def login():
    session['email'] = request.form['email']
    session['senha'] = request.form['senha']
    session['user'] = request.form['user']
    if session['user'] == "True" or session['user'] == "False":
        return redirect('/verificalogin')
    

@app.route('/verificalogin')
def verificar():
    val = FuncDAO().verificarFunc(session['email'],session['senha'],session['user'])
    if val == None:
        return "nao"
    else:
        return render_template('index.html', user = session['email'])
        
@app.route('/formprojeto')
def formprojeto():
    return render_template('formprojeto.html',func = FuncDAO().listar()) 

@app.route('/inserirproj', methods = ['POST','GET'])
def inserirproj():
    nome = request.form['nome']
    data = request.form['data_prevista']
    data_prevista = datetime.strptime(data,"%Y-%m-%d")
    proj = Projeto(nome,data_prevista)
    val = ProjDAO().inserir(proj)
    if id!='':
        proj = Projeto(nome,data_prevista)
        proj.id = id
        depto = DeptoDAO().alterar(dep)
    else:
        dep = Departamento(nome)
        dep.Gerente = idGerente
        depto = DeptoDAO().inserir(dep)
    return redirect('/listarProjeto')

@app.route('/listarProjeto')
def listarProj():
    return render_template('listarProj.html', proj = ProjDAO().listar()) 

@app.route('/deletarProjeto', methods = ['GET'])
def deletarProj():
    id = request.args.get('id')
    proj = ProjDAO().deletar(int(id))
    return redirect('/listarProjeto') 


@app.route('/form')
def form():
    try:
        cod = request.args.get('id')
        fundao = FuncDAO().buscar(cod)
    except:
        funcdao = None
    return render_template('form.html',dep = DeptoDAO().listar(), nome='Funcionário',func=fundao)

@app.route('/envio', methods = ['POST','GET'])
def trata_form():
    nome = request.form['nome']
    id_depto = (request.form['idDepto'])
    id = request.form['id']
    if id!='':
        dep = DeptoDAO().buscar(id_depto)
        fundao = Funcionario(nome)
        fundao.depto = dep
        fundao.id = id
        func = FuncDAO().alterar(fundao)
    else:
        dep = DeptoDAO().buscar(id_depto)
        funclass = Funcionario(nome)
        funclass.depto = dep
        fundao = FuncDAO().inserir(funclass)
    return "llll"

@app.route('/listar')
def listar():
    return render_template('lista.html',func=FuncDAO().listar())

@app.route('/deletar', methods = ['GET'])
def deletar():
    id = request.args.get('id')
    fundao = FuncDAO().deletar(int(id))
    return redirect('/listar') 

@app.route('/deptoform')
def formdepto():
    return render_template('formdep.html',dep = None,func=FuncDAO().funcNaoGerente())
  
@app.route('/enviodepto', methods = ['POST','GET'])
def trata_formdep():
    nome = request.form['nome']
    id = request.form['id']
    idGerente = request.form['id_gerente']
    if id!='':
        dep = Departamento(nome)
        dep.id = id
        dep.Gerente = idGerente
        depto = DeptoDAO().alterar(dep)
    else:
        dep = Departamento(nome)
        dep.Gerente = idGerente
        depto = DeptoDAO().inserir(dep)
    return redirect('/listardepto') 

@app.route('/listardepto')
def listardepto():
    return render_template('listadepto.html',depto=DeptoDAO().listar())

@app.route('/deletardepto')
def deletardepto():
    id = request.args.get('id')
    depto=DeptoDAO().deletar(id)
    return redirect('/listardepto') 

def main():
    app.env = 'development'
    app.run(debug=True, port=5000)

if __name__ == "__main__":
    main()
