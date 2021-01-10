import os
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.pipeline import make_pipeline
from sklearn.compose import make_column_transformer
from sklearn.preprocessing import StandardScaler
from sklearn.feature_selection import RFECV
from sklearn.linear_model import SGDClassifier
from sklearn.svm import SVC
from joblib import dump

description={}
file=open('data/description.txt','r')
for l in file:
    data=[str(d)for d in l.split(": ")]
    name=[str(n) for n in data[0].split(") ") ]
    descr=[str(des)for des in data[1].split("\n")]
    description[name[1]]=descr[0]
    
# as the given names are not significant at all, we use the description as names

names=[]
for key,value in description.items():
    names.append(value)
# exept for the target value which is too descriptive
names[-1]='experimental class'

data=pd.read_csv('data/biodeg.csv',names=names, delimiter=';')
df=data.copy()

def col_by_name(dataframe,name):
    res=[]
    for col in dataframe.columns:
        if name.lower() in col.lower():
            res.append(col)
    return res

def col_by_type(dataframe,dtype):
    res=[]
    for col in dataframe.select_dtypes(dtype):
            res.append(col)
    return res

trainset,testset=train_test_split(df,test_size=0.2, random_state=1)

def encryption(df):
    code={'RB':1,'NRB':0}
    for col in df.select_dtypes(include=['object']).columns:
        df.loc[:,col]=df[col].map(code)
    return df

def preprocessing(df):
    
    df=encryption(df)
    
    X=df.drop('experimental class', axis=1)
    y=df['experimental class']
    
    
    print(y.value_counts())
    return X,y

X_train, y_train=preprocessing(trainset)
X_test, y_test=preprocessing(testset)

continuous_features=col_by_type(df,'float64')
continuous_pipeline=make_pipeline(StandardScaler())
transformer=make_column_transformer((continuous_pipeline,continuous_features))

selector = RFECV(SGDClassifier(random_state=0),
                step=1,
                min_features_to_select=4,
                cv=8)

preprocessor_other=make_pipeline(transformer, selector)

final_model=make_pipeline(preprocessor_other, SVC(C=1481, gamma=0.001,random_state=0))
final_model.fit(X_train,y_train)


print(final_model.score(X_test,y_test))

dump(final_model,'model.joblib')