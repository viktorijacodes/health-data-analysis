from data_loader import load_data
from analyzer import analyze_glucose, analyze_pulse
from visualizer import glucose_visualizer, pulse_visualizer

loaded_patient_data = load_data('data/patient_data.csv')
results = analyze_glucose(loaded_patient_data)
pulse_results = analyze_pulse(loaded_patient_data)

valid_patient = False

while not valid_patient:
    try:
        selected_patient_id = input('Which patient do you want to see?(P001-P006): ')

        if selected_patient_id in results:
            selected_patient = results[selected_patient_id]
            selected_measurement = 'glucose'
            valid_patient = True

        elif selected_patient_id in pulse_results:
            selected_patient = pulse_results[selected_patient_id]
            selected_measurement = 'pulse'
            valid_patient = True
        else:
            raise ValueError()
    
    except ValueError:
        print('Invalid Patient ID, try again.')








if selected_measurement == 'glucose':
    print(
        f'Patient: {selected_patient_id}'
        f'\nBefore medication: {selected_patient["unmedicated_avg"]:.1f} mmol/L'
        f'\nAfter medication: {selected_patient["medicated_avg"]:.1f} mmol/L'
        f'\nDifference in glucose: {selected_patient["difference"]:.1f} mmol/L'
        f'\nChange: {selected_patient["change"]}'
    )

    glucose_visualizer({selected_patient_id: selected_patient})
 

elif selected_measurement == 'pulse':
    print(
        f'Patient: {selected_patient_id}'
        f'\nBefore medication: {selected_patient["unmedicated_avg"]:.0f} bpm'
        f'\nAfter medication: {selected_patient["medicated_avg"]:.0f} bpm'
        f'\nDifference in pulse: {selected_patient["difference"]:.0f} bpm'
        f'\nChange: {selected_patient["change"]}'
    )

    pulse_visualizer({selected_patient_id: selected_patient})