def analyze_glucose(data):
    # organizing data by patient with dict
    patients = {}

#for loop konverterar data till dict
    for row in data: 
        patient_id = row['patient_id'] # patient id changes depending on row in the loop


        if patient_id not in patients: # using not in because several rows/datapoints for the same patient
            unmedicated_glucose = []
            medicated_glucose = []

            patients[patient_id] = {
                'unmedicated' : unmedicated_glucose,
                'medicated' : medicated_glucose
            }


        if row['medication'] == 'none': # if the row containts 'none' in medication, adds glucose levels from that row to unmedicated glucose in the particular patients ''box''
            patients[patient_id]['unmedicated'].append(float(row['glucose']))
        else:
            patients[patient_id]['medicated'].append(float(row['glucose']))

    results = {}

    for patient_id in patients:
        current_patient_data = patients[patient_id]
        unmedicated_glucose = current_patient_data['unmedicated']
        medicated_glucose = current_patient_data['medicated']


        unmedicated_glucose_avg = sum(unmedicated_glucose) / len(unmedicated_glucose)
        medicated_glucose_avg = sum(medicated_glucose) / len(medicated_glucose)
        diff_glucose = unmedicated_glucose_avg - medicated_glucose_avg

        results[patient_id] = {
            'unmedicated_avg': unmedicated_glucose_avg,
            'medicated_avg': medicated_glucose_avg,
            'difference': diff_glucose
        }

    return results
    




    


    

'''
def analyze_blood_pressure(data):
    unmedicated_systolic = []
    unmedicated_diastolic = []
    medicated_systolic = []
    medicated_diastolic = []

    for row in data:
        if row in data:
'''


