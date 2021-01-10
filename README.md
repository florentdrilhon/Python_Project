# Python_Project
### Python for data analysis project with QSAR biodegradation dataset

So the dataset I am working on is the QSAR biodegradation dataset available here : https://archive.ics.uci.edu/ml/datasets/QSAR+biodegradation
The purpose of this work is to build a model able to predict if a chemical is ready biodegradable or not.

To analyse the dataset and construct the model I followed an approach described in the report.pdf file.

To synthetise here is the summary and some conclusions about the different steps:

Data exploratory:
-Structural analysis
1000 rows, 41 parameters, a binary target

-Content analysis
relations between the different features and the target, and among the features themselves.

-Relations/Hypothesis check
Some of the features seem linked. 

After the exploratory, we conclude that we have a small dataset but fully exploitable because no missing values. Nearly all the features seem to be important so the next parts will give us more information about which we keep or not.

Preprocessing:
-Structuration of the data
encoding of the target, train and test split

-Evaluation process
Studying the f1-score, the accuracy and the learning curves to look the performance of the models

-Feature engineering
Creation of new features not convincing. Use of a selector to reduce the number of features and avoid the overfitting as the dataset is small. Creation of a transformer to scale the continuous features ONLY for the models that need it.

After the preprocessing, we keep 16 features and add the scaler for the models who need it by creating two different preprocessing pipelines.

Model selection:
-Model comparison
comparison of different models identified for our case -> support vector machine and adaboost seem to be the best models to improve

-Hyper-parameters adjustments
RandomizedSearchCV to find the best parameters of the models. SVM improve while adaBoost is stagnating because the dataset is too small.

-Threshold selection (bonus)
Selection of a threshold to maximize the f1-score of the predictions.

Conclusion:

The support vector machine with a rbf kernel stands out as the best model in our case. 


###flask app

For the flask app, I made another python file named "final_model.py" that goes straight toward the final model construction. I made this file to avoid different versions issues and to make sure the model is compatible with environnement created for flask app.

Speaking about, to create the flask app, an environnement was created, all the packages are summarized in the "requirements.txt" file, install it all to ensure the good functionning of the app.

All the html pages are in the "template" folder.


Thanks a lot for the all the interesting things we learned in this great course !



