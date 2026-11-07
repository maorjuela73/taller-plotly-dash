"""
EJERCICIO 2 (ESTUDIANTE): Controles Interactivos con Dash Core Components (dcc)
"""

from dash import Dash, html, dcc
import plotly.express as px

app = Dash(__name__)

df_iris = px.data.iris()
figura_iris = px.scatter(
    df_iris,
    x="sepal_width",
    y="sepal_length",
    color="species",
    title="Distribución: Largo vs Ancho del Sépalo",
    labels={"sepal_width": "Ancho del Sépalo", "sepal_length": "Largo del Sépalo"}
)
figura_iris.update_layout(template="plotly_white")

app.layout = html.Div(style={"maxWidth": "900px", "margin": "30px auto", "fontFamily": "sans-serif"}, children=[
    html.H2("Exploración con Dash Core Components", style={"color": "#0f172a"}),
    html.P("Agrega controles interactivos antes del gráfico."),

    # -------------------------------------------------------------------------
    # RETO 1: Define un dcc.Dropdown con id="filtro-especie"
    # Opciones: 'setosa', 'versicolor', 'virginica' o 'TODAS'.
    # -------------------------------------------------------------------------
    html.Label("Selecciona una Especie:", style={"fontWeight": "bold", "marginTop": "10px", "display": "block"}),
    # TODO: Descomenta y completa:
    # dcc.Dropdown(
    #     id=...,
    #     options=[...],
    #     value="TODAS",
    #     clearable=False
    # ),

    # -------------------------------------------------------------------------
    # RETO 2: Define un dcc.Slider con id="slider-longitud"
    # Rango de 4 a 8, saltos de 0.5 y valor inicial 5.
    # -------------------------------------------------------------------------
    html.Label("Largo mínimo del sépalo:", style={"fontWeight": "bold", "marginTop": "15px", "display": "block"}),
    # TODO: Descomenta y completa:
    # dcc.Slider(
    #     id=...,
    #     min=...,
    #     max=...,
    #     step=...,
    #     value=...
    # ),

    # -------------------------------------------------------------------------
    # RETO 3: Integra 'figura_iris' dentro de un dcc.Graph.
    # -------------------------------------------------------------------------
    html.Div(style={"marginTop": "20px"}, children=[
        # TODO: Descomenta y completa:
        # dcc.Graph(
        #     id="grafico-iris",
        #     figure=...
        # )
    ])
])

if __name__ == "__main__":
    app.run(debug=True)
