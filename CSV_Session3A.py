import sys
import csv

def csv_reader(filename):
  """Read and output the details of CSV file."""
  try:
    print("Opening the file")
    with open(filename) as csv_file:
      print("Reading file contents as .csv")
      csv_data=csv.reader(csv_file)
      print("Attempting to extract header row")
      print("Before the for loop")
      header_row=[]
      for row in csv_data:
        print("Initializing header row")
        header_row=row
        #print(header_row)
        break
        return [header_row]
      for column in header_row:
        #print("hi")
        print(column)
        #options = list(column)
    print("Please select your header category")
    print('\n')
    print(header_row)
    print('\n')
    print("Please use the options above:")
    var1=input()
    print("The option you choose was" + var1)
    #print(header_row)  
    
    csv_file.close()
  except:
    print ("Unable to find variable file named" , filename)

try:
  print('Processing CSV file')
  csv.reader('/<Enter path to the .csv file here>')
except:
  print ("Unable to find file")
#input ('Please press ENTER to exit')
