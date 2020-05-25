#!/usr/bin/python


"""
    Starter code for the evaluation mini-project.
    Start by copying your trained/tested POI identifier from
    that which you built in the validation mini-project.

    This is the second step toward building your POI identifier!

    Start by loading/formatting the data...
"""
import pickle
import numpy as np
from sklearn.cross_validation import train_test_split
from sklearn.metrics import confusion_matrix, precision_score, classification_report, recall_score
from sklearn.tree import DecisionTreeClassifier

from tools.feature_format import featureFormat, targetFeatureSplit

data_dict = pickle.load(open("../final_project/final_project_dataset.pkl", "r") )

# add more features to features_list!
features_list = ['poi', 'salary', 'expenses', 'total_payments', 'from_poi_to_this_person', 'from_this_person_to_poi', 'shared_receipt_with_poi']

data = featureFormat(data_dict, features_list)
labels, features = targetFeatureSplit(data)


# your code goes here
features_train, features_test, labels_train, labels_test = \
    train_test_split(features, labels, test_size=0.4, random_state=42)

clf = DecisionTreeClassifier()

clf = clf.fit(features_train, labels_train)

pred = clf.predict(features_test)
cm = confusion_matrix(labels_test, pred)
print "POIs in test set for POI identifier:", len([e for e in labels_test if e == 1.0])

print "People total are in test set:", len(labels_test)

print "Precision Score:", precision_score(labels_test, pred)

print "Classification Report", classification_report(labels_test, pred)

num_features = len(features_train[0])
print "Number of features:", num_features

print "Recall Score:",  recall_score(labels_test, pred)

print "Confusion Matrix:", cm, '\n'
print '{0} True positives'.format(cm[1][1])
print '{0} True negatives'.format(cm[0][0])
print '{0} False positives'.format(cm[0][1])
print '{0} False negatives'.format(cm[1][0])
