import sys
import pandas as pd

def csv_reader(filename):
  """Read and output the details of CSV file."""
  try:
    print("Opening the file")
    print("Reading file contents as .csv")
    df=pd.read_csv(filename)
    data=pd.DataFrame(df)
    print("Attempting to extract header row")
    print("Initializing header row")
    print('\n')
    print(df.columns.tolist())
    print('\n')
    print("Please select your header category")
    print('\n')
    print("Please use the options above:")
    var1=input()
    print("The option you choose was" + var1)
    #Find the ID and return the records
    if var1 == "Id":
      id_column=df.set_index('Id')
      id_number=df.get('Id').tolist()
      print("Please select the identification number of your choosing:")
      print(id_number)
      id_select=input()
      print("Selecting the identification record -> "+ str(id_select))
      clean_num = int(id_select)
      print(id_column.loc[clean num])
    #Find the student and return the records
      if var1 == "student":
        student_name=df.get('student').tolist()
        print(student_name)
        print("Please select the student of your choosing: ")
        student_select=input()
        print("Selecting record for" + str(student_select))
        print(df[df["student"] == student_select])
    #Find the avilable language and return the records
      if var1 == "language":
        student_name=df.get('student').tolist()
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
        
        #Counting for number of beginner proficiencies for the selected language
        beginner_count = len(df.loc[(df["proficency"] == 'beginner') & (df['language'] == language_var)])
        print("Number of beginner proficency levels for" + str(language_var) + " :" + str(beginner_count))
        
        #Counting for number of intermediate proficiencies for the selected language      
        intermediate_count = len(df.loc[(df["proficency"] == 'intermediate') & (df['language'] == language_var)])
        print("Number of intermediate proficency levels for" + str(language_var) + " :" + str(intermediate_count))
        
        #Counting for number of advanced proficiencies for the selected language      
        advanced_count = len(df.loc[(df["proficency"] == 'advanced') & (df['language'] == language_var)])
        print("Number of advanced proficency levels for" + str(language_var) + " :" + str(advanced_count))
        
        #Counting for number of expert proficiencies for the selected language      
        expert_count = len(df.loc[(df["proficency"] == 'expert') & (df['language'] == language_var)])
        print("Number of expert proficency levels for" + str(language_var) + " :" + str(expert_count))
   
    #Find the proficiency and return the records
    if var1 == "proficiency":
      program_proficiency=df.get('proficency').tolist()
      print(set(program_proficiency))
      print("Please select the proficiency level of your choosing: ")
      proficiency_select=input()
      print("Selecting proficiency level" + str(proficiency_select))

      #Counting for number of selected proficiency for Python
      Python_count = len(df.loc[(df["proficiency"] == 'proficiency_select') & (df['language'] == 'Python')])
      Print("Number of " + str(proficency_select) + "proficency levels for Python :" + str(Python_count))

      #Counting for number of selected proficiency for C#
      C_count = len(df.loc[(df["proficiency"] == 'proficiency_select') & (df['language'] == 'C#')])
      Print("Number of " + str(proficency_select) + "proficency levels for C# :" + str(C_count))
      
      #Counting for number of selected proficiency for Java
      Java_count = len(df.loc[(df["proficiency"] == 'proficiency_select') & (df['language'] == 'Java')])
      Print("Number of " + str(proficency_select) + "proficency levels for Java :" + str(Java_count))
      
      #Counting for number of selected proficiency for HTML
      HTML_count = len(df.loc[(df["proficiency"] == 'proficiency_select') & (df['language'] == 'HTML')])
      Print("Number of " + str(proficency_select) + "proficency levels for HTML :" + str(HTML_count))
      
      #Counting for number of selected proficiency for Rust
      Rust_count = len(df.loc[(df["proficiency"] == 'proficiency_select') & (df['language'] == 'Rust')])
      Print("Number of " + str(proficency_select) + "proficency levels for Rust :" + str(Rust_count))
      
      #Counting for number of selected proficiency for Terraform
      Terraform_count = len(df.loc[(df["proficiency"] == 'proficiency_select') & (df['language'] == 'Terraform')])
      Print("Number of " + str(proficency_select) + "proficency levels for Terraform :" + str(Terraform_count))
      
    csv_file.close()
    
  except Exception as e:
    print ("Unable to find variable file named" , e)

try:
  print('Processing CSV file')
  csv.reader('/<Enter path to the .csv file here>')
  print(pd.__version__)
except:
  print ("Unable to find file")
#input ('Please press ENTER to exit')
