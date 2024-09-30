from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)
app.secret_key = 'supersecretkey'  # Cambia esto por una clave más segura
app.config['SESSION_TYPE'] = 'filesystem'

# Simular una base de datos temporal
administradores = {'admin@example.com': 'password123'}

@app.route('/')
def index():
    return redirect(url_for('login'))

# Ruta para el inicio de sesión
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        if email in administradores and administradores[email] == password:
            session['logged_in'] = True
            return redirect(url_for('gestion_jornada'))
        else:
            return render_template('login.html', error="Credenciales incorrectas")
    return render_template('login.html')

# Ruta para gestionar la jornada
@app.route('/gestion_jornada', methods=['GET', 'POST'])
def gestion_jornada():
    if not session.get('logged_in'):
        return redirect(url_for('login'))
    
    if request.method == 'POST':
        cantidad_lavadores = request.form['cantidad_lavadores']
        nombres_lavadores = request.form.getlist('nombres_lavadores')
        # Puedes procesar los nombres de los lavadores aquí
        return redirect(url_for('registrar_vehiculo'))
    
    return render_template('gestion_jornada.html')

# Ruta para registrar vehículos
@app.route('/registrar_vehiculo', methods=['GET', 'POST'])
def registrar_vehiculo():
    if not session.get('logged_in'):
        return redirect(url_for('login'))
    
    if request.method == 'POST':
        # Recoger la información del formulario de registro de vehículos
        tipo_carro = request.form['tipo_carro']
        color_carro = request.form['color_carro']
        propietario = request.form['propietario']
        telefono = request.form['telefono']
        placa = request.form['placa']
        lavador = request.form['lavador']
        precio = request.form['precio']
        tipo_lavado = request.form['tipo_lavado']
        # Procesar los datos del vehículo aquí

        return redirect(url_for('finalizar_jornada'))
    
    return render_template('registrar_vehiculo.html')

# Ruta para finalizar la jornada
@app.route('/finalizar_jornada', methods=['GET', 'POST'])
def finalizar_jornada():
    if not session.get('logged_in'):
        return redirect(url_for('login'))

    if request.method == 'POST':
        # Procesar finalización de jornada
        session.clear()  # Cerrar la sesión
        return redirect(url_for('login'))
    
    return render_template('finalizar_jornada.html')

if __name__ == '__main__':
    app.run(debug=True)
