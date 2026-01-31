from flask import Flask, request, jsonify, render_template
import tensorflow as tf
import numpy as np
from PIL import Image
import json
import io
import os
import gdown

app = Flask(__name__)

# Download model from Google Drive if not exists
MODEL_FILE = 'pokedex_model.h5'
if not os.path.exists(MODEL_FILE):
    print("Downloading model from Google Drive...")
    file_id = 'YOUR_FILE_ID_HERE'  # Replace with your FILE_ID
    url = f'https://drive.google.com/file/d/1AP-v-ZnMGo82MZvlpPS15nAJC8_kSk-z/view?usp=drive_link'
    gdown.download(url, MODEL_FILE, quiet=False)
    print("Model downloaded!")

# Load model and labels
model = tf.keras.models.load_model(MODEL_FILE)
with open('label_map.json', 'r') as f:
    label_map = json.load(f)

reverse_map = {v: k for k, v in label_map.items()}

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if 'file' not in request.files:
        return jsonify({'error': 'No file uploaded'}), 400
    
    file = request.files['file']
    
    img = Image.open(io.BytesIO(file.read()))
    
    if img.mode == 'RGBA':
        background = Image.new("RGB", img.size, (255, 255, 255))
        background.paste(img, mask=img.split()[3])
        img = background
    elif img.mode != 'RGB':
        img = img.convert('RGB')
    
    img = img.resize((224, 224))
    img_array = np.array(img) / 255.0
    img_array = np.expand_dims(img_array, axis=0)
    
    prediction = model.predict(img_array)
    pred_idx = np.argmax(prediction)
    confidence = float(prediction[0][pred_idx] * 100)
    pokemon_name = reverse_map[pred_idx]
    
    top3_idx = np.argsort(prediction[0])[-3:][::-1]
    top3 = []
    for idx in top3_idx:
        top3.append({
            'name': reverse_map[idx],
            'confidence': float(prediction[0][idx] * 100)
        })
    
    return jsonify({
        'pokemon': pokemon_name,
        'confidence': confidence,
        'top3': top3
    })

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)