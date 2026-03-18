from flask import Flask
import requests
import numpy as np
from PIL import Image
import io

app = Flask(__name__)
@app.route('/')
def hello():
    return "greetings from my security scanner demo :)"

@app.route('/analyze')
def analyze():
    # dummy image processing
    arr = np.zeros((100, 100, 3), dtype=np.uint8)
    img = Image.fromarray(arr)
    buf = io.BytesIO()
    img.save(buf, format='PNG')
    return f"Processed array of shape {arr.shape}"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
