# License  
This project is licensed under GNU GPLv3.
For details, see: https://github.com/fordhamcisc69302019springfinalproject/PreProcessing/blob/master/LICENSE

All other rights reserved.

# Documentations  
## Overview
- Train data after pre-processed has been saved into *census-income.data.precessed.csv*
- You can complete normalization, imputation and balancing process with this tool.  
There are two ways to make use of this tool:  
1. Directly open *CISC6930_preprocessing.py*, customize parameters and arguements below:  
```Python
if __name__ == "__main__":
```  
After execute all code, you should get the following variables:
- **train**:  train data, which has been normalized and imputed;
- **X_train, y_train**:  observations and labels respectly from train data, balanced by SMOTE;

2. Put *CISC6930_preprocessing.py* in the same directory of your code. Then use it as a module.  
Example:  
```Python
import CISC6930_preprocessing as pp

train_path = 'census-income.data.csv'
columns = ['age','workclass','fnlwgt','education','education_num','marital_status','occupation','relationship','race','sex','capital_gain','capital_loss','hours_per_week','native_country','label']

train = pp.load_data(train_path, columns)

train = pp.preprocess(train)
```  

## Functions
From *CISC6930_preprocessing*, you can call those functions:  

### load_data(path, names)  
- Parameters:  
path: string
names: list of strings or integer
- Return: dataframe  

### get_unique(df)
- Parameters:  
df: dataframe
- Return: dictionary (contains all unique value of each feature)
- Example:
```Python
>>> unique = get_unique(train)
>>> print(unique['workclass'])
[' State-gov' ' Self-emp-not-inc' ' Private' ' Federal-gov' ' Local-gov'
 ' ?' ' Self-emp-inc' ' Without-pay' ' Never-worked']
```

### get_distribution(df)
- Parameters:  
df: dataframe
- Return: dictionary (contains counted number of each unique value of each feature)
- Example:
```Python
>>> unique_count = get_distribution(train)
>>> print(unique_count['workclass'][' Local-gov'])
2093
```

### zscore_normalize(df, col)
- Parameters:  
df: dataframe
col: list (column names to be normalized)
- Return: dataframe


### min_max_normalize(df, col)
- Parameters:  
df: dataframe
col: list (column names to be normalized)
- Return: dataframe

### encoder_normalize(df, col)
- Parameters:  
df: dataframe
col: list (column names to be normalized)
- Return: dataframe

### rf_imputation(df, col)
- Parameters:  
df: dataframe
col: list (column names to be imputed)
- Return: dataframe

### preprocess(df)
**It is a quick function to do all above things**
- Parameters:  
df: dataframe
- Return: dataframe
