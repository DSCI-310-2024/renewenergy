import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
from sklearn import set_config
from sklearn.metrics import mean_squared_error
import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from renewenergy.split_xy_columns import split_xy_columns

data = {
        'Feature1': [1, 2, 3],
        'Feature2': [4, 5, 6],
        'Country Name': ['a', 'b', 'c'],
        'Renewable electricity output (% of total electricity output)': [10, 20, 30]
    }
dataset = pd.DataFrame(data)

def test_x_column_exist():
    dataset_x, dataset_y = split_xy_columns(dataset)
    # Check if dataset_x and dataset_y are pandas DataFrames
    assert isinstance(dataset_x, pd.DataFrame), "dataset_x is not a pandas DataFrame"

def test_y_column_exist():
    dataset_x, dataset_y = split_xy_columns(dataset)
    # Check if dataset_x and dataset_y are pandas DataFrames
    assert isinstance(dataset_y, pd.DataFrame), "dataset_y is not a pandas DataFrame"

def check_expected_x_columns():
    dataset_x, dataset_y = split_xy_columns(dataset)
    # Check if dataset_x contains only features and dataset_y contains only the target column
    expected_columns_x = set(['Feature1', 'Feature2'])
    expected_columns_y = set(['Renewable electricity output (% of total electricity output)'])
    assert set(dataset_x.columns) == expected_columns_x, "dataset_x does not contain the expected features"

def check_drop_columns():
    dataset_x, dataset_y = split_xy_columns(dataset)
    # Check if dataset_x contains only features and dataset_y contains only the target column
    assert ('Country Name' not in dataset_x.columns)

def check_expected_x_columns():
    dataset_x, dataset_y = split_xy_columns(dataset)
    expected_columns_y = set(['Renewable electricity output (% of total electricity output)'])
    assert set(dataset_y.columns) == expected_columns_y, "dataset_y does not contain the expected target column"