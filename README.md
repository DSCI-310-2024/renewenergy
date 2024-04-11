# renewenergy

A great package to run aanalysis to help predict the renewable energy output of a country.

[![Documentation Status](https://readthedocs.org/projects/renewenergy/badge/?version=latest)](https://renewenergy.readthedocs.io/en/latest/?badge=latest)

## Installation

```bash
$ pip install renewenergy
```

## Usage
```

from renewenergy.clean_data import clean_data
from renewenergy.eda import create_scatter_plots
from renewenergy.functionread import reading_datain
from renewenergy.impute_split import impute_split
from renewenergy.linear_regression import split_xy_columns, plot_rmse


url= "https://github.com/DSCI-310-2024/renewenergy/raw/makingdocumentation/tests/docs_data.zip"

trial1= reading_datain(url, "testing_data.csv", "data", "imported.csv")

cleaned= clean_data("data/imported.csv", "data", "energy_test.csv", "energy_train.csv",12)
```

## Contributing

Interested in contributing? Check out the contributing guidelines. Please note that this project is released with a Code of Conduct. By contributing to this project, you agree to abide by its terms.

## License

`renewenergy` was created by Neha Menon, Caden Chan, Peter Chen, Tak Sripratak. It is licensed under the terms of the MIT license.

## Credits

`renewenergy` was created with [`cookiecutter`](https://cookiecutter.readthedocs.io/en/latest/) and the `py-pkgs-cookiecutter` [template](https://github.com/py-pkgs/py-pkgs-cookiecutter).
