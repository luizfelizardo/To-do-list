from flask import Flask, redirect, request, render_template, url_for
import sqlite3

app = Flask(__name__)

def conectar_banco():
    return sqlite3.connect("tarefas.db")

def criar_tabela():
    conexao = conectar_banco()
    cursor = conexao.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS tarefas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            descricao TEXT NOT NULL,
            status TEXT NOT NULL,
            data_criacao TEXT NOT NULL,
            data_vencimento TEXT
        )
    """)
    conexao.commit()
    conexao.close()

def adicionar_tarefa(descricao, status, data_criacao, data_vencimento):
    conexao = conectar_banco()
    cursor = conexao.cursor()
    cursor.execute("""
        INSERT INTO tarefas (descricao, status, data_criacao, data_vencimento)
        VALUES (?, ?, ?, ?)
    """, (descricao, status, data_criacao, data_vencimento))
    conexao.commit()
    conexao.close()

def listar_tarefas():
    conexao = conectar_banco()
    cursor = conexao.cursor()
    cursor.execute("SELECT * FROM tarefas")
    tarefas = cursor.fetchall()
    conexao.close()
    return tarefas

def deletar_tarefa(id):
    conexao = conectar_banco()
    cursor = conexao.cursor()
    cursor.execute("DELETE FROM tarefas WHERE id = ?", (id,))
    conexao.commit()
    conexao.close()

criar_tabela()

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        descricao = request.form['descricao']
        data_criacao = request.form['data_criacao']
        data_vencimento = request.form['data_vencimento']
        adicionar_tarefa(descricao, 'pendente', data_criacao, data_vencimento)
        return redirect(url_for('index'))  # Redireciona para evitar reenvio do formulário
    tarefas = listar_tarefas()
    return render_template('index.html', tarefas=tarefas)

@app.route('/deletar/<int:id>')
def deletar(id):
    deletar_tarefa(id)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)