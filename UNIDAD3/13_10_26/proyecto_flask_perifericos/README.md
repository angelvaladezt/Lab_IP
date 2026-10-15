# Proyecto práctico: panel de periféricos

Aplicación didáctica que utiliza únicamente Python, Flask, HTML, CSS y JavaScript. Flask entrega un documento HTML estático y expone rutas JSON. JavaScript consulta esas rutas y actualiza el contenido del documento.

## Funciones incluidas

- Login de demostración con validación en Python.
- Menú que se construye con datos enviados por Flask.
- Formulario para registrar periféricos.
- Texto, botones, enlace, imagen y opciones cargados desde una ruta JSON.
- Retroalimentación de carga, éxito y error.
- Uso de teclado, foco visible y diseño adaptable.

## Ejecución

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
python app.py
```

En Windows, activa el entorno con:

```powershell
.venv\Scripts\activate
```

Abre `http://127.0.0.1:5000`.

## Acceso de demostración

- Usuario: `alumno`
- Contraseña: `python123`

Estas credenciales sólo sirven para practicar. Una aplicación real debe almacenar contraseñas mediante un hash seguro, usar sesiones y aplicar protección contra intentos repetidos.

## Estructura

```text
proyecto_flask_perifericos/
├── app.py
├── requirements.txt
└── static/
    ├── index.html
    ├── css/styles.css
    ├── js/app.js
    ├── images/ingenieria_software.png
    └── fonts/
```

## Flujo de datos

1. El navegador solicita `/` y Flask entrega `static/index.html`.
2. JavaScript solicita `/api/config` y recibe JSON.
3. JavaScript coloca los valores en propiedades como `textContent`, `src` y `href`.
4. Login y formulario envían JSON con `fetch()`.
5. Python valida los datos y devuelve JSON con un código HTTP apropiado.
