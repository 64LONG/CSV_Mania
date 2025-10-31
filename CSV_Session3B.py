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
      print("Initializing header row")
      header_row = next(csv_data)
      records =list(csv_data)
    print("Please select your header category")
    print('\n')
    print(header_row)
    print('\n')
    print("Please use the options above:")
    zip(header_row, records[0])
    #print(header_row)  
    #Single_list=list(zip(header_row,records[0]))
    #print(Single_list)
    #Full_list=list(zip(header_row,records))
    #print(Full_list)
    #print(records)
    var1=input()
    print("The option you choose was" + var1)
    #print(header_row)
    #print(records)
    avaliable_languages=[]
    for data in records:
      avaliable_languages.append(data[2])
    if var1 == "language":
      print(set(avaliable_languages))
      print("Please select your language you want to count")
      print('\n')
      print('\n')
      language_var=input()
      cleaned_language_var=str(language_var)
      print("The option you choose was" + language_var)
      print('\n')
      language_count = avaliable_language.count(language_var)
      print("There is currently " + str(language_var) + " programmers using " + str(language_var))
    
    csv_file.close()
  except:
    print ("Unable to find variable file named" , filename)

try:
  print('Processing CSV file')
  csv.reader('/<Enter path to the .csv file here>')
except:
  print ("Unable to find file")
#input ('Please press ENTER to exit')
