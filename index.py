from flask import Flask, render_template, redirect, url_for, request, session, flash

app = Flask(__name__)
app.secret_key = 'tu_clave_secreta'

carros = []  # Lista simulada para los carros
lavadores = []  # Lista simulada para los lavadores

# Página de inicio de sesión
@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Lógica de inicio de sesión
        session['admin'] = True
        flash('Has iniciado sesión correctamente', 'success')
        return redirect(url_for('admin_dashboard'))

    return render_template('login.html')


# Dashboard de administración
@app.route('/admin', methods=['GET', 'POST'])
def admin_dashboard():
    if 'admin' not in session:
        flash('Debes iniciar sesión para acceder a esta página', 'warning')
        return redirect(url_for('login'))

    if request.method == 'POST':
        # Recibir los datos de los lavadores
        cantidad = int(request.form['cantidad'])
        lavadores.clear()  # Limpiar los lavadores previos
        for i in range(cantidad):
            lavador = request.form[f'lavador_{i+1}']
            lavadores.append(lavador)

        flash(f'{cantidad} lavadores registrados exitosamente', 'success')
        return redirect(url_for('admin_dashboard'))

    return render_template('admin_dashboard.html', lavadores=lavadores, carros=carros)


# Registrar los carros
@app.route('/registro', methods=['GET', 'POST'])
def registro_carro():
    if 'admin' not in session:
        flash('Debes iniciar sesión para acceder a esta página', 'warning')
        return redirect(url_for('login'))

    if request.method == 'POST':
        propietario = request.form['propietario']
        telefono = request.form['telefono']
        placa = request.form['placa']
        tipo_carro = request.form['tipo_carro']
        color_carro = request.form['color_carro']
        lavador = request.form['lavador']
        precio = request.form['precio']
        
        # Agregar carro a la lista simulada
        carros.append({
            'propietario': propietario,
            'telefono': telefono,
            'placa': placa,
            'tipo_carro': tipo_carro,
            'color_carro': color_carro,
            'lavador': lavador,
            'precio': float(precio)
        })

        flash('El carro ha sido registrado exitosamente', 'success')
        return redirect(url_for('registro_carro'))

    return render_template('registro_carro.html', lavadores=lavadores, carros=carros)


# Ver los datos de los carros lavados y el dinero recaudado
@app.route('/reporte')
def reporte():
    if 'admin' not in session:
        flash('Debes iniciar sesión para acceder a esta página', 'warning')
        return redirect(url_for('login'))

    total_dinero = sum(carro['precio'] for carro in carros)
    total_carros = len(carros)

    return render_template('reporte.html', total_dinero=total_dinero, total_carros=total_carros, carros=carros)

# Cerrar sesión
@app.route('/logout')
def logout():
    session.pop('admin', None)
    flash('Has cerrado sesión', 'info')
    return redirect(url_for('login'))


if __name__ == '__main__':
    app.run(debug=True)