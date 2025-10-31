import sys
import pandas as pd

def csv_reader(filename):
  """Read and output the details of CSV file."""
  try:
    print("Opening the file")
    iris_dataframe=pd.csvReader(filename)
    #print(iris_dataframe)
    #Print the first top 5 rows of the file
    print(iris_dataframe.head())
    #Print a specific number of rows starting from the frist row of the data frame
    print(iris_dataframe.head(8))
    print("---")

    print("---")
    #Print the last bottom 5 rows of the file
    print(iris_dataframe.tail())
    print("---")
    #Print a specific number of rows starting from the last row of the data frame
    print(iris_dataframe.tail(2))
    print("---")
    print(iris_dataframe.shape[0])
    #Print a shape of frame using an intermediate proificency
    print(iris_dataframe[iris_dataframe["proificency"] == 'intermediate'].shape[0])
    print("---")
    #print specfic columns of the data frame
    students= iris_dataframe["student"])
    print(students)
    print("---")
    student_program= iris_dataframe[["student" , "language"]])
    print(student_program)
    #print a row using an intermediate proificency
    print(iris_dataframe[iris_dataframe["proificency"] == 'intermediate'])
    print("---")
    #Print a column using an intermediate proificency as a condition
    print(iris_dataframe.loc[iris_dataframe["proificency"] == 'intermediate', "student"])
    
  except Exception as e:
    print ("Unable to find variable file named" , e)

try:
  print('Processing CSV file')
  csv.reader('/<Enter path to the .csv file here>')
  print(pd.__version__)
except:
  print ("Unable to find file")
#input ('Please press ENTER to exit')
