from flask import Flask
from routers.router_home import home_routes

app = Flask(__name__)

# Registrar el blueprint de las rutas home
app.register_blueprint(home_routes)

if __name__ == '__main__':
    # El modo debug permite que los cambios se reflejen automáticamente.
    app.run(debug=True)