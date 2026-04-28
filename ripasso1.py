class ExamException(Exception):
    pass
class CSVTimeSeriesFile():
    def __init__(self,name):
        self.name=name
        try:
           with open(self.name,'r') as file:
              x= file.read()
        except:
           raise ExamException('impox aprire il file')

    def get_data(self):
        listoflist=[]
        file=open(self.name,'r')
        for line in file:
         var=line.strip().split(',')
         date=var[0]
         try:
            temp=float(var[1])
            if temp<0:
               continue
         except:
            continue
         if date=='dt':
            continue
         listoflist.append([date,temp])
        file.close()
        return listoflist

def compute_variations(time_series, first_year, last_year, N):
   if N >= (last_year - first_year + 1):
    raise ExamException("Errore: N non valido")
   years={}
   for element in time_series:
      date=element[0].split('-')
      year=int(date[0])
      month=int(date[1])
      temp=float(element[1])
      if first_year<=year<=last_year:
        if year not in years:
            years[year]=[]
        
        years[year].append(temp)
   media={}
   for element in years:
      media[element]=[]
      var=(years[element])
      med=float(sum(var))/len(var)
      media[element]=med
   risultato={}
   for year in range(first_year, last_year + 1):
    if year in media:
        anni_precedenti = []

        for previous_year in range(year - N, year):
            if previous_year in media:
                anni_precedenti.append(media[previous_year])

        if len(anni_precedenti) == N:
            media_mobile = sum(anni_precedenti) / N
            risultato[str(year)] = media[year] - media_mobile
   return risultato
   
   
def verify_temperature(time_series,tempmin,tempmax):
   if tempmax<tempmin:
      raise ExamException('Errore: temperatura massima superiore a temperatura minima')
   out=[]
   for element in time_series:
      date=element[0].split('-')
      year=int(date[0])
      month=int(date[1])
      temp=element[1]
      if temp<tempmin or tempmax<temp:
        if year not in out:
           out.append(year)
   return out
      




time_series_file = CSVTimeSeriesFile(name="GlobalTemperatures_mock.csv")
time_series = time_series_file.get_data()
print(time_series)
n=(compute_variations(time_series, 1900, 1904, 3))
print(n)
class ExamException(Exception):
    pass
class CSVTimeSeriesFile():
    def __init__(self,name):
        self.name=name
        try:
           with open(self.name,'r') as file:
              x= file.read()
        except:
           raise ExamException('impox aprire il file')

    def get_data(self):
        listoflist=[]
        file=open(self.name,'r')
        for line in file:
         var=line.strip().split(',')
         date=var[0]
         try:
            temp=float(var[1])
            if temp<0:
               continue
         except:
            continue
         if date=='dt':
            continue
         listoflist.append([date,temp])
        file.close()
        return listoflist

def compute_variations(time_series, first_year, last_year, N):
   if N >= (last_year - first_year + 1):
    raise ExamException("Errore: N non valido")
   years={}
   for element in time_series:
      date=element[0].split('-')
      year=int(date[0])
      month=int(date[1])
      temp=float(element[1])
      if first_year<=year<=last_year:
        if year not in years:
            years[year]=[]
        
        years[year].append(temp)
   media={}
   for element in years:
      media[element]=[]
      var=(years[element])
      med=float(sum(var))/len(var)
      media[element]=med
   risultato={}
   for year in range(first_year, last_year + 1):
    if year in media:
        anni_precedenti = []

        for previous_year in range(year - N, year):
            if previous_year in media:
                anni_precedenti.append(media[previous_year])

        if len(anni_precedenti) == N:
            media_mobile = sum(anni_precedenti) / N
            risultato[str(year)] = media[year] - media_mobile
    return risultato
   
   
def verify_temperature(time_series,tempmin,tempmax):
   if tempmax<tempmin:
      raise ExamException('Errore: temperatura massima superiore a temperatura minima')
   out=[]
   for element in time_series:
      date=element[0].split('-')
      year=int(date[0])
      month=int(date[1])
      temp=element[1]
      if temp<tempmin or tempmax<temp:
        if year not in out:
           out.append(year)
   return out
      




time_series_file = CSVTimeSeriesFile(name="GlobalTemperatures_mock.csv")
time_series = time_series_file.get_data()
print(time_series)
n=(compute_variations(time_series, 1900, 1904, 3))
print(n)

print(verify_temperature(time_series,9.0,21.5))

   



         


   



         