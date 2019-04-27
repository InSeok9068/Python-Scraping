from urllib.request import urlopen
from io import StringIO
import csv

data = urlopen(
    "http://pythonscraping.com/files/MontyPythonAlbums.csv"
).read().decode('ascii','ignore')
dataFile = StringIO(data)
dicReader = csv.DictReader(dataFile)

print(dicReader.fieldnames)

for row in dicReader:
    print(row)