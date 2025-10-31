import sys
import csv

csv_file=open('/<Enter path to the .csv file here>')

csv_reader=csv.reader(csv_file)
csv_data=list(csv_reader)
print(csv_data)
 
csv_file.close()
