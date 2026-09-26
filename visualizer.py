import matplotlib.pyplot as plt
from matplotlib.ticker import FormatStrFormatter

def glucose_visualizer(results):
    for patient_id in results:
        patient = results[patient_id] #ger mig tillgång till datasettet för unika patient
        dates = patient['dates']
        glucose = patient['glucose']

        # varje patient får sin egen graph
        plt.figure()
        plt.title(f'Glucose levels - {patient_id}')
        plt.xlabel('Date')
        plt.ylabel('Glucose (mmol/L)')

        # avrundar och formaterar glukos värde till 1 decimaltecken i graph
        plt.gca().yaxis.set_major_formatter(FormatStrFormatter('%.1f'))

        plt.plot(dates, glucose) #skapar xy axis för varje patient
        plt.grid() #lägger till gridd för lättare avläsning
        plt.xticks(rotation=45) # roterar datum för att det ska bli lättare att avläsa
        plt.tight_layout() # formatterar graph så allt får plats

    plt.show() #visar graph