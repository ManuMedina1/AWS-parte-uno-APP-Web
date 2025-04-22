import psycopg2
from flask import Flask, render_template, request, redirect

app = Flask(__name__)

# Conectar a PostgreSQL en RDS
db = psycopg2.connect(
    host="tu-endpoint-rds.amazonaws.com",
    user="admin",
    password="tu_contraseña",
    database="mi_base_de_datos"
)

@app.route("/")
def mostrar_fechas():
    cursor = db.cursor()
    cursor.execute("SELECT nombre, fecha FROM fechas_importantes ORDER BY fecha ASC")
    datos = cursor.fetchall()
    cursor.close()
    return render_template("index.html", fechas=datos)

@app.route("/agregar", methods=["GET", "POST"])
def agregar_fecha():
    if request.method == "POST":
        nombre = request.form["nombre"]
        fecha = request.form["fecha"]
        cursor = db.cursor()
        cursor.execute("INSERT INTO fechas_importantes (nombre, fecha) VALUES (%s, %s)", (nombre, fecha))
        db.commit()
        cursor.close()
        return redirect("/")
    return render_template("agregar.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
