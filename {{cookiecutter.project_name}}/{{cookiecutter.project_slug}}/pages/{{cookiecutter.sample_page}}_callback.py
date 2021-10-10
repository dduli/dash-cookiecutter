import logging

from dash.dependencies import Input, Output

from {{cookiecutter.project_slug}}.app import app
from {{cookiecutter.project_slug}}.pages.{{cookiecutter.sample_page}}_app import (
    INPUT_BOX_ID,
    OUTPUT_ID,
)


logger = logging.getLogger(__name__)


@app.callback(
    Output(OUTPUT_ID, "children"),
    [
        Input(INPUT_BOX_ID, "value")
    ],
)
def on_button_click(text):
    return text
