class ExamException(Exception):
 pass

class CSVTimeSeriesFile():
 def __init__(self,name):
   self.name=name
   try:
    with open(self.name,'r') as file:
        contenuto=file.read()
   
   except:
    raise ExamException('"Errore: impossibile aprire il file"')
   
   if contenuto=="":
    raise ExamException('"Errore: il file `e vuoto o non contiene dati validi"') 
   #controlla se il file all'interno è vuoto



 def get_data(self,country):
  listoflist=[]
  file=open(self.name,'r')
  for line in file:
        pippo=line.strip().split(',')
        if pippo[0] == "dt":
          continue
        date=pippo[0]
        date=date.split('-')
        try:
            temperature=float(pippo[1])
        except:
            continue
        countries=pippo[2]
        if countries==country:
            listoflist.append([pippo[0],temperature])
  if len(listoflist)==0:
    raise ExamException('Errore: il nome del paese non `e presente nel file')
  file.close()
  return listoflist
  
def mediannuale(timeseries,years):
  dizionario_anno = {}
  media=0
  mesivalidi=0
  for element in timeseries:
    temperatura=element[1]
    date=element[0].split('-')
   
def mediatimeseries(timeseries,first_year,last_year):
  
  years={}
  dizionario_anno = {}
  for element in timeseries:
    date=element[0].split('-')
    #print(element)
    year=date[0]
    month=date[1]

    
    temperature=element[1]
    year =int(year)
    if first_year<=year<=last_year:
        if year not in dizionario_anno:
          dizionario_anno.update({year : [element[1]]})
        else:
          dizionario_anno[year].append(element[1])
   
        if year not in years:
            years[year]=[]
  medie={}
  for element in dizionario_anno:
   media= float(sum(dizionario_anno[element])/len(dizionario_anno[element]))#lista di elemnti nell'anno, calcola media
   medie.update({element:media})
  print(medie)
  return medie


        


def compute_variations(time_series_1, time_series_2, first_year, last_year):
  if not isinstance(first_year, int) or not isinstance(last_year, int):#non usare try con isinstance  usa sempre if
    raise ExamException("Errore: l’anno inserito non `e un intero")
  media1=mediatimeseries(time_series_1,first_year,last_year)
  media2=mediatimeseries(time_series_2,first_year,last_year)
  finale={}
  for element in media1:
    if element in media2:
      sottr= (media2[element])-media1[element]#rappresenta il valore all'interno non la chiave
      finale.update({element:sottr})
  print (finale)
  return finale
    



  
  

  



time_series_file = CSVTimeSeriesFile(name="GlobalLandTemperaturesByCountry_mock.csv")
time_series_italy = time_series_file.get_data(country="Italy")
time_series_germany=time_series_file.get_data(country='Germany')
compute_variations(time_series_italy,time_series_germany,1900,1903)
  

  