# Este fichero.py sirve para alojar la factoria de aplicación así como para que Python reconozca la carpeta como un paquete
import os
from flask import Flask

def create_app(test_config = None):
    # Crea y configura la app
    app = Flask(__name__, instance_relative_config = True)
    app.config.from_mapping(SECRET_KEY = 'dev', DATABASE = os.path.join(app.instance_path, 'flask.sqlite'),)

    if test_config is None:
        # Load the instace config, if it exists, when not testing
        app.config.from_file('config.py', silent = True)
    else: 
        app.config.from_mapping(test_config)
    
    # ensure the instance folder exists
    try: 
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # a simple page that says hello
    @app.route('/hello')
    def hello():
        return 'Hello, World!'
    return app