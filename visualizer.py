import matplotlib.pyplot as plt
from matplotlib.ticker import FormatStrFormatter


def glucose_visualizer(results):
    for patient_id in results:
        # hämtar data från valda patient
        patient = results[patient_id] 
        dates = patient['dates']
        glucose = patient['glucose']
        medication_start = patient['medication_start']

        # varje patient får sin egen graph i ROSA :)
        plt.figure(facecolor = '#FCE4EC')
        plt.gca().set_facecolor('#FFF5F8')
        plt.title(f'Glucose levels - {patient_id}', fontweight='bold', color='#E91E63')
        plt.xlabel('Date', fontweight='bold', color='#E91E63')
        plt.ylabel('Glucose (mmol/L)', fontweight='bold', color='#E91E63')
        # avrundar och formaterar glukos värde till 1 decimaltecken i graph
        plt.gca().yaxis.set_major_formatter(FormatStrFormatter('%.1f'))
        # skapar xy axis
        plt.plot(dates, glucose, color='#E91E63',  marker='o')
        # lägger till en vertikal indikatorn för medicinstart
        plt.axvline(
            medication_start,
            color='#E91E63',                
            linestyle='--',
            label='Medication started'
        )
        plt.legend()
        # Lägger till ett svagt rutnät för enklare avläsning
        plt.grid(alpha=0.3) 
        # roterar datum för att det ska bli lättare att avläsa
        plt.xticks(rotation=45) 
        # formatterar graph så allt får plats
        plt.tight_layout() 

    plt.show() #visar graph


def pulse_visualizer(results):
    for patient_id in results:
        # hämtar data för varje unik patient
        patient = results[patient_id] 
        dates = patient['dates']
        pulse = patient['pulse']
        medication_start = patient['medication_start']

        # varje patient får sin egen graph i ROSA :)
        plt.figure(facecolor = '#FCE4EC')
        plt.gca().set_facecolor('#FFF5F8')
        plt.title(f'Pulse levels - {patient_id}', fontweight='bold', color='#E91E63')
        plt.xlabel('Date', fontweight='bold', color='#E91E63')
        plt.ylabel('Pulse (bpm)', fontweight='bold', color='#E91E63')
        # avrundar och formaterar pulsvärden till 1 decimaltecken i graph
        plt.gca().yaxis.set_major_formatter(FormatStrFormatter('%.0f'))
        # skapar xy axis
        plt.plot(dates, pulse, color='#E91E63',  marker='o')
        # lägger till en vertikal indikatorn för medicinstart
        plt.axvline(
            medication_start,
            color='#E91E63',                
            linestyle='--',
            label='Medication started'
        )
        plt.legend()
        # lägger till svagt rutnät för lättare avläsning
        plt.grid(alpha=0.3)
        # roterar datum för bättre läsbarhet
        plt.xticks(rotation=45)
        # formatterar graph så allt får plats
        plt.tight_layout()

    plt.show()