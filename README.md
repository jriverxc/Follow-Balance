# Follow Balance

Aplicacion web para comparar dos archivos JSON exportados de tu cuenta y detectar usuarios que no te siguen de vuelta.

## Funcionalidades
- Carga de archivos `followers_1.json` y `following.json` desde el navegador.
- Analisis inmediato con resumen de cuentas.
- Lista de usuarios que no te siguen con enlace directo al perfil.
- Descarga de resultados en CSV.
- Panel de ayuda desplegable con pasos de exportacion.

## Stack
- FastAPI
- Jinja2
- Tailwind CSS compilado localmente (sin CDN)

## Requisitos
- Python 3.10+
- Node.js 18+

## Instalacion
Instala dependencias de backend:
```bash
python -m pip install -r requirements.txt
```

Instala dependencias de frontend:
```bash
npm install
```

## Desarrollo
Compila Tailwind en modo watch (terminal 1):
```bash
npm run css:watch
```

Levanta FastAPI (terminal 2):
```bash
python manage.py
```

URL local:
- `http://127.0.0.1:8000`

## Build de CSS para produccion
```bash
npm run css:build
```
Genera `app/static/css/tailwind.css` minificado.

## Estructura
```text
.
|-- app/
|   |-- main.py
|   |-- routes.py
|   |-- services/
|   |   `-- unfollow.py
|   |-- templates/
|   |   |-- base.html
|   |   `-- index.html
|   `-- static/
|       |-- logo.png
|       `-- css/
|           |-- tailwind.css
|           `-- src/
|               `-- tailwind.css
|-- manage.py
|-- requirements.txt
|-- package.json
|-- tailwind.config.js
`-- .gitignore
```

## Endpoints
- `GET /`: pantalla principal.
- `POST /`: analiza archivos y muestra resultados.
- `POST /download-csv`: descarga CSV con usuarios no reciprocos.

## Notas
- El resultado puede incluir cuentas desactivadas.
- Los archivos se procesan en memoria durante la solicitud.
