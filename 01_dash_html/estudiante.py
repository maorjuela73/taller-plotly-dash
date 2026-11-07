"""
EJERCICIO 1 (ESTUDIANTE): Construyendo una Maqueta con Dash HTML Components
"""

from dash import Dash, html

app = Dash(__name__)

# -----------------------------------------------------------------------------
# RETO 1: Define los estilos para el contenedor principal usando camelCase.
# -----------------------------------------------------------------------------
estilos_contenedor = {
    "maxWidth": "850px",
    "margin": "40px auto",
    "padding": "30px",
    # TODO: Agrega un color de fondo claro ("backgroundColor": "#f8fafc")
    # TODO: Agrega bordes redondeados ("borderRadius": "10px")
    # TODO: Aplica una tipografía moderna ("fontFamily": "Segoe UI, sans-serif")
}

# -----------------------------------------------------------------------------
# RETO 2: Define el árbol de componentes dentro de app.layout.
# -----------------------------------------------------------------------------
app.layout = html.Div(
    style=estilos_contenedor,
    children=[
        # TODO: Agrega un html.H1 con el texto "Mi Primer Dashboard con Dash"
        # y estilo centrado con color "#1e3a8a"

        # TODO: Agrega un párrafo informativo (html.P) explicando qué es Dash

        # TODO: Agrega una línea divisoria usando html.Hr()

        # TODO: Crea un contenedor html.Div que agrupe:
        #   1. Un html.Span que diga "Estado: Plantilla activa"
        #   2. Un html.A que enlace a "https://dash.plotly.com" con target="_blank"
    ]
)

if __name__ == "__main__":
    app.run(debug=True)
