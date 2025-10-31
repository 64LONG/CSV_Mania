import ipydeps
ipydeps.pip('pandas')

import sys
import csv
import pandas as pd

csv_file=open('/<Enter path to the .csv file here>')

data_frame=pd.read(csv_file)
print(data_frame)
 
csv_file.close()
