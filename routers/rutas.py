from flask import Blueprint, render_template, request, redirect, url_for, flash
from controllers.funciones import buscar_conciliacion_por_iuc, obtener_intervinientes_por_iuc

# Definimos el Blueprint para las rutas principales/home
home_routes = Blueprint('home_routes', __name__)

@home_routes.route('/', methods=['GET', 'POST'])
@home_routes.route('/login', methods=['GET', 'POST'])
def login():
    """
    Maneja el login de usuarios.
    - GET: Muestra el formulario de login.
    - POST: Procesa el login y redirige a la ficha de conciliación.
    """
    if request.method == 'POST':
        # En un caso real, aquí se validarían las credenciales del usuario.
        # Por ahora, simplemente redirigimos como se solicitó.
        return redirect(url_for('home_routes.buscar_conciliacion'))
    
    # Si es GET, simplemente muestra la página de login
    return render_template('public/login.html')

@home_routes.route('/ficha_conciliacion')
def ficha_conciliacion():
    """
    Muestra la página de la ficha de conciliación.
    """
    return render_template('public/conciliacion/ficha_conciliacion.html')


@home_routes.route('/buscar_conciliacion', methods=['GET', 'POST'])
def buscar_conciliacion():
    """
    Muestra la página para buscar la conciliación y redirige al hacer submit.
    """
    if request.method == 'POST':
        iuc = request.form.get('iuc')
        if not iuc:
            flash('Por favor, ingresa un IUC.', 'warning')
            return redirect(url_for('home_routes.buscar_conciliacion'))

        # Realizar ambas búsquedas
        proceso = buscar_conciliacion_por_iuc(iuc)
        intervinientes = obtener_intervinientes_por_iuc(iuc)

        # Solo si no se encuentra NADA, mostrar error
        if not proceso and not intervinientes:
            flash(f'No se encontró información para el IUC {iuc} en ninguna de las tablas consultadas.', 'danger')
            return redirect(url_for('home_routes.buscar_conciliacion'))

        # Si se encuentra algo, renderizar la ficha con los datos disponibles
        return render_template(
            'public/conciliacion/ficha_conciliacion.html',
            proceso=proceso,
            intervinientes=intervinientes
        )
    
    # Si es GET, muestra la página de búsqueda
    return render_template('public/conciliacion/buscar_conciliacion.html')


