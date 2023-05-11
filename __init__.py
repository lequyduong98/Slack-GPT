from flask import Flask

# init SQLAlchemy so we can use it later in our models

app = Flask(__name__)

# blueprint for non-auth parts of app
from .main import main as main_blueprint
app.register_blueprint(main_blueprint)
