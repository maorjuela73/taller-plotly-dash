"""
EJERCICIO 4 (SOLUCIÓN): Dashboard Analítico Gapminder Completo
"""

from dash import Dash, html, dcc, Input, Output
import plotly.express as px

app = Dash(__name__)

df = px.data.gapminder()
continentes_lista = sorted(df["continent"].unique())
anios_lista = sorted(df["year"].unique())

app.layout = html.Div(style={"maxWidth": "1000px", "margin": "0 auto", "padding": "20px", "fontFamily": "Segoe UI, sans-serif"}, children=[
    html.H1("Explorador Socioeconómico Global", style={"textAlign": "center", "color": "#0f172a"}),
    html.P("Filtra el continente y el año para examinar la relación entre ingresos y longevidad.", style={"textAlign": "center", "color": "#64748b"}),
    html.Hr(style={"margin": "20px 0"}),

    html.Div(style={"display": "flex", "gap": "20px", "marginBottom": "20px"}, children=[
        html.Div(style={"flex": "1"}, children=[
            html.Label("1. Selecciona un Continente:", style={"fontWeight": "bold", "color": "#334155"}),
            dcc.Dropdown(
                id="filtro-continente",
                options=[{"label": c, "value": c} for c in continentes_lista],
                value="Americas",
                clearable=False
            )
        ]),
        html.Div(style={"flex": "1"}, children=[
            html.Label("2. Selecciona un Año:", style={"fontWeight": "bold", "color": "#334155"}),
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

    html.Div(
        id="panel-metricas",
        style={
            "padding": "12px 20px",
            "backgroundColor": "#f1f5f9",
            "borderRadius": "6px",
            "marginBottom": "20px",
            "fontWeight": "600",
            "color": "#1e293b"
        }
    ),

    dcc.Graph(id="grafico-gapminder")
])

@app.callback(
    [
        Output("grafico-gapminder", "figure"),
        Output("panel-metricas", "children")
    ],
    [
        Input("filtro-continente", "value"),
        Input("filtro-anio", "value")
    ]
)
def actualizar_dashboard(continente_elegido, anio_elegido):
    df_filtrado = df[(df["continent"] == continente_elegido) & (df["year"] == anio_elegido)]

    figura = px.scatter(
        df_filtrado,
        x="gdpPercap",
        y="lifeExp",
        size="pop",
        color="country",
        hover_name="country",
        log_x=True,
        size_max=45,
        title=f"PIB per cápita vs Expectativa de Vida en {continente_elegido} ({anio_elegido})",
        labels={
            "gdpPercap": "PIB per cápita (USD - escala log)",
            "lifeExp": "Expectativa de vida (años)",
            "pop": "Población"
        }
    )
    figura.update_layout(template="plotly_white", transition_duration=350)

    total_paises = len(df_filtrado)
    expectativa_promedio = df_filtrado["lifeExp"].mean() if total_paises > 0 else 0
    texto_resumen = f"Mostrando {total_paises} países de {continente_elegido}. Expectativa de vida promedio: {expectativa_promedio:.1f} años."

    return figura, texto_resumen

if __name__ == "__main__":
    app.run(debug=True)
