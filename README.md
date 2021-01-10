# Python_Project
### Python for data analysis project with QSAR biodegradation dataset

So the dataset I am working on is the QSAR biodegradation dataset available here : https://archive.ics.uci.edu/ml/datasets/QSAR+biodegradation
The purpose of this work is to build a model able to predict if a chemical is ready biodegradable or not.

The objective I chose is to act on f1-score and the accuracy to provide a polyvalent model.

To analyse the dataset and construct the model I followed an approach described in the report.pdf file.

To synthetise here is the summary and some conclusions about the different steps:

**Data exploratory:**



After the exploratory, we conclude that we have a small dataset but fully exploitable because no missing values. Nearly all the features seem to be important so the next parts will give us more information about which we keep or not. Moreover, we have made several groups of features by identifying relations between them. So we have the "number of atoms" group which gather the features about the number of the designated atom present in the chemical, we have the "presence/absence" group which gather the features about presence/absence of certain bonds, and we gather all the continuous features to make it easier to scale them in the future.



**Preprocessing:**



First we structurated the data by encoding the target and spliting the dataset in test and train split. Then, after evaluating a first model in overfitting, we chose to reduce the number of features in the model.So, we kept 16 features selected by a recuserive feature elimination selector, and add the scaler for the models who need it by creating two different preprocessing pipelines. We tried to created two new features but their results were not convincing.



**Model selection:**



After a comparison of different models identified for our case, support vector machine and adaboost seemed to be the best models to improve. Then we used a RandomizedSearchCV to find the best parameters of the models. SVM made good progress while adaBoost was stagnating because the dataset is too small. Finaly we selected a threshold to maximize the f1-score of the predictions which was our initial goal.






**Conclusion:**

The support vector machine with a rbf kernel stands out as the best model in our case. 


## Flask app

For the flask app, I made another python file named "final_model.py" that goes straight toward the final model construction. I made this file to avoid different versions issues and to make sure the model is compatible with environnement created for flask app.

Speaking about, to create the flask app, an environnement was created, all the packages are summarized in the "requirements.txt" file, install it all to ensure the good functionning of the app.

All the html pages are in the "template" folder.


Thanks a lot for the all the interesting things we learned in this great course !



