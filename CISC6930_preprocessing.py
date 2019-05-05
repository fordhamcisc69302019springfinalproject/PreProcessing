"""

Author: Qiangwen Xu

"""

import pandas as pd
from scipy.stats import zscore
from sklearn import preprocessing
from sklearn.ensemble import RandomForestClassifier
from imblearn.over_sampling import SMOTE
import numpy as np
import time


# Import dataset and set column names
def load_data(path, names):
    df = pd.DataFrame(pd.read_csv(path, header = None))
    df.columns = names
    return df


# Return a dictionary contains all unique value of each feature
def get_unique(df):
    uniqueX = {}
    for f in df.columns:
        uniqueX[f] = df[f].unique()
    return uniqueX


# Return a dictionary contains counted number of each unique value of each feature
def get_distribution(df):
    distribution = {}
    for f in df.columns:
        distribution[f] = {}
        count_tem = df[f].value_counts()
        for u in count_tem.index:
            distribution[f][u] = count_tem[u]
    return distribution


# The following three functions are for normalization.
# Parameter 'col' is a list of column names to be normalized
def zscore_normalize(df, col):
    df_zscore = df
    for c in col:
        df_zscore[c] = df_zscore[c].apply(zscore)
    return df_zscore


def min_max_normalize(df, col):
    df_mm = df
    for c in col:
        mm_scaler = preprocessing.MinMaxScaler()
        df_mm[c] = mm_scaler.fit_transform(df_mm[c].values.reshape(-1,1))
    return df_mm


def encoder_normalize(df, col):
    df_ec = df
    for c in col:
        le = preprocessing.LabelEncoder()
        df_ec[c] = le.fit_transform(df_ec[c].values)
        globals()[c+'_class'] = le.classes_
    return df_ec


# Parameter 'col' is a list of column names to be imputed
def rf_imputation(df, col):
    df_imp = df
    df_miss = df_imp.loc[(df_imp[col[0]].isin(['0'])) | (df_imp[col[1]].isin(['0'])) | (df_imp[col[2]].isin(['0']))] 
    df_imp.drop(df_miss.index, inplace=True)
    for c in col:
        X = df_imp.drop(col+['label'], axis=1)
        y = df_imp[c]
        clf = RandomForestClassifier(n_estimators=10,
                                     random_state=10,
                                     bootstrap=True)
        clf.fit(X, y)
        df_miss[c] = clf.predict(df_miss.drop(col+['label'], axis=1))
    df_imp = df_imp.append(df_miss)
    return df_imp


def feature_extend(df, feature_name):
    df_etd = df
    df_etd = pd.get_dummies(df_etd, columns = [feature_name])
    get_unique(train)[feature_name]
    
    

# Consist label classes btwm train and test data
def consistent_label(pd_dataframe):
    pd_dataframe["label"] = pd_dataframe["label"].replace([" >50K.", " <=50K."], [" >50K", " <=50K"])
    return pd_dataframe


# Quick way to complete preprocess
def preprocess(df):
    df_pp = df
    df_pp = min_max_normalize(df_pp, ['capital_gain', 'capital_loss'])
    df_pp = encoder_normalize(df_pp, ['workclass',
                                      'education',
                                      'marital_status',
                                      'occupation',
                                      'relationship',
                                      'race',
                                      'sex',
                                      'native_country'])
    imp_col = ['workclass', 'occupation', 'native_country']
    df_pp = rf_imputation(df_pp, imp_col)
    return df_pp


if __name__ == "__main__":
    
    # load train data
    train_path = 'census-income.data.csv'
    columns = ['age','workclass','fnlwgt','education','education_num','marital_status','occupation','relationship','race','sex','capital_gain','capital_loss','hours_per_week','native_country','label']
    train = load_data(train_path, columns)
    
    
    # Put all unique value into a dictionary for further querying
    unique = get_unique(train)
    print(unique['workclass'])
    unique_count = get_distribution(train)
    print(unique_count['workclass'][' Local-gov'])
    
    
    # Normalize train data by min_max method
    train = min_max_normalize(train, ['capital_gain', 
                                      'capital_loss'])
    
    
    # Normalize train data by encoder method
    train = encoder_normalize(train, ['workclass', 
                                      'education', 
                                      'marital_status',
                                      'occupation',
                                      'relationship',
                                      'race',
                                      'sex',
                                      'native_country'])
    
    
    # Deal with missing value (around 7.37%) through random forest
    imputate_columns = ['workclass', 'occupation', 'native_country']
    train = rf_imputation(train, imputate_columns)

    # Deal with imbalance through SMOTE
    X_train, y_train = SMOTE().fit_resample(train.drop(['label'], axis=1), train['label'])
    y_train = y_train.reshape(-1,1)
    train = pd.DataFrame(np.hstack((X_train,y_train)))
    train.columns = columns
    
    train.to_csv('census-income.data.precessed_'+str(int(time.time()))+'.csv')