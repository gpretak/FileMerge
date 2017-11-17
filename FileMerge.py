# import libaries
import pandas as pd
import numpy as np
import datetime

# set date and time variables for export file
now = datetime.datetime.now()
day = now.day
month = now.month
year = now.year

# Find all files in a directory 
from os import listdir
from os.path import isfile, join
mypath = r'C:\PLACE FILE DIRECTORY PATH HERE'
onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]

# concat absolute path and file names to create a list of full file names
# Create a dataframe for each file

#initialize variables
paths = []
df_list = []
#counter added to count files
counter = 0

# Create a dataframe for each file and append it to a dataframe list
for i in onlyfiles:
    newpath = mypath + "\\" + i
    paths.append(newpath)
    # Skip Row - If header starts in row 3, skiprows=2
    df = pd.read_excel(newpath,index_col=None, skiprows=2, header=0)
    df_list.append(df)
    counter += 1
print(counter,"files imported")

#create merged dataframe 
df_merge = pd.concat(df_list)

# Remove a row that does not equal a value
#df_merge = df_merge[df_merge["COLUMN_NAME"] != 'Value to exclude']

# Export File to XLSX
# Enter destination path for file
excel = r'C:\PASTE FILE DIRECTORY FOR OUPUT FILE HERE\SAMPLEFILENAME-'+str(month)+'-'+str(day)+'-'+str(year)+'.xlsx'
writer = pd.ExcelWriter(excel)
# If Index is set to True, an additional column will be created on the first row
# with an index. 
# If Index is set to False, exported file will not have any additional columns
df_merge.to_excel(writer,str(month)+'-'+str(day)+'-'+str(year), index=False)
writer.save()
print(counter,"files merged successfully")
print("File exported")