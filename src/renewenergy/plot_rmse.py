import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
from sklearn import set_config
from sklearn.metrics import mean_squared_error


# def split_xy_columns(dataset):
#     """
#     Read a specified data file in from a URL containing a zip file.

#     Parameters
#     ----------
#     url : str
#         URL of link containing zip file. 
    
#     data_file: str
#         Specified file in .ZIP that data is to be extracted from. 
    
#     data_path: str
#         Directory to which the imported data should be saved to. 
    
#     file_name: str
#         Name of file that imported data will be saved to. 
    

#     Returns
#     -------
#     file_name.csv
#         CSV file that data is saved to. 

#     Examples
#     --------
#     >>> reading_datain("url", "WDICSV.csv", "data/raw", "downloaded_data.csv" )
    
#     """

#     #splitting the x and y columns of the data
#     dataset_x = dataset
#     dataset_x = dataset_x.drop('Renewable electricity output (% of total electricity output)', axis=1)
#     dataset_x = dataset_x.drop('Country Name', axis=1)
#     dataset_y = dataset[["Renewable electricity output (% of total electricity output)"]]

#     return dataset_x, dataset_y

#@click.command()
#@click.option('--training_data_path', help='path of training set data (csv) to read', type=str)
#@click.option('--test_data_path', help='path of test set data (csv) to read', type=str)
#@click.option('--output_path', help='folder path to save the results, need to end with.png', type=str)

def plot_rmse(training_data_path, test_data_path, output_path):
    """
    Perform linear regression and plot the results on a graph containing Expected vs Predicted. 

    Parameters
    ----------
    training_data_path: str
        Path to training data .csv file
    
    test_data_path: str
        Path to test data .csv file
    
    output_path: str
        Directory to which the figure should be saved to. 
    
    
    Returns
    -------
    results.png
        Figure containing the Predicted vs Expected Values of the linear regression.

    Examples
    --------
    >>> plot_rmse("data/energy_train.csv", "data/energy_test.csv", "results/" )
    
    """
    #read clean train and test dataset

    energy_train = pd.read_csv(training_data_path)
    energy_test = pd.read_csv(test_data_path)

    #splitting the x and y columns of the data

    energy_train_x, energy_train_y = split_xy_columns(energy_train)
    energy_test_x, energy_test_y = split_xy_columns(energy_test)
    
    #making the linear model
    lm=LinearRegression()
    lm.fit(energy_train_x, energy_train_y)
    
    y_true = energy_test_y['Renewable electricity output (% of total electricity output)']
    y_pred = lm.predict(energy_test_x)
    energy_RMSE = mean_squared_error(y_true=y_true,
                                     y_pred=y_pred)**(1/2)

    fig = plt.figure()
    plt.scatter(x=y_pred, y=energy_test_y['Renewable electricity output (% of total electricity output)'])
    plt.title(f"Predicted vs. Ground Truth Target Value (RMSE={energy_RMSE})")
    plt.xlabel("Predicted Values")
    plt.ylabel("True Values")
    plt.savefig(output_path)
    return energy_RMSE, fig

#if __name__ == '__main__':
#    plot_rmse()