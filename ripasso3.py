class ExamException(Exception):
 pass


class CSVTimeSeriesFile():
    def __init__(self,name):
        self.name=name
    def get_data(self):
       listoflist=[]
       file=open(self.name,'r')
       for line in file:
          var=line.sptrip().split(',')
           


def comkp(time_series, first_year, second_year):
   years={}
   for element in time_series:
      date=element[0].split('-')
      year=date[0]
      temp=element[1]
      month=date[1]
      if year==
      if year not in years:
         years[year]=[]
      years[year].append([month,temp])

  
  
  

  