# renewenergy

A great package to run aanalysis to help predict the renewable energy output of a country.

[![codecov](https://codecov.io/gh/DSCI-310-2024/renewenergy/graph/badge.svg?token=X00ruRbQWc)](https://codecov.io/gh/DSCI-310-2024/renewenergy) ![PyPI](https://img.shields.io/pypi/v/renewenergy?label=pypi%20package) [![Documentation Status](https://readthedocs.org/projects/renewenergy/badge/?version=latest)](https://renewenergy.readthedocs.io/en/latest/?badge=latest)
      



## Installation

```bash
$ pip install renewenergy
```

## Usage
```
from renewenergy.clean_data import clean_data
from renewenergy.create_scatter_plots import create_scatter_plots
from renewenergy.reading_data import reading_data
from renewenergy.impute_split import impute_split
from renewenergy.split_xy_columns import split_xy_columns
from renewenergy.plot_rmse import plot_rmse

import pandas as pd
from matplotlib import pyplot as plt
```

## Contributing

Interested in contributing? Check out the [contribution guidelines](https://github.com/DSCI-310-2024/renewenergy/blob/main/CONTRIBUTING.md). Please note that this project is released with a [Code of Conduct](https://github.com/DSCI-310-2024/renewenergy/blob/main/CONDUCT.md). By contributing to this project, you agree to abide by its terms.

## License

`renewenergy` was created by Neha Menon, Caden Chan, Peter Chen, Tak Sripratak. It is licensed under the terms of the MIT license.

## Credits

`renewenergy` was created with [`cookiecutter`](https://cookiecutter.readthedocs.io/en/latest/) and the `py-pkgs-cookiecutter` [template](https://github.com/py-pkgs/py-pkgs-cookiecutter).
