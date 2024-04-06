import pandas as pd
from sklearn.model_selection import train_test_split
import numpy


def impute_split(data, impute_val, train_size, rand_seed=0):  
    """
    Takes a data frame and creates a a training and testing split, with imputation for NA values

    Parameters:
    - data: The initial dataset (DataFrame) to be tidied
    - impute_value: The value to replace all NA values with within the dataset
    - train_size: A value from 0-1 that represents the % of data to be used in the training split (remainder will be used in testing split)
    - rand_seed: A seed value to be used for randomness, allowing for reproducible results; default value is 0

    Returns:
    train: Imputed, training dataset split
    test: Imputed, testing dataset split
    """

    numpy.random.seed(rand_seed)
    data = data.fillna(impute_val)
    train, test = train_test_split(data, train_size = train_size)
    return train, test