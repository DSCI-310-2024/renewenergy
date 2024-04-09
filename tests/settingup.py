import os
import zipfile
import pandas as pd

data_for_df= {'Country':['Canada', 'US', 'Jamaica'],
        'Number':[20, 21, 19]}
data= pd.DataFrame(data_for_df)

#make a directory with file called WDICSV.csv
file1= open("test1.csv", "w")
file1.write("this is a test file")

# file2= open("testing_data.csv", "w")
# file2.write("need to put")
data.to_csv('targ.csv', index=False)



#make a empty zip file
with zipfile.ZipFile('emptyfile.zip', 'w', zipfile.ZIP_STORED) as zipf:
    pass

with zipfile.ZipFile('dummydata.zip', 'w', zipfile.ZIP_STORED) as zipf:
    # zipf.write('test1.csv')
    zipf.write("targ.csv")
    zipf.write("test1.csv")
  