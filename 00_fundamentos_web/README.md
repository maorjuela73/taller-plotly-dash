# Módulo 0: Fundamentos Web y el Árbol DOM

Antes de escribir código en Dash, es vital entender cómo los navegadores representan una página web.

## ¿Qué es el DOM (Document Object Model)?

Cuando un navegador lee un archivo HTML, no lo ve solo como texto: construye un **árbol de nodos en memoria** donde cada etiqueta (`<div>`, `<h1>`, `<p>`) es una caja o "nodo" hijo de otra caja.

## Instrucciones del Ejercicio

1. Abre el archivo `ejemplo_dom.html` haciendo doble clic en él para abrirlo en tu navegador.
2. Presiona `F12` (o clic derecho -> **Inspeccionar**) para abrir las herramientas de desarrollador (**DevTools**).
3. Dirígete a la pestaña **Elementos** (Elements). Verás el árbol DOM completo.
4. Despliega la etiqueta `<main id="contenedor-posts">`.
5. Haz clic en el botón azul **"+ Agregar Post"**.
6. Observa cómo en la pestaña de Elementos se inserta un nuevo nodo `<article>` en tiempo real y cómo cambia el contador del footer sin recargar la página.
