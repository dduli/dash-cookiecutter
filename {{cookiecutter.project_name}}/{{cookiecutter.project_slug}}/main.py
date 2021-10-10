import logging

from dash.dependencies import Input, Output
import dash_core_components as dcc
import dash_bootstrap_components as dbc
import dash_html_components as html

from {{cookiecutter.project_slug}}.app import app
from {{cookiecutter.project_slug}}.pages import (
    {{cookiecutter.sample_page}}_app
)
import {{cookiecutter.project_slug}}.pages.{{cookiecutter.sample_page}}_callback  # noqa: F401


logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)


PAGE_LOADING_SPINNOR_ID = "page-loading-spinnor-id"


home_path = "/"
{{cookiecutter.sample_page}}_path = "/pages/{{cookiecutter.sample_page}}"


dashboard = dbc.Navbar([
    dbc.Col(
        dbc.NavbarBrand(
            "{{cookiecutter.project_name.replace("-", " ").title()}}",
            className="ml-2",
            href="/",
            style={"font-size": 50}
        )
    )
    ],
    color="dark",
    dark=True,
)


app.layout = dbc.Container(
    [
        dcc.Location(id="url", refresh=True),
        dashboard,
        dbc.Spinner(html.Div(id=PAGE_LOADING_SPINNOR_ID), color="warning"),
        html.Div(id="page-content"),
    ],
)


@app.callback(
    [
        Output("page-content", "children"),
        Output(PAGE_LOADING_SPINNOR_ID, "children"),
    ],
    [
        Input("url", "pathname"),
    ],
)
def display_page(pathname):
    if pathname == {{cookiecutter.sample_page}}_path or pathname == home_path:
        return (
            {{cookiecutter.sample_page}}_app.get_layout(),
            ""
        )
    else:
        return "404", ""


if __name__ == "__main__":
    app.run_server(debug=True, host="0.0.0.0", port=8030)
