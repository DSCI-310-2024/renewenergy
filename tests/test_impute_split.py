import pandas as pd
import numpy as np
import os
import pathlib
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from src.renewenergy.impute_split import impute_split
import pytest

# Create a sample dataset
data = pd.DataFrame({
    'A': [1, 2, np.nan, 4, 5],
    'B': [np.nan, 2, 3, 4, 5],
    'C': [1, 2, 3, np.nan, 5]
})

# Define Parameters
impute_value = 0
train_size = 0.8



def test_returns_dataframes():
    # Tests whether or not the function returns two data frames
    train, test = impute_split(data, impute_value, train_size)
    assert isinstance(train, pd.DataFrame)
    assert isinstance(test, pd.DataFrame)

def test_NA_values_replaced():
    # Tests if the NA values are replaced within the dataframe
    train, test = impute_split(data, impute_value, train_size)
    assert train.isnull().sum().sum() == 0
    assert test.isnull().sum().sum() == 0

def test_split_sizes():
    # Tests that the size of the train and test sets are correct
    exp_train = int(train_size * len(data))
    exp_test = len(data) - exp_train

    train, test = impute_split(data, impute_value, train_size)
    assert len(train) == exp_train
    assert len(test) == exp_test

def test_no_missing_rows():
    # Tests that the the total size of the train/test splits are the size of the original dataset
    train, test = impute_split(data, impute_value, train_size)
    assert (len(train) + len(test)) == len(data)

def test_splits_different():
    # Tests that the split is random and the train/test splits are different from eachother
    train, test = impute_split(data, impute_value, train_size)
    assert not train.equals(test)
    