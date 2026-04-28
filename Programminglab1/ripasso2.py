
class ExamException(Exception):
    pass


class solita():
    def __init__(self,name):
        self.name=name
        try:
           with open(self.name, 'r') as file:
             x=file.read()
             if x==(''):
              raise ExamException('seh proprio vuoto')
        except:
           raise ExamException('non è pox aprire il file')
        
    
    
    def get_data(self,country):
        listoflist=[]
        file=open(self.name,'r')
        for line in file:
            var=line.strip().split(',')
            data=var[0]
            try:
                temp=float(var[1])
            except:
             continue
            paese=var[2]
            if country==paese:
                listoflist.append([data,temp])
        file.close()
        if listoflist==[]:
         raise ExamException('paese non presente nel file')
        return listoflist

#def mediatemp()

def funzionemedia(time_series, first_year,last_year):
   years={}
   for element in time_series:
      date=element[0].split('-')
      year=int(date[0])
      month=date[1]
      temp=element[1]
      if first_year<=year<=last_year:
         if year not in years:
            years[year]=[]
         years[year].append(temp)
   media={}
   for element in years:
      medi=sum(years[element])/len(years[element])
      media[element]=medi
   return media

   


def compute_variations(time_series_1, time_series_2, first_year, last_year):
   if isinstance(first_year,(int))==False:
      raise ExamException
   if isinstance(last_year,(int))==False:
      raise ExamException
   time1=funzionemedia(time_series_1,first_year, last_year)
   time2=funzionemedia(time_series_2,first_year,last_year)
   var={}
   for element in time1:
      if element in time2:
         x=float(time2[element]-time1[element])
      var[element]=[]
      var[element]=x
   return var
         

def verifica():
    # due serie temporali con valori noti
    time_series_1 = [
        ["1900-01-01", 10.0],
        ["1900-02-01", 20.0],
        ["1901-01-01", 30.0],
        ["1901-02-01", 50.0]
    ]

    time_series_2 = [
        ["1900-01-01", 15.0],
        ["1900-02-01", 25.0],
        ["1901-01-01", 40.0],
        ["1901-02-01", 60.0]
    ]

    # medie attese:
    # 1900 -> ts1 = 15.0 ; ts2 = 20.0 ; differenza = 5.0
    # 1901 -> ts1 = 40.0 ; ts2 = 50.0 ; differenza = 10.0
    expected = {
        "1900": 5.0,
        "1901": 10.0
    }

    result = compute_variations(time_series_1, time_series_2, 1900, 1901)

    if result == expected:
        print("Test superato")
    else:
        print("Errore nel test")
        print("Atteso:", expected)
        print("Ottenuto:", result)



