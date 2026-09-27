from data_loader import load_data
from analyzer import analyze_glucose, analyze_pulse
from visualizer import glucose_visualizer, pulse_visualizer

loaded_patient_data = load_data("data/patient_data.csv")
results = analyze_glucose(loaded_patient_data)
pulse_results = analyze_pulse(loaded_patient_data)

selected_patient_id = input('Which patient do you want to see?(P001-P006): ')

if selected_patient_id in results:
    selected_patient = results[selected_patient_id]
    selected_measurement = "glucose"

elif selected_patient_id in pulse_results:
    selected_patient = pulse_results[selected_patient_id]
    selected_measurement = "pulse"


for current_patient_id in results:
    patient = results[current_patient_id]

    print(f'Glukos - Patient: {current_patient_id}')
    print(f'Average before medication: {round(patient["unmedicated_avg"], 2)} mmol/L')
    print(f'Average after medication: {round(patient["medicated_avg"], 2)} mmol/L')
    print(f'Difference in glucose levels: {round(patient["difference"], 2)} mmol/L')
    print(f'Glucose change: {patient["change"]}')

for patient_id in pulse_results:
    patient = pulse_results[patient_id]

    print(f'Pulse - Patient: {patient_id}')
    print(f'Average before medication: {round(patient["unmedicated_avg"], 0):.0f} bpm')
    print(f'Average after medication: {round(patient["medicated_avg"], 0):.0f} bpm')
    print(f'Difference in pulse: {round(patient["difference"], 0):.0f} bpm')
    print(f'Pulse change: {patient["change"]}')


if selected_measurement == "glucose":
    glucose_visualizer({selected_patient_id: selected_patient})

elif selected_measurement == "pulse":
    pulse_visualizer({selected_patient_id: selected_patient})