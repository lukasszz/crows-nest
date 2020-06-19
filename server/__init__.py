from flask import Flask

from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

from server.config import Config

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)

# Dodaje możliwość zrobienia continue w templatach
app.jinja_env.add_extension('jinja2.ext.loopcontrols')

from server import routes, models