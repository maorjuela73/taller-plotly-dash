"""
EJERCICIO 3 (ESTUDIANTE): Reactividad Pura con @app.callback
"""

from dash import Dash, html, dcc, Input, Output

app = Dash(__name__)

app.layout = html.Div(style={"maxWidth": "600px", "margin": "50px auto", "fontFamily": "sans-serif"}, children=[
    html.H2("Mi Primer Callback Reactivo"),
    html.P("Escribe tu nombre abajo para ver la reactividad en acción:"),

    dcc.Input(
        id="input-nombre",
        type="text",
        value="Ada Lovelace",
        placeholder="Ingresa tu nombre...",
        style={"width": "100%", "padding": "10px", "fontSize": "16px", "borderRadius": "5px", "border": "1px solid #cbd5e1"}
    ),

    html.Br(), html.Br(),

    html.Div(
        id="salida-saludo",
        style={"padding": "15px", "backgroundColor": "#eff6ff", "borderRadius": "6px", "color": "#1d4ed8", "fontWeight": "bold"}
    )
])

# -----------------------------------------------------------------------------
# RETO: Conecta el Input con el Output usando el decorador @app.callback
# 1. Output: id "salida-saludo", propiedad "children"
# 2. Input: id "input-nombre", propiedad "value"
# -----------------------------------------------------------------------------
# @app.callback(
#     Output(component_id=..., component_property=...),
#     Input(component_id=..., component_property=...)
# )
def responder_saludo(valor_del_input):
    # TODO: Retorna un saludo personalizado con 'valor_del_input'
    pass

if __name__ == "__main__":
    app.run(debug=True)
