from flask import Flask, jsonify, request


app = Flask(__name__, static_folder="static", static_url_path="")

USUARIO_DEMO = {
    "usuario": "alumno",
    "clave": "python123",
    "nombre": "Estudiante de Ingeniería de Software",
}

CONFIGURACION = {
    "titulo": "Panel de periféricos",
    "subtitulo": "Interfaz construida con HTML, CSS, JavaScript, Flask y Python",
    "mensaje_bienvenida": "Inicia sesión para consultar el menú y registrar un periférico.",
    "botones": {
        "login": "Ingresar",
        "guardar": "Guardar periférico",
    },
    "enlace": {
        "texto": "Ver los datos que entrega Python",
        "url": "/api/config",
    },
    "imagen": {
        "src": "/images/ingenieria_software.png",
        "alt": "Identidad gráfica de Ingeniería de Software",
    },
    "menu": [
        {"id": "inicio", "texto": "Inicio"},
        {"id": "registro", "texto": "Formulario"},
        {"id": "ayuda", "texto": "Ayuda"},
    ],
    "tipos": ["Teclado", "Mouse", "Monitor", "Impresora", "Otro"],
}

REGISTROS = [
    {"id": 1, "nombre": "Teclado principal", "tipo": "Teclado", "cantidad": 1}
]


@app.get("/")
def inicio():
    """Entrega el documento HTML estático de la aplicación."""
    return app.send_static_file("index.html")


@app.get("/api/config")
def obtener_configuracion():
    """Expone textos, enlace, imagen, botones y opciones de menú como JSON."""
    return jsonify(CONFIGURACION)


@app.post("/api/login")
def iniciar_sesion():
    datos = request.get_json(silent=True) or {}
    usuario = str(datos.get("usuario", "")).strip()
    clave = str(datos.get("clave", ""))

    if not usuario or not clave:
        return jsonify(ok=False, mensaje="Completa usuario y contraseña."), 400

    credenciales_validas = (
        usuario == USUARIO_DEMO["usuario"]
        and clave == USUARIO_DEMO["clave"]
    )
    if not credenciales_validas:
        return jsonify(ok=False, mensaje="Credenciales incorrectas."), 401

    return jsonify(
        ok=True,
        mensaje="Acceso correcto.",
        usuario={"nombre": USUARIO_DEMO["nombre"]},
        menu=CONFIGURACION["menu"],
    )


@app.get("/api/perifericos")
def listar_perifericos():
    return jsonify(registros=REGISTROS, total=len(REGISTROS))


@app.post("/api/perifericos")
def registrar_periferico():
    datos = request.get_json(silent=True) or {}
    nombre = str(datos.get("nombre", "")).strip()
    tipo = str(datos.get("tipo", "")).strip()

    try:
        cantidad = int(datos.get("cantidad", 0))
    except (TypeError, ValueError):
        cantidad = 0

    errores = {}
    if len(nombre) < 3:
        errores["nombre"] = "Escribe al menos 3 caracteres."
    if tipo not in CONFIGURACION["tipos"]:
        errores["tipo"] = "Selecciona un tipo válido."
    if cantidad < 1 or cantidad > 50:
        errores["cantidad"] = "La cantidad debe estar entre 1 y 50."

    if errores:
        return jsonify(ok=False, errores=errores), 400

    registro = {
        "id": len(REGISTROS) + 1,
        "nombre": nombre,
        "tipo": tipo,
        "cantidad": cantidad,
    }
    REGISTROS.append(registro)
    return jsonify(ok=True, mensaje="Periférico guardado.", registro=registro), 201


if __name__ == "__main__":
    app.run(debug=True)
