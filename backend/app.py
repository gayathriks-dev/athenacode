from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
from werkzeug.utils import secure_filename
import os
from pathlib import Path

app = Flask(__name__)
CORS(app)

UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['SECRET_KEY'] = 'your_secret_key_here'  # Replace with your secret key

@app.route('/api/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return 'No file part', 400
    file = request.files['file']
    if file.filename == '':
        return 'No selected file', 400
    if file:
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        return 'File uploaded successfully', 200

@app.route('/api/visualize/<int:patient_id>', methods=['GET'])
def visualize_data(patient_id):
    # Placeholder for data retrieval and visualization logic
    # Replace with actual logic to fetch and process CSV data
    # For demonstration, send back dummy data
    dummy_data = [{'id': 1, 'name': 'John Doe', 'age': 30}, {'id': 2, 'name': 'Jane Smith', 'age': 25}]
    return jsonify({'visualization_data': dummy_data})

if __name__ == '__main__':
    app.run(debug=True)
