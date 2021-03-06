#!/usr/bin/python

import pickle
from sklearn.cross_validation import train_test_split
from sklearn.metrics import accuracy_score, confusion_matrix, precision_score, classification_report, recall_score
from sklearn.naive_bayes import GaussianNB
from sklearn.linear_model import SGDClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from sklearn.tree import DecisionTreeClassifier

from tools.feature_format import featureFormat, targetFeatureSplit
from tester import dump_classifier_and_data

# Task 1: Select what features you'll use.
features_list = ['poi', 'salary', 'bonus', 'restricted_stock_deferred', 'deferred_income', 'total_stock_value',
                 'exercised_stock_options', 'long_term_incentive', 'restricted_stock']

# Load the dictionary containing the dataset
with open("final_project_dataset.pkl", "r") as data_file:
    data_dict = pickle.load(data_file)


# Task 2: Remove outliers
data_dict.pop("TOTAL", 0)


# Task 3: Create new feature(s)
# Store to my_dataset for easy export below.
my_dataset = data_dict

# List of people on POI list with no emails going to or from others on POI list.
no_email_interaction = []
for key in my_dataset.keys():
    my_dataset[key]['no_emails'] = my_dataset[key]['poi'] \
            and my_dataset[key]['from_messages'] == 'NaN' \
            and my_dataset[key]['shared_receipt_with_poi'] == 'NaN' \
            and my_dataset[key]['from_this_person_to_poi'] == 'NaN' \
            and my_dataset[key]['from_poi_to_this_person'] == 'NaN' \
            and my_dataset[key]['to_messages'] == 'NaN'
    if my_dataset[key]['no_emails']:
        no_email_interaction.append(key)
print no_email_interaction, "are POIs with no emails in the data set."


# Extract features and labels from dataset for local testing

data = featureFormat(my_dataset, features_list, sort_keys=True)
labels, features = targetFeatureSplit(data)


# Task 4: Try a variety of classifiers

# DecisionTreeClassifier()              # Accuracy: Changes, Precision: Changes, Recall: Changes
# SGDClassifier()                       # Accuracy: Changes, Precision: Changes, Recall: Changes
# KNeighborsClassifier(n_neighbors=6)   # Accuracy: .89/.86, Precision: .0,  Recall: .0
# SVC(C=.001, kernel="rbf", gamma=0.1)  # Accuracy: .89/.86, Precision: .0,  Recall: .0
# GaussianNB()                          # Accuracy: .93/.36, Precision: .75/.18, Recall: .5/1.0

# Task 5: Tune your classifier to achieve better than .3 precision and recall
# using our testing script.

features_train, features_test, labels_train, labels_test =\
    train_test_split(features, labels, test_size=0.4, random_state=42)

clf = GaussianNB()
clf = clf.fit(features_train, labels_train)

pred = clf.predict(features_test)
cm = confusion_matrix(labels_test, pred)
acc_score = accuracy_score(pred, labels_test)

print "Accuracy Score:", acc_score
print "Precision Score:", precision_score(labels_test, pred)
print "Recall Score:",  recall_score(labels_test, pred)

print "Total people in training set:", len(labels_train)
print "POIs in training set:", len([e for e in labels_train if e == 1.0])

print "Total people in test set:", len(labels_test)
print "POIs in test set:", len([e for e in labels_test if e == 1.0])

print "Classification Report", classification_report(labels_test, pred)

print "Confusion Matrix:", cm, '\n'
print '{0} True positives'.format(cm[1][1])
print '{0} True negatives'.format(cm[0][0])
print '{0} False positives'.format(cm[0][1])
print '{0} False negatives'.format(cm[1][0])

# Task 6: Dump your classifier, dataset, and features_list so anyone can
# check your results. You do not need to change anything below, but make sure
# that the version of poi_id.py that you submit can be run on its own and
# generates the necessary .pkl files for validating your results.

dump_classifier_and_data(clf, my_dataset, features_list)
