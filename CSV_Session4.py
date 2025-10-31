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
    var1=input()
    print("The option you choose was" + var1)
    id_number=[]
    student_name=[]
    avaliable_languages=[]
    program_proficiency=[]
    for data in records:
      id_number.append(data[0])
      student_name.append(data[1])
      avaliable_languages.append(data[2])
      program_proficiency.append(data[3])
    #Find the ID and return the records
    if var1 == "Id":
      print(id_number)
      print("Please select the identification number if your choosing: ")
      id_select=input()
      print("Selecting the identification record -> "+ str(id_select))
      filtered_id_number=[]
      for scan in records:
        if scan[0] == id_select:
          filtered_id_number.append(scan)
          print(filtered_id_number)
    #Find the student and return the records
      if var1 == "student":
      print(student_name)
      print("Please select the student of your choosing: ")
      student_select=input()
      print("Selecting record for "+ str(student_select))
      filtered_student_name=[]
      for scan in records:
        if scan[1] == student_select:
          filtered_student_name.append(scan)
          print(filtered_student_name)
    #Find the avilable language and return the records
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
      print("Here is the proficiency levels for " + str(language_var))
      filtered_lang_proficency = []
      for scan in records:
        if scan[2] == language_var:
          filtered_lang_proficency.append(scan[3])
      beginner_count = filtered_lang_proficency.count("beginner")
      print("Number of beginner proficency levels for" + str(language_var) + " :" + str(beginner_count))
      intermediate_count = filtered_lang_proficency.count("intermediate")
      print("Number of intermediate proficency levels for" + str(language_var) + " :" + str(intermediate_count))
      advanced_count = filtered_lang_proficency.count("advanced")
      print("Number of advanced proficency levels for" + str(language_var) + " :" + str(advanced_count))
      expert_count = filtered_lang_proficency.count("expert")
      print("Number of expert proficency levels for" + str(language_var) + " :" + str(expert_count))
    #Find the proficiency and return the records
    if var1 == "proficency":
      print(set(program_proficency))
      print("Please select the proficency level of your choosing: ")
      proficency_select=input()
      filtered_proficency_program = []
      for scan in records:
        if scan[3] == proficency_select:
          filtered_proficency_program.append(scan[2])
          Python_count = filtered_proficency_program.count("Python")
          Print("Number of " + str(proficency_select) + "proficency levels for Python :" + str(Python_count))
          C_count = filtered_proficency_program.count("C#")
          Print("Number of " + str(proficency_select) + "proficency levels for C# :" + str(C_count))
          Java_count = filtered_proficency_program.count("Java")
          Print("Number of " + str(proficency_select) + "proficency levels for Java :" + str(Java_count))
          HTML_count = filtered_proficency_program.count("HTML")
          Print("Number of " + str(proficency_select) + "proficency levels for HTML :" + str(HTML_count))
          Rust_count = filtered_proficency_program.count("Rust")
          Print("Number of " + str(proficency_select) + "proficency levels for Rust :" + str(Rust_count))
          Terraform_count = filtered_proficency_program.count("Terraform")
          Print("Number of " + str(proficency_select) + "proficency levels for Terraform :" + str(Terraform_count))
    csv_file.close()
    
  except Exception as e:
    print ("Unable to find variable file named" , e)

try:
  print('Processing CSV file')
  csv.reader('/<Enter path to the .csv file here>')
except:
  print ("Unable to find file")
#input ('Please press ENTER to exit')
