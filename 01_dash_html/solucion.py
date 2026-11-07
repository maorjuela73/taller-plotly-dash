"""
EJERCICIO 1 (SOLUCIÓN): Construyendo una Maqueta con Dash HTML Components
"""

from dash import Dash, html

app = Dash(__name__)

estilos_contenedor = {
    "maxWidth": "850px",
    "margin": "40px auto",
    "padding": "30px",
    "backgroundColor": "#f8fafc",
    "borderRadius": "10px",
    "boxShadow": "0 4px 6px -1px rgba(0, 0, 0, 0.1)",
    "fontFamily": "Segoe UI, Tahoma, Geneva, Verdana, sans-serif"
}

app.layout = html.Div(
    style=estilos_contenedor,
    children=[
        html.H1(
            "Mi Primer Dashboard con Dash",
            style={"textAlign": "center", "color": "#1e3a8a", "marginBottom": "10px"}
        ),
        html.P(
            "Dash traduce objetos nativos de Python a componentes HTML y React.js "
            "funcionales en cualquier navegador web moderno.",
            style={"color": "#475569", "fontSize": "16px", "lineHeight": "1.5"}
        ),
        html.Hr(style={"border": "0", "borderTop": "1px solid #cbd5e1", "margin": "20px 0"}),
        html.Div(
            style={"display": "flex", "justifyContent": "space-between", "alignItems": "center"},
            children=[
                html.Span(
                    "Estado: Plantilla estática cargada correctamente",
                    style={"color": "#059669", "fontWeight": "bold"}
                ),
                html.A(
                    "Ver Documentación Oficial",
                    href="https://dash.plotly.com/dash-html-components",
                    target="_blank",
                    style={"color": "#2563eb", "textDecoration": "none"}
                )
            ]
        )
    ]
)

if __name__ == "__main__":
    app.run(debug=True)
