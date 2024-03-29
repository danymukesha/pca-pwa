# pca-pwa

[![Python Tests](https://github.com/danymukesha/pca-pwa/actions/workflows/main.yml/badge.svg)](https://github.com/danymukesha/pca-pwa/actions/workflows/main.yml)

`pca-pwa`, a simplified manner for insights and decision-making by visualizing complex relationships with PCA web application.

### The Purpose of the Package
- The purpose of the package is to offer a simple way of visualizing relatationships between items of any given dataset. 
The user could easily obtain a pca plot without needing to configure or compile the application.

### Installation
To install `pca_pwa`, you can use pip. Open your terminal and run:

```sh
pip install pca_pwa
```
Open `IPython` or `Jupyter Notebook`
```python
>>> from pca_pwa import app
>>> app.app.run(debug=True, use_reloader=True, host='0.0.0.0', port=8082)
>>> # * Serving Flask app 'app'
>>> # * Debug mode: on
>>> # * Running on http://127.0.0.1:8082
```

Open the url: http://127.0.0.1:8082

![image](https://github.com/danymukesha/pca-pwa/assets/45208254/03c32efa-3873-4173-9682-877c51aefdd6)

Upload `xslx/slx` file (Excel) 

- e.g.:
  - Click [here](https://github.com/danymukesha/pca-pwa/raw/main/tests/samples_file.xlsx) to download the excel file
    * Items/Observations should be in rows
    * Variables/Features should in columns
      
        - **Standard Data (table) Format**
        
        The example of standard data format to be used while uploading to pca-pwa web app is a dataframe from sample names
        in the first column, and the rest (e.g.: metabolites, genes, RNA, etc.) for each sample in the following columns (see Table 1).
        
        **Table 1:** ***Standard data table format.***
        
        | Sample | Met 1   | Met 2   | Met 3   | ...     | Met N   |
        |--------|---------|---------|---------|---------|---------|
        | S1     | 99,380  | 10.177  | 51.484  | ...     | 71.882  |
        | S2     | 101.195 | 10.786  | 50.446  | ...     | 73.318  |
        | S3     | 102.165 | 9,375   | 49.668  | ...     | 72,056  |
        | S4     | 99.481  | 8.291   | 48.111  | ...     | 73.282  |
        | S5     | 101.282 | 10.867  | 50.209  | ...     | 73,572  |
        | S6     | 99.43   | 9.95    | 47.602  | ...     | 71,983  |


Choose a method of imputation for missing values.

Then run the pca by clicking ``Perform PCA`` button.

![image](https://github.com/danymukesha/pca-pwa/assets/45208254/a25bf538-599e-4353-80e4-a26963e4d721)

---------

Otherwise you can use `git clone`:

Here is the [Usage](https://github.com/danymukesha/pca-pwa/blob/main/Usage.md):

Clone the github repository

```git
git clone https://github.com/danymukesha/pca-pwa.git
```

Run the app

```sh
cd pca-pwa
python3.1 pca-pwa/app.y

# * Serving Flask app 'app'
# * Debug mode: on
# * Running on http://127.0.0.1:8082
```

Open the url: http://127.0.0.1:8082

### License
This project is licensed under the MIT License.

### Credits
Author: MIT © [Dany Mukesha](https://danymukesha.github.io/)

Email: danymukesha@gmail.com

Thank you for using `pca_pwa`!
