import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
from sklearn import set_config
from sklearn.metrics import mean_squared_error


def split_xy_columns(dataset):
    """
    Split a dataset into X (explanatory variables) and Y (target variables).

    Parameters
    ----------
    dataset : pandas dataframe

    Returns
    -------
    dataset.x
        Pandas dataframe containing explanatory variables
    
    dataset.y
        Pandas dataframe containing target variable

    Examples
    --------
    >>> split_xy_columns(imported_df)
    
    """

    #splitting the x and y columns of the data
    dataset_x = dataset
    dataset_x = dataset_x.drop('Renewable electricity output (% of total electricity output)', axis=1)
    dataset_x = dataset_x.drop('Country Name', axis=1)
    dataset_y = dataset[["Renewable electricity output (% of total electricity output)"]]

    return dataset_x, dataset_y