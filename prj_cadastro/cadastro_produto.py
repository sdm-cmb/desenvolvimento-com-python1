
from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
#flask com f minusculo é a biblioteca, Flask com F maiusculo é a classe 



# conector faz o a conexão do sql com python


# a variavel abaixo é a variavel que roda a aplicação (todos os objetos de projeto dependem dela)
app = Flask(__name__)
#Varialvel da aplicação sempre pede __name__

# a linha abaixo cria a chave de segurança, serve de verificação
app.secret_key = "aprendendodoiniciocomdaniel"

# a linha abiaxo configura o acesso ao banco de dados 
app.config["SQLALCHEMY_DATABASE_URI"] = '{SGBD}://'

# @ signfica criar uma rota
@app.route('/inicio')
def ola():
    return '<h1>Inciando Flask</h1>'

@app.route('/lista')
def lista():
    return render_template('index.html',
                           descricao ="Aqui estão seus produtos cadastrados",  lista_prod = produtos_cadastrados)
#render template busca a pagina dentro de uma pasta templates 


@app.route('/cadastrar')
def cadastrar_produto():
    return render_template('cadastrar.html')

@app.route('/adicionar', methods=['POST', ])
def adicionar_produtos():

    nome_prod = request.form['TxtNome']
    marca_prod = request.form['TxtMarca']
    preco_prod = request.form['TxtPreco']

    novo_produto = Produto(nome_prod, marca_prod, preco_prod)

    produtos_cadastrados.append(novo_produto)
    return render_template("index.html",
                           descricao= "Novo Produto Cadastrado", lista_prod = produtos_cadastrados)
app.run()

#400 a 404 - pagina nao encontrada nos rastros 
#200 a 209 - retorno encontrado 
# SQL ALCHEMY me da segurança para fazer o banco de dados dentro do pyhton
