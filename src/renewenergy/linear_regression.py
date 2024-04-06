import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
from sklearn import set_config
from sklearn.metrics import mean_squared_error


def split_xy_columns(dataset):
    #splitting the x and y columns of the data
    dataset_x = dataset
    dataset_x = dataset_x.drop('Renewable electricity output (% of total electricity output)', axis=1)
    dataset_x = dataset_x.drop('Country Name', axis=1)
    dataset_y = dataset[["Renewable electricity output (% of total electricity output)"]]

    return dataset_x, dataset_y

#@click.command()
#@click.option('--training_data_path', help='path of training set data (csv) to read', type=str)
#@click.option('--test_data_path', help='path of test set data (csv) to read', type=str)
#@click.option('--output_path', help='folder path to save the results, need to end with.png', type=str)

def plot_rmse(training_data_path, test_data_path, output_path):
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