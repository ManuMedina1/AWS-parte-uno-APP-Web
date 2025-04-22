# 🎉 Fechas Importantes - Aplicación Web en Flask 🚀

## 📌 Descripción
Esta es una **aplicación web simple** creada con **Flask** y **PostgreSQL** en AWS RDS. Su propósito es **guardar y mostrar fechas importantes**, como cumpleaños, días festivos, aniversarios, etc.  

Los usuarios pueden:  
✅ **Ver una lista de fechas importantes** guardadas en la base de datos.  
✅ **Agregar nuevas fechas** mediante un formulario intuitivo.  
✅ **Ejecutar la aplicación localmente o en una instancia EC2** de AWS.  

---

## 🏗️ Estructura del Proyecto
```
mi_app_fechas/
├── app.py              # Código principal en Flask
├── templates/          # Carpeta con archivos HTML
│   ├── index.html      # Página principal
│   ├── agregar.html    # Página para añadir nuevas fechas
├── static/             # Archivos estáticos (CSS)
│   ├── styles.css      # Estilos de la aplicación
├── requirements.txt    # Dependencias de Python
└── README.md           # Documentación del proyecto
```

---

## ⚙️ Instalación y Configuración

### 1️⃣ **Clonar el repositorio**
```bash
git clone https://github.com/tu_usuario/mi_app_fechas.git
cd mi_app_fechas
```

### 2️⃣ **Instalar dependencias**
```bash
pip install -r requirements.txt
```

### 3️⃣ **Configurar la conexión con RDS**  
📌 En `app.py`, edita estos valores con los datos de tu base de datos en **AWS RDS**:
```python
db = psycopg2.connect(
    host="tu-endpoint-rds.amazonaws.com",
    user="admin",
    password="tu_contraseña",
    database="mi_base_de_datos"
)
```

### 4️⃣ **Ejecutar la aplicación**
```bash
python3 app.py
```
Accede a la aplicación desde el navegador en:
```
http://127.0.0.1:5000/
```

---

## 🎨 Diseño y Estilos
La aplicación usa un diseño **simple pero vistoso** con CSS. Se incluyen:  
✅ **Fondos degradados** para un look moderno.  
✅ **Efectos en botones y tarjetas** para mejorar la experiencia.  
✅ **Diseño minimalista** con colores cálidos y legibles.  

---

## 🚀 Despliegue en AWS EC2
Para ejecutar en EC2 y servir la aplicación en **puerto 80**:  
1️⃣ Instalar **Nginx** en tu instancia:
   ```bash
   sudo apt install nginx -y
   ```
2️⃣ Configurar un **proxy inverso** para que Flask trabaje con Nginx.
3️⃣ Ajustar reglas de seguridad en AWS para permitir tráfico HTTP.

---

## 📜 Licencia
Este proyecto es libre de uso y mejora. ¡Si tienes ideas para expandirlo, haz un **pull request**! 🚀  

---

## 🛠️ Creadores
🔹 **Infraestructura en AWS:** **Manuel (el dueño del repo)** 👨‍💻  
🔹 **Desarrollo de la App Web:** **Copilot (Tu Compañero de Código)** 🤖  
