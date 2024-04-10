import pandas as pd
import sys
import pathlib
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from renewenergy.reading_data import reading_data
import pytest


empty_zip="https://github.com/DSCI-310-2024/DSCI310-Group14/blob/testing1/tests/emptyfile.zip"

zip_with_files= "https://github.com/DSCI-310-2024/DSCI310-Group14/raw/testing1/tests/dummydata.zip"

invalid_url="https://github.com/DSCI-310-2024/DSCI310-Group14/blob/testing1/tests/emptyfil"

no_zip_url= "https://github.com/DSCI-310-2024/DSCI310-Group14/blob/testing1/tests/test1.csv"

#will test if function works as it is meant to

def test_path_exists():
    # url= 'https://databank.worldbank.org/data/download/WDI_CSV.zip'
    trial1=reading_data(zip_with_files,"targ.csv", "data/raw","downloaded.csv")
    path = pathlib.Path("data/raw/downloaded.csv")
    assert os.path.exists(path)

def test_url_not_exist():
    # url= 'https://github.com/ttimbers/breast_cancer_predictor_py/blob/main/src/read_zip'
    with pytest.raises(ValueError, match='The inputed URL does not exist.'):
        reading_data(invalid_url,"WDICSV.csv", "data/raw","downloaded.csv")

def test_nozip():
    # url= 'https://databank.worldbank.org'
    with pytest.raises(ValueError, match='The inputed URL is not a ZIP file, please input a ZIP file'):
        reading_data(no_zip_url,"WDICSV.csv", "data/raw","downloaded.csv")

def test_specified_file_does_not_exist():
    # url="https://databank.worldbank.org/data/download/WDI_CSV.zip"
    with pytest.raises(ValueError, match="The specified file is not present within the inputed ZIP file"):
        reading_data(zip_with_files, "fakename.csv", "data/raw","downloaded.csv")

def test_filename_exists():
    # url="https://databank.worldbank.org/data/download/WDI_CSV.zip"
    with pytest.raises(ValueError, match="The filename already exists."):
        reading_data(zip_with_files,"targ.csv", "data/raw","downloaded.csv")

def test_clean_up():
    os.remove("data/raw/downloaded.csv")
    path = pathlib.Path("data/raw/downloaded.csv")
    assert not os.path.exists(path)

# def test_clean_up_dir():
#     os.remove("tests/dummydata.zip")
#     os.remove("tests/emptyfile.zip")
#     os.remove('tests/targ.csv')
#     os.remove("tests/test1.csv")
#     path1 = pathlib.Path("tests/dummydata.zip")
#     path2 = pathlib.Path("tests/emptyfile.zip")
#     path3 = pathlib.Path("tests/targ.csv")
#     path4 = pathlib.Path("tests/test1.csv")
#     assert not os.path.exists(path1) and not os.path.exists(path2) and not os.path.exists(path3) and not os.path.exists(path4)

# def test_path_preexisting():
#     url=""
#     with pytest.raises(ValueError, match="The filepath already exists."):
#         reading_datain(url, "", "", "")
        
# def test_zip():
#     url="https://databank.worldbank.org/data/download/WDI_CSV.zip"
#     with pytest.raises(ValueError, match="The specified file is not present within the inputed ZIP file"):
#         reading_datain(url, "WDICSV.csv", "data/raw","downloaded.csv")
        





 