from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def pagina_inicial():
    return render_template ('index.html')

@app.route("/produtos")
def pagina_produtos():
    return render_template ('produtos.html')

@app.route("/contato")
def pagina_contatos():
    return render_template ('contato.html')

if __name__ == '__main__':
    app.run(debug=True)