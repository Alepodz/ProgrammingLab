class ExamException(Exception):
 pass

class CSVTimeSeriesFile():
    def __init__(self,name):
        try:
          file=open(self.name,'r')
        except:
           raise ExamException('impossibile aprire il file')
        self.name=name



    def get_data(self):
        liste=[]
        file=open(self.name,'r')
        for line in file:
           element=line.strip().split(',')
           # se la riga ha meno di 2 campi, la ignoro
           if len(element) < 2:
                continue
            # salto l'intestazione
           if element[0] == "dt":
                continue
           data=element[0]
           temperatura=element[1]
           try:
             temperatura=float(temperatura)
             temperatura>0
           except:
            continue
           if temperatura < 0:
                continue
           liste.append([data,temperatura])
        file.close()
        return liste
 

 
def compute_variations(time_series, first_year, last_year, N):
   intervallo=int(last_year)-int(first_year)+1
   if N>= intervallo:
      raise ExamException('finestra troppo lunga')
   years={}
   for element in time_series:
      date=element[0]
      temperature=element[1]
      year=date.strip('-')
      if year >= first_year and year <= last_year:
         if year not in years:
           years[year]=[]
         intervallo=int(last_year)-int(first_year)

   if len(years) == 0:
        raise ExamException("Nessun dato nell'intervallo selezionato.")

    # calcolo media annuale per ogni anno disponibile
   annual_averages = {}
   for year in years:
        values = years[year]
        annual_averages[year] = sum(values) / len(values)
   # ordino gli anni disponibili
   ordered_years = sorted(annual_averages.keys())
   result = {}
    # parto dall'indice N, perché servono N anni precedenti
   for i in range(N, len(ordered_years)):
        current_year = ordered_years[i]
        # prendo i N anni precedenti
        previous_years = ordered_years[i - N:i]
        # calcolo la media delle medie annuali precedenti
        previous_sum = 0
        for year in previous_years:
            previous_sum += annual_averages[year]
        mobile_average = previous_sum / N
        # differenza tra media annuale corrente e media dei N anni precedenti
        variation = annual_averages[current_year] - mobile_average
        result[current_year] = variation

      
    



   

   
