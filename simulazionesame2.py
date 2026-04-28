class errore(Exception):
    pass


class CSVTimeSeriesFile():
    def __init__(self, name):
        self.name=name

    def get_data():
     listoflist=[]
     try:
      file=open('self.name','r')
     except: 
        raise errore('errore lista valori vuota')
     for line in file:
        element=line.strip().split(',')
        if element[0]=='date':
         continue
        if len(element)< 2:
           continue
        date=element[0]
        passenger=element[1]
        try:
                passengers = int(passengers)
        except:
         print("Valore passeggeri non valido")
         continue
        listoflist.append([date,passenger])
     file.close()
     return listoflist


     
    def compute_variations(time_series, first_year, last_year):

     years = {}

     for element in time_series:

        date = element[0]
        passengers = element[1]

        year = date.split("-")[0]

        if year < first_year or year > last_year:
            continue

        if year not in years:
            years[year] = []

        years[year].append(passengers)


     averages = {}

     for year in years:

        values = years[year]

        avg = sum(values) / len(values)

        averages[year] = avg


     result = {}

     sorted_years = sorted(averages.keys())

     for i in range(len(sorted_years)-1):

        year1 = sorted_years[i]
        year2 = sorted_years[i+1]

        diff = averages[year2] - averages[year1]

        key = year1 + "-" + year2

        result[key] = diff

     return result
