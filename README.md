# Follow Balance

Follow Balance es una aplicacion web que analiza dos archivos JSON exportados de una cuenta y detecta que usuarios no siguen de vuelta.

## Que hace el programa
- Recibe dos archivos: `followers_1.json` y `following.json`.
- Procesa ambos archivos en memoria y compara seguidores vs seguidos.
- Muestra un resumen con:
  - cantidad de cuentas seguidas,
  - cantidad de seguidores,
  - cantidad de usuarios no reciprocos.
- Presenta la lista de resultados en pantalla.
- Permite abrir cada resultado en su perfil con un enlace directo.
- Permite descargar la lista en formato CSV.

## Como funciona (overview)
- El backend recibe los archivos enviados desde el formulario.
- Se valida que sean JSON y que tengan la estructura esperada.
- Se calcula la diferencia entre los usuarios seguidos y los seguidores.
- Se renderiza la vista con resultados y opciones de exportacion.

## Tecnologias
- **FastAPI**: servidor web y manejo de rutas.
- **Jinja2**: renderizado de templates HTML.
- **Tailwind CSS**: estilos de interfaz (CSS compilado localmente).
- **Python**: logica de parsing y comparacion de datos.

## Nota
El resultado puede incluir cuentas desactivadas.
