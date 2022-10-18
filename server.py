from flask import Flask, render_template, request, redirect

from users import User #importamos la clase usuario para utilizar sus funciones 

app = Flask (__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/new')
def new():
    return render_template('new.html')

@app.route('/create', methods=['POST'])
def create():
    # recibimos  el formulario a través de  una variable llamada  request.form
    User.guardar(request.form)
    return redirect('/')


if __name__=="__main__":
    app.run(debug=True)