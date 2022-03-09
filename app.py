
from flask import Flask, request, session, render_template, url_for, jsonify
from werkzeug.utils import redirect
from werkzeug.exceptions import abort

app = Flask(__name__)

app.secret_key = 'Mi_llave_secreta'

#http://localhost
@app.route('/')
def inicio():
        if 'username' in session:
            return f'El usuario ya ha hecho login {session["username"]}'
        return 'No ha  hecho login'

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        #omitimos validacion de usuario y password
        usuario = request.form['username']
        #agregar usuario a la session
        session['username'] = usuario 
        #session['username'] = request.form['username']
        return redirect(url_for('inicio'))
    return render_template('login.html')

    #app.logger.info(f'Entramos al path`` {request.path }')  
    #return 'Hola Mundo desde Flask'

@app.route('/logout')
def logout():
    session.pop('username')
    return redirect(url_for('inicio'))


@app.route('/saludar/<nombre>')
def saludar(nombre):
    return f'Saludos {nombre}'

@app.route('/edad/<int:edad>')
def mostrar_edad(edad):
    return f'Tu edad es: {edad}'

@app.route('/mostrar/<nombre>', methods=['GET', 'POST'])
def mostrar_nombre(nombre):
    return render_template('mostrar.html', nombre=nombre)

@app.route('/redireccionar')
def redireccionar():
    return redirect(url_for('mostrar_nombre', nombre = 'Ambrocio'))

@app.route('/salir')
def salir():
    return abort(404)

@app.errorhandler(404)
def pagina_no_encontrada(error):
    return render_template('error404.html', error=error), 404

#REST Representacion  dtstr transfer
@app.route('/api/mostrar/<nombre>', methods=['GET', 'POST'])
def mostrar_jason(nombre):
    valores = {'nombre': nombre, 'metodo_http': request.method }
    return jsonify (valores)
  