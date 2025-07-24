from flask import Flask
from routers.rutas import home_routes

app = Flask(__name__)

# Configura una clave secreta para las sesiones (necesaria para flash)
# En producción, esto debería ser un valor más complejo y seguro.
app.secret_key = 'my-super-secret-key'

# Registrar el blueprint de las rutas home
app.register_blueprint(home_routes)

if __name__ == '__main__':
    # El modo debug permite que los cambios se reflejen automáticamente.
    app.run(debug=True)