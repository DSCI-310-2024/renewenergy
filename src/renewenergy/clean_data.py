import click
from io import BytesIO
import pandas as pd
import os
from zipfile import ZipFile
from urllib.request import urlopen
from sklearn.model_selection import train_test_split
import numpy as np
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from renewenergy.impute_split import impute_split

def clean_data(dataread,dataout,datafile1, datafile2, seed):
  """
    Perform all cleaning steps on the dataset 

    Parameters
    ----------
    dataread: str
        Path to dataset
    
    dataout: str
        Path to save training and testing datasets to. 
    
    datafile1: str
        Name of CSV file to save test data to. 
    
    datafile2: str
        Name of CSV file to save training data to. 

    seed: int
        Used to allow for reproduceability of results.
    
    
    Returns
    -------
    training.csv
        CSV containing the training data 
    
    test.csv
        CSV containing the test data 
      

    Examples
    --------
    >>> plot_rmse("data/energy_train.csv", "data/energy_test.csv", "results/" )
    
  """
  np.random.seed(seed)
  data1 = pd.read_csv(dataread)
  data1=data1.pivot_table(index= 'Country Name', values="2015", columns='Indicator Name')
  data1= data1[['Access to electricity (% of population)', 'Adjusted net national income (constant 2015 US$)', 
             'CO2 emissions (kt)', 'Death rate, crude (per 1,000 people)',
              'Land area (sq. km)', 'PM2.5 air pollution, mean annual exposure (micrograms per cubic meter)',
                'Population, total','Renewable energy consumption (% of total final energy consumption)',
             'Renewable electricity output (% of total electricity output)']]
  energy_train, energy_test = impute_split(data1, 0, 0.75, seed)
  os.makedirs(dataout, exist_ok=True)  
  energy_test.to_csv(dataout+"/"+datafile1)  
  energy_train.to_csv(dataout+ "/"+datafile2)
  

