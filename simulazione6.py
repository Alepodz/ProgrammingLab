class ExamException(Exception):
 pass

class CSVTimeSeriesFile():
  def __init__(self,name):
    self.name=name

  def get_data(self,città):
    listcon=[]
    try:
     file=open(self.name)
    except:
      raise ExamException('il file non esiste')
    for line in file:
      var=line.strip().split(',')
      data=var[0]
      temperatura=var[1]
      city=var[2]
      try:
        temperatura=float(var[1])
      except:
        continue
      if city==città:
        listcon.append([data,temperatura])
    if listcon==[]:
      raise ExamException('"Errore: il nome della citt`a non `e presente nel file".')
    return listcon

def compute_slope(time_series, first_year, last_year):
  years={}
  for element in time_series:
    date= element[0]
    temperatura=element[1]
    year=int(date.split('-')[0])
    if first_year<=year<=last_year:
        if year not in years:
          years[year]=[]
        years[year].append(temperatura)
  validyears={}
  for year in years:
    if len(years[year])>=6:
      media = sum(years[year]) / len(years[year])
      validyears[year] = media
  n=len(validyears)

  if n==0:
    raise ExamException('errore nessun anno valido')
  x_bar = sum(validyears.keys()) / n
  y_bar = sum(validyears.values()) / n

  numeratore = 0
  denominatore = 0

  for year in validyears:

        xi = year
        yi = validyears[year]

        numeratore += (xi - x_bar) * (yi - y_bar)
        denominatore += (xi - x_bar) ** 2

  if denominatore == 0:
        raise ExamException("Errore nel calcolo")

  m = numeratore / denominatore

  return m




time_series_file = CSVTimeSeriesFile(name="GlobalLandTemperaturesByMajorCity_mock.csv")
time_series_italy = time_series_file.get_data(città="Rome")
print(time_series_italy)
x=(compute_slope(time_series_italy,1899,1900))
print(x)

