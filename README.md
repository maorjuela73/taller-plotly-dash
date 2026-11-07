# Taller Práctico: Dashboards con Plotly Dash en Python

Repositorio oficial del taller práctico de 2 horas. Aprende a construir aplicaciones analíticas interactivas en la web sin escribir JavaScript.

## Requisitos previos
* Python 3.9 o superior instalado.
* Editor de código (VS Code, PyCharm o Cursor recomendado).
* Navegador web moderno (Chrome, Edge, Firefox).

## Instalación y Configuración

1. Clona este repositorio o descomprime el archivo `.zip`:
   ```bash
   git clone https://github.com/maorjuela73/taller-plotly-dash.git
   cd taller-plotly-dash
   ```

2. Crea y activa un entorno virtual (recomendado):
   ```bash
   # En Windows
   python -m venv venv
   venv\Scripts\activate

   # En macOS/Linux
   python3 -m venv venv
   source venv/bin/activate
   ```

3. Instala las dependencias:
   ```bash
   pip install -r requirements.txt
   ```

## Estructura de las Carpetas

Cada carpeta temática contiene:

* `README.md`: Explicación conceptual, objetivos y guía del ejercicio.
* `estudiante.py`: Plantilla con comentarios guía (`TODO` / `RETO`) para que programes durante la sesión.
* `solucion.py`: Código completo y funcional para validar tus respuestas si te bloqueas.

| Carpeta | Tema | Duración |
| --- | --- | --- |
| `00_fundamentos_web` | El Árbol DOM, etiquetas e inspección web con F12 | 20 min |
| `01_dash_html` | Plantilla básica y componentes de maquetado (`dash.html`) | 25 min |
| `02_dcc_componentes` | Controles de formulario y gráficos (`dash.dcc`) | 30 min |
| `03_callbacks_basicos` | Decoradores y reactividad (`Input` -> `Output`) | 25 min |
| `04_proyecto_integrador` | Dashboard multi-filtro con Gapminder | 20 min |
