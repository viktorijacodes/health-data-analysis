
# listor med medicin som används i analysen
diabetes_meds = ["Metformin"]
heart_meds = ["Enalapril", "Metoprolol"]

# Parent class med relevanta atributer för alla patienter
class Patient:
    def __init__(self, patient_id):
        self.patient_id = patient_id
        self.dates = []
        self.medication_start = None
        

# Child class för analys av glukos
class DiabetesPatient(Patient):
    def __init__(self, patient_id):
        super().__init__(patient_id)
        self.glucose = []
        self.unmedicated_glucose = []
        self.medicated_glucose = []

    # beräknar skillnaden mellan glukos före och efter medicinering
    def calculate_glucose_results(self):
        unmedicated_glucose_avg = sum(self.unmedicated_glucose) / len(self.unmedicated_glucose)
        medicated_glucose_avg = sum(self.medicated_glucose) / len(self.medicated_glucose)
        
        diff_glucose = unmedicated_glucose_avg - medicated_glucose_avg
        
        if diff_glucose > 0:
            change = "decreased"
        elif diff_glucose < 0:
            change = "increased"
        else:
            change = "no change"
        
        return {
            'unmedicated_avg': unmedicated_glucose_avg,
            'medicated_avg': medicated_glucose_avg,
            'difference': diff_glucose,
            'change': change
        }


# Child class för puls analys
class HeartPatient(Patient):
    def __init__(self, patient_id):
        super().__init__(patient_id)
        self.pulse = []
        self.unmedicated_pulse = []
        self.medicated_pulse = []

    # Beräknar skillnaden mellan puls före och efter medicineringen
    def calculate_pulse_results(self):
        unmedicated_pulse_avg = sum(self.unmedicated_pulse) / len(self.unmedicated_pulse)
        medicated_pulse_avg = sum(self.medicated_pulse) / len(self.medicated_pulse)
             
        diff_pulse = unmedicated_pulse_avg - medicated_pulse_avg
    
        if diff_pulse > 0:
            change = "decreased"
        elif diff_pulse < 0:
            change = "increased"
        else:
            change = "no change"
    
        return {
            'unmedicated_avg': unmedicated_pulse_avg,
            'medicated_avg': medicated_pulse_avg,
            'difference': diff_pulse,
            'change': change
        }


def analyze_glucose(data):
    # organiserar data efter patient-id
    patients = {}

    for row in data: 
        patient_id = row['patient_id']

        if patient_id not in patients:
            # Skapar ett patientobjekt första gången patient id hittas
            patient = DiabetesPatient(patient_id) 
            # Sparar patientobjektet med patient id som nyckel
            patients[patient_id] = patient 

        patient = patients[patient_id]

        # sorterar glukosvärden beroende om patient fått medicin eller inte
        if row['medication'] == 'none': 
            patient.unmedicated_glucose.append(float(row['glucose']))
        elif row['medication'] in diabetes_meds:
            patient.medicated_glucose.append(float(row['glucose']))

        # sparar datum och glukosvärden för visualisering
        patient.dates.append(row['date'])
        patient.glucose.append(float(row['glucose']))

        if row['medication'] != 'none' and patient.medication_start is None:
            patient.medication_start = row['date']

    # sparar all resultat i en dict som jag fått från loopet
    results = {}

    for patient_id in patients:
        current_patient_data = patients[patient_id]

        if current_patient_data.medicated_glucose:
            glucose_results = current_patient_data.calculate_glucose_results()

            results[patient_id] = {
                'unmedicated_avg': glucose_results['unmedicated_avg'],
                'medicated_avg': glucose_results['medicated_avg'],
                'difference': glucose_results['difference'],
                'change' : glucose_results['change'],
                'dates': current_patient_data.dates,
                'glucose': current_patient_data.glucose,
                'medication_start': current_patient_data.medication_start
            }

    return results


def analyze_pulse(data):
    # Sorterar patientdata efter patient-id
    patients = {}

    for row in data: 
        patient_id = row['patient_id']

        if patient_id not in patients:
            # skapar ett patientobjekt första gången patient-id hittas
            patient = HeartPatient(patient_id)
            patients[patient_id] = patient

        patient = patients[patient_id]
        
        if row['medication'] == 'none':
            patient.unmedicated_pulse.append(float(row['heart_rate']))
        elif row['medication'] in heart_meds:
            patient.medicated_pulse.append(float(row['heart_rate']))

        patient.dates.append(row['date'])
        patient.pulse.append(float(row['heart_rate']))

        if row['medication'] != 'none' and patient.medication_start is None:
            patient.medication_start = row['date']

    results = {}

    # organizerar och analyserar data
    for patient_id in patients:
        current_patient_data = patients[patient_id]

        if current_patient_data.medicated_pulse:
            pulse_results = current_patient_data.calculate_pulse_results()
       
            results[patient_id] = {
                'unmedicated_avg': pulse_results['unmedicated_avg'],
                'medicated_avg': pulse_results['medicated_avg'],
                'difference': pulse_results['difference'],
                'change' : pulse_results['change'],
                'dates': current_patient_data.dates,
                'pulse': current_patient_data.pulse,
                'medication_start': current_patient_data.medication_start
            }

    return results