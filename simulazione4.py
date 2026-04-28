class ExamException(Exception):
    pass


class CSVTimeSeriesFile():
    def __init__(self, name):
        self.name = name
        try:
            file = open(self.name)
            file.close()
        except:
            raise ExamException("Errore: impossibile aprire il file")

    def get_data(self):
        lista = []
        file = open(self.name, 'r')
        for line in file:
            line = line.strip().split(',')
            if len(line) < 3:
                continue
            if line[0] == "dt":
                continue
            data = line[0]
            try:
                temperatura = float(line[1])
                uncertainty = float(line[2])
            except:
                continue
            if uncertainty >= 5:
                print("Data saltata perché valore troppo incerto")
                continue
            lista.append([data, temperatura])
        file.close()
        return lista



def compute_month_variation(time_series, first_year, second_year):

    # Controllo che i due anni siano interi
    if not isinstance(first_year, int) or not isinstance(second_year, int):
        raise ExamException("Errore: gli anni inseriti devono essere di tipo intero.")

    # Controllo che il secondo anno sia maggiore del primo
    if second_year <= first_year:
        raise ExamException("Errore: il secondo anno deve essere maggiore del primo.")

    # Dizionari che conterranno:
    # mese -> temperatura
    first_year_data = {}
    second_year_data = {}

    # Scorro tutta la time series
    for element in time_series:
        date = element[0]
        temperature = element[1]

        # La data è nel formato DD/MM/YYYY
        parts = date.split('/')

        # Se la data non è fatta bene, salto
        if len(parts) != 3:
            continue

        day = parts[0]
        month = parts[1]
        year = parts[2]

        # Provo a trasformare mese e anno in interi
        try:
            month = int(month)
            year = int(year)
        except:
            continue

        # Se la riga appartiene al primo anno, salvo la temperatura di quel mese
        if year == first_year:
            first_year_data[month] = temperature

        # Se la riga appartiene al secondo anno, salvo la temperatura di quel mese
        if year == second_year:
            second_year_data[month] = temperature

    # Dizionario finale:
    # chiave = mese
    # valore = temperatura(second_year) - temperatura(first_year)
    result = {}

    # Controllo tutti i mesi da 1 a 12
    for month in range(1, 13):

        # Il mese deve essere presente in entrambi gli anni
        if month in first_year_data and month in second_year_data:
            result[month] = second_year_data[month] - first_year_data[month]
        else:
            print("La variazione per il mese " + str(month) + " non può essere calcolata")

    # Se non è stato possibile calcolare nessun mese
    if len(result) == 0:
        raise ExamException("Gli anni considerati non hanno mesi validi")

    return result

 

   



        