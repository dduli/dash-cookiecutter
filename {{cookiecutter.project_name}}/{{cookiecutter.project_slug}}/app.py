import dash
import os
import dash_bootstrap_components as dbc
from flask import Flask


flask_app = Flask(__name__)
flask_app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0
flask_app.config["SECRET_KEY"] = os.urandom(12)


app = dash.Dash(
    __name__,
    server=flask_app,
    external_stylesheets=[dbc.themes.BOOTSTRAP],

)
app.config.suppress_callback_exceptions = True
app.secret_key = os.urandom(12)
