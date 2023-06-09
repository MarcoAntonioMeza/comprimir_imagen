import os
import datetime

from flask import Flask, request, jsonify, render_template, send_file
from PIL import Image
"""
ruta_actual = os.path.dirname(os.path.abspath(__file__))
carpeta = "images/"
imagen = f"{carpeta}\\descarga.jpg"
"""



app = Flask('__name__')

CARPETA_IMAGENES = 'images/'
app.config['UPLOAD_FOLDER'] = CARPETA_IMAGENES


@app.route('/', methods = ['GET', 'POST'])
def index():
    if request.method == "POST":
        imagen = request.files['imagen']
        ruta_imagen = os.path.join(app.config['UPLOAD_FOLDER'], imagen.filename)
        
        imagen.save(ruta_imagen)

        imagen_comprimida = comprimir(ruta_imagen)
        
        #return jsonify({'msg': ruta_imagen})
        return send_file(imagen_comprimida, mimetype='image/jpeg')
    else:
        return render_template('index.html')

def comprimir(ruta):

    img = Image.open(ruta)
    
    extencion = "jpg"
    ruta_salida = "new_img/"

    if not os.path.exists(ruta_salida):
        os.makedirs(ruta_salida)
    
    if img.format in ['PNG', 'JPG', 'JPEG', 'WEBP']:

        fecha = datetime.datetime.now().date()
        hora_actual = datetime.datetime.now()
        hora_formateada = hora_actual.strftime('%H:%M:%S').replace(":", "-")

        nombre = f"img-{fecha}-{hora_formateada}.{extencion}"

        img = img.convert('RGB')

        img.save(f"{ruta_salida}{nombre}",optimize=True, quality=75)
        
        return f"{ruta_salida}{nombre}"

        


if __name__ == '__main__':

    app.run(debug=True)
    
    #comprimir(imagen)
    
