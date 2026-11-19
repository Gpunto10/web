# Web de Gema Díez

Web personal (portfolio) publicada con GitHub Pages.

- El contenido y la estructura viven en `_fuente/gen.py` (la foto, en `_fuente/photo.txt`).
- Para cambiar algo: editar `_fuente/gen.py` y ejecutar `python3 _fuente/gen.py`. Genera `index.html`, las páginas de caso y `foto.jpg` en la raíz.
- Imágenes de los casos: originales en `_fuente/imagenes/`; `python3 _fuente/imagenes.py` las recorta en `img/`.
- Los estilos están en `styles.css` (sistema "Luz de cumbre", v0.5).
- Cada cambio que llega a la rama `main` se publica solo en uno o dos minutos.

## Versiones guardadas
- `anterior/`: copia congelada de la web antes de la v7 (17 nov 2026), con las pruebas de color A–D (`anterior/prueba-*.html`). No se regenera con `gen.py`.
- `anterior/v-2026-11-19-antes-accesibilidad/`: la web justo antes de los arreglos de accesibilidad (WCAG 2.1 AA) del 19 nov 2026.
- `anterior/v-2026-11-19-antes-menu/`: la web antes de que el menú de la home pasara a scroll en una sola página y «Hablemos» del menú a «Contacto» (19 nov 2026).
