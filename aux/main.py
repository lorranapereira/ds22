from flask import Flask, render_template, request, redirect, session
import hashlib
from funcionariodao import funcionarioDao
from funcionario import Funcionario
from departamentodao import departamentoDao
from departamento import Departamento
from projetodao import ProjetoDao
from projeto import Projeto
import psycopg2
from datetime import date

app = Flask(__name__)

@app.route('/')
def hello():
    return redirect('funcionario/telaListar')


@app.route('/login',methods = ['POST', 'GET'])
def login():
    daofunc = funcionarioDao()
    f = daofunc.procurar(request.form["senha"],request.form["login"])
    if(f == None):
        return ('senha ou login errado')
    else:
        session['login'] = request.form["login"]
        session['senha'] = request.form["senha"]
        if(f.admin == "true"):
            return render_template('telaInserirFunc.html')
        else:
            return redirect('projeto/telaListar')

    

@app.route('/funcionario/telaInserir')
def formsFunc():
    dao = departamentoDao()
    lista_deptos = dao.listar()
    return render_template('telaInserirFunc.html', departamentos = lista_deptos)

@app.route('/funcionario/telaListar')
def listaFunc():
    dao = funcionarioDao()
    lista_func = dao.listar()
    return render_template('telaListarFunc.html', funcionarios = lista_func)

@app.route('/funcionario/excluir', methods = ['GET'])
def excluirFunc():
    cod_func = int(request.values["cod"])
    dao = funcionarioDao()
    dao.deletar(cod_func)
    return redirect ('/funcionario/telaListar')

@app.route('/funcionario/alterar')
def alterarFunc():
    cod_alterar = int(request.values["cod"])
    dao = funcionarioDao()
    funcionario = dao.buscar(cod_alterar)
    dao = departamentoDao()
    lista_deptos = dao.listar()
    return render_template('telaInserirFunc.html', funcionario = funcionario, departamentos = lista_deptos)

@app.route('/funcionario/buscar')
def buscarFunc():
    cod = int(request.values["cod"])
    dao = funcionarioDao()
    funcionario = dao.buscar(cod)
    return render_template('telaBuscarFunc.html', funcionario = funcionario)

@app.route('/funcionario/salvar', methods = ['POST', 'GET'])
def salvarFunc():
    nome = request.form["nome"]
    email = request.form["email"]
    departamento = request.form["departamento"]
    login = request.form["login"]
    admin = request.form["admin"]
    senha = request.form["senha"]
    daodepto = departamentoDao()
    senha = hashlib.md5(senha.encode()).hexdigest()
    d = daodepto.buscar(int(departamento))
    f = Funcionario(nome,email,login,senha,admin)
    f.addDepto(d)
    dao = funcionarioDao()
    if(request.values.has_key("codigo") == True):
        cod = request.form["codigo"]
        f.codigo = int(cod)
    dao.salvar(f)
    return redirect('/funcionario/telaListar')

@app.route('/departamento/buscar')
def buscarDepto():
    cod = int(request.values["cod"])
    dao = departamentoDao()
    departamento = dao.buscar(cod)
    return render_template('telaBuscarDepto.html', departamento = departamento)


@app.route('/departamento/salvar', methods = ['POST', 'GET'])
def salvarDepto():
    nome = request.form["nome"]
    gerente = request.form["gerente"]
    daodepto = departamentoDao()
    daofunc =  funcionarioDao()
    f = daofunc.buscar(int(gerente))
    d = Departamento(nome)
    d.addGerente(f)
    if(request.values.has_key("codigo") == True):
        cod = request.form["codigo"]
        d.codigo = int(cod)
    daodepto.salvar(d)
    return redirect('/')

@app.route('/departamento/telaListar')
def listaDepto():
    dao = departamentoDao()
    lista_deptos = dao.listar()
    return render_template('telaListarDepto.html', departamentos = lista_deptos)

@app.route('/departamento/telaInserir')
def formsDepto():
    dao = funcionarioDao()
    lista_funcs = dao.listar()
    return render_template('telaInserirDepto.html', funcionarios = lista_funcs)

@app.route('/departamento/alterar')
def alterarDepto():
    cod_alterar = int(request.values["cod"])
    daodepto = departamentoDao()
    departamento = daodepto.buscar(cod_alterar)
    daofunc = funcionarioDao()
    lista_funcs = daofunc.listar()
    return render_template('telaInserirDepto.html', departamento = departamento, funcionarios = lista_funcs)

@app.route('/departamento/excluir', methods = ['GET'])
def excluirDepto():
    cod_depto = int(request.values["cod"])
    dao = departamentoDao()
    dao.deletar(cod_depto)
    return redirect ('/')

@app.route('/projeto/telaInserir')
def formsProj():
    dao = ProjetoDao()
    daofunc = funcionarioDao()
    lista_projetos = dao.listar()
    lista_funcs = daofunc.listar()
    return render_template('telaInserirProjeto.html', projetos = lista_projetos, funcionarios = lista_funcs)


@app.route('/projeto/alterar')
def alterarProj():
    cod_alterar = int(request.values["cod"])
    daoproj = ProjetoDao()
    projeto = daoproj.buscar(cod_alterar)
    #daofunc = funcionarioDao()
    #lista_funcs = daofunc.listar()
    return render_template('telaInserirProjeto.html', projeto = projeto)

@app.route('/projeto/salvar', methods = ['POST', 'GET'])
def salvarProjeto():
    func = request.form["func"]
    nome = request.form["nome"]
    data = request.form["data"]
    daoprojeto = ProjetoDao()
    daofunc = funcionarioDao()
    f = daofunc.buscar(int(func))
    p = Projeto(nome,data)
    p.addFunc(f)
    if(request.values.has_key("codigo") == True):
        cod = request.form["codigo"]
        p.codigo = int(cod)
    daoprojeto.salvar(p)
    daoprojeto.vincularFunc(p)
    return redirect('/telaListarProjeto')

@app.route('/projeto/telaListar')
def listaProjeto():
    dao = ProjetoDao()
    lista_proj = dao.listar()
    return render_template('telaListarProjetos.html', projetos = lista_proj)

@app.route('/projeto/excluir', methods = ['GET'])
def excluirProjeto():
    cod_proj = int(request.values["cod"])
    dao = ProjetoDao()
    dao.deletar(cod_proj)
    return redirect ('/')

@app.route('/projeto/buscar')
def buscarProjeto():
    cod = int(request.values["cod"])
    dao = ProjetoDao()
    projeto = dao.buscar(cod)
    return render_template('telaBuscarProjeto.html', projeto = projeto)
def main():
    app.secret_key = 'string'
    app.env = 'development'
    app.run(debug = True, port = 5000)

if __name__ == '__main__': 
    main()
