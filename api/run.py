from flask import Flask
from loguru import logger
from .routes.get_client_info import clients_bp


# Crear la app de Flask
app = Flask(__name__)

# Registrar los blueprints
app.register_blueprint(clients_bp, url_prefix='/clients')

logger.info('################ API Iniciada ################')

# Iniciar la app
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)