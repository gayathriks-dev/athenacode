from flask import Blueprint, render_template, redirect, url_for, flash
from flask_login import current_user, login_required
from app import db
from models import Patient, Record
from forms import PatientForm, RecordForm

patients_bp = Blueprint('patients', __name__)

@patients_bp.route('/dashboard')
@login_required
def dashboard():
    patients = Patient.query.filter_by(user_id=current_user.id).all()
    return render_template('dashboard.html', patients=patients)

@patients_bp.route('/patient/<int:patient_id>')
@login_required
def patient_details(patient_id):
    patient = Patient.query.get_or_404(patient_id)
    records = Record.query.filter_by(patient_id=patient.id).all()
    return render_template('patient_details.html', patient=patient, records=records)

@patients_bp.route('/patient/new', methods=['GET', 'POST'])
@login_required
def new_patient():
    form = PatientForm()
    if form.validate_on_submit():
        patient = Patient(name=form.name.data, dob=form.dob.data, user_id=current_user.id)
        db.session.add(patient)
        db.session.commit()
        flash('Patient has been added!', 'success')
        return redirect(url_for('patients.dashboard'))
    return render_template('new_patient.html', form=form)

@patients_bp.route('/patient/<int:patient_id>/add_record', methods=['GET', 'POST'])
@login_required
def add_record(patient_id):
    form = RecordForm()
    patient = Patient.query.get_or_404(patient_id)
    if form.validate_on_submit():
        record = Record(data=form.data.data, patient_id=patient.id)
        db.session.add(record)
        db.session.commit()
        flash('Record has been added!', 'success')
        return redirect(url_for('patients.patient_details', patient_id=patient.id))
    return render_template('add_record.html', form=form, patient=patient)


