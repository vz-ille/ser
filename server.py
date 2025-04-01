from flask import Flask, jsonify
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)

@app.route('/api/check_update')
def check_update():
    updates_folder = os.path.join(os.getcwd(), 'updates')
    apk_path = os.path.join(updates_folder, 'app.apk')

    if os.path.exists(apk_path):
        update_available = True
        download_url = '/updates/app.apk'  # La URL relativa para descargar el APK
    else:
        update_available = False
        download_url = None

    return jsonify({
        'update_available': update_available,
        'version_code': 2,  # Puedes ajustar esto según tu lógica de versiones
        'download_url': download_url
    })

@app.route('/updates/<filename>')
def updates(filename):
    updates_folder = os.path.join(os.getcwd(), 'updates')
    return send_from_directory(updates_folder, filename)

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=True, port=port, host='0.0.0.0')