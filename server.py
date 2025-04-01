from flask import Flask, send_from_directory, jsonify, redirect
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)

# Define la carpeta donde se almacenarán los archivos de actualización (por ejemplo, el APK)
UPLOAD_FOLDER = 'updates'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Asegúrate de que la carpeta de carga exista
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

# URL pública donde has alojado tu archivo APK en MediaFire
APK_PUBLIC_URL = 'https://download937.mediafire.com/sngpruhodv2gStOIX2W25bIS9z01nJ2UTEqX_9XQ3YxsOJT-HdOaLGiy6enVwTzvtLQBDcd4GeQIlVNp7lZNDBYkr3tkXSc8qEk2saEamcnXuKkIFk-yxLoXUfIxzSzKDxX5FUkvB_yMPVf4wvVegcEi8d7yf3fJzgHXLPw1zp_8zwg/xw0pegnmiwta7zl/app.apk'

# Ruta para redirigir a la URL pública del APK
@app.route('/download_apk')
def download_apk():
    return redirect(APK_PUBLIC_URL)

# API endpoint para verificar si hay una nueva versión disponible
@app.route('/api/check_update')
def check_update():
    # Aquí podrías tener lógica más compleja para comparar versiones
    # Por ahora, simplemente indicamos que siempre hay una actualización disponible para simplificar
    update_available = True
    return jsonify({
        'update_available': update_available,
        'download_url': '/download_apk'
    })

if __name__ == '__main__':
    app.run(debug=True, port=5000)