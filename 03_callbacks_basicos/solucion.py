"""
EJERCICIO 3 (SOLUCIÓN): Reactividad Pura con @app.callback
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

@app.callback(
    Output(component_id="salida-saludo", component_property="children"),
    Input(component_id="input-nombre", component_property="value")
)
def responder_saludo(valor_del_input):
    if not valor_del_input or valor_del_input.strip() == "":
        return "Por favor ingresa un nombre para continuar..."

    return f"¡Hola, {valor_del_input.strip()}! Bienvenido/a al desarrollo de Dashboards reactivos."

if __name__ == "__main__":
    app.run(debug=True)
