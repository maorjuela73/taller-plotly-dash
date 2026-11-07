"""
EJERCICIO 4 (ESTUDIANTE): Dashboard Analítico Gapminder Completo
"""

from dash import Dash, html, dcc, Input, Output
import plotly.express as px

app = Dash(__name__)

df = px.data.gapminder()
continentes_lista = sorted(df["continent"].unique())
anios_lista = sorted(df["year"].unique())

app.layout = html.Div(style={"maxWidth": "1000px", "margin": "0 auto", "padding": "20px", "fontFamily": "sans-serif"}, children=[
    html.H1("Explorador Socioeconómico Global", style={"textAlign": "center", "color": "#0f172a"}),
    html.Hr(),

    html.Div(style={"display": "flex", "gap": "20px", "marginBottom": "20px"}, children=[
        html.Div(style={"flex": "1"}, children=[
            html.Label("1. Selecciona un Continente:", style={"fontWeight": "bold"}),
            dcc.Dropdown(
                id="filtro-continente",
                options=[{"label": c, "value": c} for c in continentes_lista],
                value="Americas",
                clearable=False
            )
        ]),
        html.Div(style={"flex": "1"}, children=[
            html.Label("2. Selecciona un Año:", style={"fontWeight": "bold"}),
            dcc.Slider(
                id="filtro-anio",
                min=int(min(anios_lista)),
                max=int(max(anios_lista)),
                step=None,
                value=2007,
                marks={int(a): str(a) for a in anios_lista if a % 10 == 2 or a == 2007}
            )
        ])
    ]),

    html.Div(id="panel-metricas", style={"padding": "12px", "backgroundColor": "#f1f5f9", "borderRadius": "6px", "marginBottom": "15px", "fontWeight": "bold"}),

    dcc.Graph(id="grafico-gapminder")
])

# -----------------------------------------------------------------------------
# RETO: Completa el callback con 2 Outputs y 2 Inputs:
# Outputs: ("grafico-gapminder", "figure") y ("panel-metricas", "children")
# Inputs: ("filtro-continente", "value") y ("filtro-anio", "value")
# -----------------------------------------------------------------------------
# @app.callback(
#     [Output(...), Output(...)],
#     [Input(...), Input(...)]
# )
def actualizar_dashboard(continente_elegido, anio_elegido):
    # TODO 1: Filtra 'df' por 'continente_elegido' y 'anio_elegido'
    # TODO 2: Crea el gráfico px.scatter con x="gdpPercap", y="lifeExp", size="pop", color="country", log_x=True
    # TODO 3: Calcula el promedio de expectativa de vida y arma un texto resumen
    # TODO 4: Retorna figura, texto_resumen
    pass

if __name__ == "__main__":
    app.run(debug=True)
