import requests
from io import BytesIO
# import urllib.request as urllib2
import pandas as pd
import os
from zipfile import ZipFile
from urllib.request import urlopen
import pathlib

def reading_datain(url, data_file, data_path, file_name):
    """Simple program that reads in the data from a URL, and selects a file from the .zip."""
    request= requests.get(url)

    if request.status_code !=200:
        raise ValueError('The inputed URL does not exist.')
    
    if url[-4:] !=".zip":
        raise ValueError('The inputed URL is not a ZIP file, please input a ZIP file')
    data_url= urlopen(url)
    file = ZipFile(BytesIO(data_url.read()))
    loa=file.namelist()
    if data_file not in loa: 
        raise ValueError("The specified file is not present within the inputed ZIP file")

    data_csv = file.open(data_file)
    data = pd.read_csv(data_csv)
    os.makedirs(data_path, exist_ok=True)  
        
    path = pathlib.Path(data_path+"/"+file_name)
    if os.path.exists(path):
        raise ValueError("The filename already exists.")
    else: 
        return data.to_csv(data_path+"/"+file_name)  
       

if __name__ == '__main__':
    reading_datain()