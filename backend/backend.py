import flask
from flask import Flask, request
from flask_cors import CORS, cross_origin
from PIL import Image
app = Flask(__name__)
CORS(app)

image = Image.open('8bit-cloud-resize.jpg')
pixels = list(iter(image.getdata()))


@app.route("/pixel")
def pixel():
    index = int(request.args.get('index'))
    r = pixels[index][0]
    g = pixels[index][1]
    b = pixels[index][2]
    return flask.jsonify({ 'r': r, 'b': b, 'g': g })

if __name__ == '__main__':
    app.run()
