from data_loader import load_data
from analyzer import analyze_glucose

loaded_patient_data = load_data("data/patient_data.csv")
results = analyze_glucose(loaded_patient_data)

for patient_id in results:
    patient = results[patient_id]

    print(f'Patient: {patient_id}')
    print(f'Average before medication: {round(patient["unmedicated_avg"], 2)} mmol/L')
    print(f'Average after medication: {round(patient["medicated_avg"], 2)} mmol/L')
    print(f'Difference in glucose levels: {round(patient["difference"], 2)} mmol/L')
