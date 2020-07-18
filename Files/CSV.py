import csv

class CSV:
    csvList = []

    def __init__(self, filepath):
        with open(filepath)as files:
            csvReader = csv.reader(files, delimiter = ',')
            for x in csvReader:
                self.csvList.append(x)
        pass

