from flask import Blueprint, flash, redirect, request, url_for
from flask_login import login_required
from werkzeug.utils import secure_filename
import os
from models import Record, Patient  # Assuming these are SQLAlchemy models
from app import db  # Assuming this is the Flask app instance

reports_bp = Blueprint('reports', __name__)

@reports_bp.route('/api/upload', methods=['POST'])
@login_required
def upload():
    if 'file' not in request.files:
        flash('No file part', 'danger')
        return redirect(request.url)

    file = request.files['file']

    if file.filename == '':
        flash('No selected file', 'danger')
        return redirect(request.url)

    if file:
        try:
            filename = secure_filename(file.filename)
            file.save(os.path.join('uploads', filename))
            flash('File uploaded successfully', 'success')
            return redirect(url_for('reports.upload'))  # Redirect to upload page or handle as needed
        except Exception as e:
            flash(f'Error uploading file: {str(e)}', 'danger')
            return redirect(request.url)

    return redirect(request.url)

@reports_bp.route('/api/visualize/<int:patient_id>')
@login_required
def visualize(patient_id):
    patient = Patient.query.get_or_404(patient_id)
    records = Record.query.filter_by(patient_id=patient.id).all()
    # Assuming Record and Patient have appropriate data structure for visualization
    visualization_data = [{'field1': record.field1, 'field2': record.field2} for record in records]  # Example data structure
    return {'visualization_data': visualization_data}
