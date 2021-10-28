import dash_bootstrap_components as dbc
import dash_html_components as html


# element_ids
INPUT_BOX_ID = "{{cookiecutter.sample_page}}-input_box-id"
OUTPUT_ID = "{{cookiecutter.sample_page}}-output-id"


input_box = dbc.InputGroup(
    [
        dbc.InputGroupText("Text"),
        dbc.Input(id=f"{INPUT_BOX_ID}", placeholder="Place input here", debounce=True),
    ],
    size="lg"
),


def get_layout():
    return dbc.Container(
        [
            html.Hr(),
            dbc.Col(
                input_box,
                style={
                    "width": "50%"
                },
            ),
            dbc.Col(
                html.Div(id=f"{OUTPUT_ID}"),
                style={
                    "width": "50%",
                    "padding-top": "20px",
                },
            )
        ]
    )
