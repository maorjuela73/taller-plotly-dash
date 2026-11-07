"""
EJERCICIO 2 (SOLUCIÓN): Controles Interactivos con Dash Core Components (dcc)
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
    html.P("Controles interactivos y visor de gráficos integrados en el layout:"),

    html.Label("Selecciona una Especie:", style={"fontWeight": "bold", "marginTop": "10px", "display": "block"}),
    dcc.Dropdown(
        id="filtro-especie",
        options=[
            {"label": "Todas las especies", "value": "TODAS"},
            {"label": "Setosa", "value": "setosa"},
            {"label": "Versicolor", "value": "versicolor"},
            {"label": "Virginica", "value": "virginica"}
        ],
        value="TODAS",
        clearable=False
    ),

    html.Label("Largo mínimo del sépalo:", style={"fontWeight": "bold", "marginTop": "15px", "display": "block"}),
    dcc.Slider(
        id="slider-longitud",
        min=4,
        max=8,
        step=0.5,
        value=5,
        marks={i: f"{i}" for i in range(4, 9)}
    ),

    html.Div(style={"marginTop": "20px"}, children=[
        dcc.Graph(
            id="grafico-iris",
            figure=figura_iris
        )
    ])
])

if __name__ == "__main__":
    app.run(debug=True)
