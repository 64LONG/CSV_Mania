import sys
import csv

def csv_reader(filename):
  """Read and output the details of CSV file."""
  try:
    print("1")
    with open(filename) as csv_file:
      print("2")
      csv_data=csv.reader<csv_file)
      print("3")
      for csv_record in csv_data:
        print(csv_record)
      csv_file.close()
  except:
    print ("Unable to find file named" , filename)

try:
  print('Processing CSV file')
  csv.reader('/<Enter path to the .csv file here>')
except:
  print ("Unable to find file")

#input ('Please press ENTER to exit')
