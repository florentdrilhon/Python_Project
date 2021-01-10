from flask import (Flask,
                   redirect,
                   render_template,
                   abort, url_for, session)

from flask_script import Manager
from flask_bootstrap import Bootstrap
from joblib import load
import numpy as np
import pandas as pd
from werkzeug.exceptions import HTTPException

from collections import OrderedDict
import os
from random import randint

from wtforms import StringField, SubmitField, IntegerField
from wtforms.validators import DataRequired, Length
from flask_wtf import Form



#loading the model

model=load('model.joblib')


# loading the datas (same code as the notebook)

description={}
file=open('data/description.txt','r')
for l in file:
    data=[str(d)for d in l.split(": ")]
    name=[str(n) for n in data[0].split(") ") ]
    descr=[str(des)for des in data[1].split("\n")]
    description[name[1]]=descr[0]
    

names=[]
for key,value in description.items():
    names.append(value)
names[-1]='experimental class'
df=pd.read_csv('data/biodeg.csv',names=names, delimiter=';')
X=df.drop('experimental class', axis=1)



#### as I used a selector, I got the indexes of the features the model keeped:

selected_indexes=[ 1,  2,  4,  5,  6,  8,  9, 13, 18, 19, 25, 31, 36, 37, 38, 39]
features=[]
for i in selected_indexes:
    features.append(df.columns[i])





# initialization of the flask app

app = Flask(__name__, template_folder="template")
bootstrap = Bootstrap(app)
app.config["SECRET_KEY"] = "secret"





@app.route('/')
def home():
    return redirect("/welcome_page")
	

@app.route('/welcome_page', methods=['POST','GET'])
def myfonction():
	form=MyForm()
	
	if form.validate_on_submit():
		return redirect("/predict")

	return render_template("Welcome_page.html", descr=features, form=form)
	


@app.route('/predict',methods=['POST','GET'])
def prediction():

	form=MyForm()
	if form.validate_on_submit():
		return redirect("/predict")

	index=randint(0, X.shape[0])
	y=model.predict(X)

	# to show only the selected features
	intermediate_X=dict()
	for i in range(len(selected_indexes)):
		intermediate_X[features[i]]= X.iloc[index, selected_indexes[i]]

	if y[index]==1:
		return render_template("predict_RB.html", X=intermediate_X,form=form)
	else :
		return render_template("predict_NRB.html", X=intermediate_X,form=form)






class MyForm(Form):
	submit = SubmitField("Test it now")







if __name__ == "__main__":
	
    app.run(debug=True)