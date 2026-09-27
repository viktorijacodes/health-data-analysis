class Patient:
    def __init__(self, patient_id):
        self.patient_id = patient_id
        self.dates = []
        self.glucose = []
        self.pulse = []
        self.medication_start = None
        self.unmedicated_glucose = []
        self.medicated_glucose = []

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
         



def analyze_glucose(data):
    # organizing data by patient with dict
    patients = {}

#for loop konverterar data till dict
    for row in data: 
        patient_id = row['patient_id'] # patient id changes depending on row in the loop


        if patient_id not in patients:# using not in because several rows/datapoints for the same patient
            patient = Patient(patient_id)
            patients[patient_id] = patient


        if row['medication'] == 'none': # if the row containts 'none' in medication, adds glucose levels from that row to unmedicated glucose in the particular patients ''box''
            patient.unmedicated_glucose.append(float(row['glucose']))
        else:
            patient.medicated_glucose.append(float(row['glucose']))
        # lägger till i loopet för att använda för graph
        patient.dates.append(row['date'])
        patient.glucose.append(float(row['glucose']))

        if row['medication'] != 'none' and patient.medication_start is None:
            patient.medication_start = row['date']

    #sparar all resultat i en dict som jag fått från loopet
    results = {}

    for patient_id in patients:
        current_patient_data = patients[patient_id]

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
    patients = {}
    for row in data: 
        patient_id = row['patient_id'] # patient id changes depending on row in the loop

        if patient_id not in patients: # using not in because several rows/datapoints for the same patient
                    unmedicated_pulse = []
                    medicated_pulse = []
                    dates = []
                    pulse = []
                    medication_start = None
        
                    patients[patient_id] = {
                        'unmedicated' : unmedicated_pulse,
                        'medicated' : medicated_pulse,
                        'dates' : dates,
                        'pulse' : pulse,
                        'medication_start' : medication_start
                    }

        if row['medication'] == 'none':
            patients[patient_id]['unmedicated'].append(float(row['heart_rate']))
        else:
            patients[patient_id]['medicated'].append(float(row['heart_rate']))

        patients[patient_id]['dates'].append(row['date'])
        patients[patient_id]['pulse'].append(float(row['heart_rate']))

        if row['medication'] != 'none' and patients[patient_id]['medication_start'] is None:
                    patients[patient_id]['medication_start'] = row['date']

    results = {}
    
    for patient_id in patients:
        current_patient_data = patients[patient_id]
        unmedicated_pulse = current_patient_data['unmedicated']
        medicated_pulse = current_patient_data['medicated']
    
    
        unmedicated_pulse_avg = sum(unmedicated_pulse) / len(unmedicated_pulse)
        medicated_pulse_avg = sum(medicated_pulse) / len(medicated_pulse)
        diff_pulse = unmedicated_pulse_avg - medicated_pulse_avg
    
    
        if diff_pulse > 0:
            change = "decreased"
        elif diff_pulse < 0:
            change = "increased"
        else:
            change = "no change"
    
        results[patient_id] = {
            'unmedicated_avg': unmedicated_pulse_avg,
            'medicated_avg': medicated_pulse_avg,
            'difference': diff_pulse,
            'change' : change,
            'dates': current_patient_data['dates'],
            'pulse': current_patient_data['pulse'],
            'medication_start': current_patient_data['medication_start']
        }

    return results

