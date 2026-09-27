import matplotlib.pyplot as plt
from matplotlib.ticker import FormatStrFormatter

def glucose_visualizer(results):
    for patient_id in results:
        patient = results[patient_id] #ger mig tillgång till datasettet för unika patient
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

        plt.plot(dates, glucose, color='#E91E63',  marker='o') #skapar xy axis för varje patient i rosa :)
        plt.axvline(
            medication_start,
            color='#E91E63',                #lägger till en vertikal indikatorn för medicinstart
            linestyle='--',
            label='Medication started'
        )
        plt.legend()
        plt.grid(alpha=0.3) #lägger till gridd för lättare avläsning och gör den litte mindre synlig
        plt.xticks(rotation=45) # roterar datum för att det ska bli lättare att avläsa
        plt.tight_layout() # formatterar graph så allt får plats

    plt.show() #visar graph




def pulse_visualizer(results):
    for patient_id in results:
        patient = results[patient_id] #ger mig tillgång till datasettet för unika patient
        dates = patient['dates']
        pulse = patient['pulse']
        medication_start = patient['medication_start']

        # varje patient får sin egen graph i ROSA :)
        plt.figure(facecolor = '#FCE4EC')
        plt.gca().set_facecolor('#FFF5F8')


        plt.title(f'Pulse levels - {patient_id}', fontweight='bold', color='#E91E63')
        plt.xlabel('Date', fontweight='bold', color='#E91E63')
        plt.ylabel('Pulse (bpm)', fontweight='bold', color='#E91E63')

        # avrundar och formaterar glukos värde till 1 decimaltecken i graph
        plt.gca().yaxis.set_major_formatter(FormatStrFormatter('%.0f'))

        plt.plot(dates, pulse, color='#E91E63',  marker='o') #skapar xy axis för varje patient i rosa :)
        plt.axvline(
            medication_start,
            color='#E91E63',                #lägger till en vertikal indikatorn för medicinstart
            linestyle='--',
            label='Medication started'
        )
        plt.legend()
        plt.grid(alpha=0.3) #lägger till gridd för lättare avläsning och gör den litte mindre synlig
        plt.xticks(rotation=45) # roterar datum för att det ska bli lättare att avläsa
        plt.tight_layout() # formatterar graph så allt får plats

    plt.show() #visar graph