import sys
import csv

csv_file=open('/<Enter path to the .csv file here>')
csv_data=csv.reader(csv_file)

for csv_record in csv_data:
  print(csv_record)
 
csv_file.close()
