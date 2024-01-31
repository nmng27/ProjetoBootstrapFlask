from flask import Flask, render_template, request, redirect, session,flash
from Arquivos.classeFuncionario import Funcionario
from Arquivos.classeUsuario import Usuario

app = Flask(__name__)
app.secret_key = "mult-e"

funcionarios = []
usuarioPermitido001 = Usuario("nicholas.mangussi@linkedin.com","senha123")
usuarioPermitido002 = Usuario("usuario.teste@exemplo.com","senha")
usuarioPermitido003 = Usuario("producao@exemplo.com","senha")
usuariosPermitidos = {usuarioPermitido001.get_email():usuarioPermitido001.get_senha(),
                      usuarioPermitido002.get_email():usuarioPermitido002.get_senha(),
                      usuarioPermitido003.get_email():usuarioPermitido003.get_senha()}
@app.route("/")
def index():
    return render_template("lista.html",Titulo="Lista de Funcionários",funcionarios=funcionarios)

@app.route("/novo")
def novo():
    return render_template("novo.html",Titulo="Adicionar colaborador")

@app.route("/criar",methods=["POST"])
def criar():
    nome = request.form['nome']
    email = request.form['email']
    cargo = request.form['cargo']

    funcionario = Funcionario(nome,email,cargo)
    funcionarios.append(funcionario)
    return redirect('/')

@app.route('/login')
def login():
    return render_template("login.html")


@app.route("/autenticar",methods=["POST"])
def autenticar():
    emailDigitado = request.form["email"]
    senhaDigitada = request.form["senha"]

    for k,v in usuariosPermitidos.items():
        if(emailDigitado == k and senhaDigitada == v):
            flash("Usuário Logado com sucesso!")
            return redirect("/")
        else:
            flash("Usuário Negado!")
            return redirect("/login")
            


@app.route("/logout")
def logout():
    session['usuarioLogado'] = None
    flash("Logout efetuado com sucesso!")
    return redirect("/login")
app.run(debug=True)