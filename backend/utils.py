import pandas as pd
from app import db
from models import Patient, Record

def process_csv(file):
    data = pd.read_csv(file)
    for _, row in data.iterrows():
        patient = Patient.query.filter_by(name=row['name']).first()
        if not patient:
            patient = Patient(name=row['name'], dob=row['dob'])
            db.session.add(patient)
            db.session.commit()
        record = Record(patient_id=patient.id, data=row['data'])
        db.session.add(record)
        db.session.commit()
