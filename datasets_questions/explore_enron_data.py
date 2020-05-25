#!/usr/bin/python
# coding=utf-8

""" 
    Starter code for exploring the Enron dataset (emails + finances);
    loads up the dataset (pickled dict of dicts).

    The dataset has the form:
    enron_data["LASTNAME FIRSTNAME MIDDLEINITIAL"] = { features_dict }

    {features_dict} is a dictionary of features associated with that person.
    You should explore features_dict as part of the mini-project,
    but here's an example to get you started:

    enron_data["SKILLING JEFFREY K"]["bonus"] = 5600000

"""

import pickle

enron_data = pickle.load(open("../final_project/final_project_dataset.pkl", "rb"))

# How many data points (people) are in the data set?
len(enron_data)
print "Number of data points (people) that are in the data set", len(enron_data.keys())

# For each person, how many features are available?
len(enron_data.values()[0])
enron_data[enron_data.keys()[0]]
print "Number of features available for each person", len(enron_data['SKILLING JEFFREY K'])

# How many POIs were there total?
poi_names_text = '../final_project/poi_names.txt'
poi_names = open(poi_names_text, 'r')
names = poi_names.readlines()
print "Number of POIs total", len(names[2:])
poi_names.close()

# How many POIs are there in the E+F (emails + finances) data set
count = 0
for user in enron_data:
    if enron_data[user]['poi']:
        count += 1
print "Number of POIs in the E+F data set", count

# How many folks in this data set have a quantified salary?
count_salary = 0
for key in enron_data.keys():
    if enron_data[key]['salary'] != 'NaN':
        count_salary += 1
print "Number of people in data set with quantified salary", count_salary

# How many people in the E+F data set (as it currently exists) have “NaN” for their salary?
# What percentage of people in the data set as a whole is this?
count_NaN_salary = 0
for key in enron_data.keys():
    if enron_data[key]['salary'] == 'NaN':
        count_NaN_salary += 1
print "Number of total people in the E+F data set that have NaN for salary", count_NaN_salary
print "As a percent of total", float(count_NaN_salary) / len(enron_data.keys())

# How many POIs in the E+F data set have “NaN” for their salary?
# What percentage of POI’s as a whole is this?
count_NaN_POI_salary = 0
for key in enron_data.keys():
    if enron_data[key]['salary'] == 'NaN' and enron_data[key]['poi']:
        count_NaN_POI_salary += 1
print "Number of POIs in the E+F data set that have NaN for salary", count_NaN_POI_salary
print "As a percent of total", float(count_NaN_POI_salary) / len(enron_data.keys())

# Who has "NaN" for their salary?
no_sal_poi = []
for key in enron_data.keys():
    if enron_data[key]['salary'] == 'NaN' and enron_data[key]['poi']:
        no_sal_poi.append(key)
print no_sal_poi, "has no salary in the data set."

# How many people in this data set have quantified expenses?
count_expenses = 0
for key in enron_data.keys():
    if enron_data[key]['expenses'] != 'NaN':
        count_expenses += 1
print "Number of people with quantified expenses", count_expenses
print "As a percent of total", float(count_expenses) / len(enron_data.keys())

# How many POIs in this data set have quantified expenses?
count_expenses = 0
for key in enron_data.keys():
    if enron_data[key]['expenses'] != 'NaN' and enron_data[key]['poi']:
        count_expenses += 1
print "Number of POIs with quantified expenses", count_expenses
print "As a percent of total", float(count_expenses) / len(enron_data.keys())

# How many people having missing expenses?
count_no_expenses = 0
for key in enron_data.keys():
    if enron_data[key]['expenses'] == 'NaN':
        count_no_expenses += 1
print "Number of people without quantified expenses", count_no_expenses
print "As a percent of total", float(count_no_expenses) / len(enron_data.keys())

# How many POIs having missing expenses?
count_no_expenses = 0
for key in enron_data.keys():
    if enron_data[key]['expenses'] == 'NaN' and enron_data[key]['poi']:
        count_no_expenses += 1
print "Number of POIs without quantified expenses", count_no_expenses
print "As a percent of total", float(count_no_expenses) / len(enron_data.keys())

# What about a known email address?
count_email = 0
for key in enron_data.keys():
    if enron_data[key]['email_address'] != 'NaN':
        count_email += 1
print "Number of people in data set with a known email address", count_email

# What about any without an email addresses?
count_no_email = 0
for key in enron_data.keys():
    if enron_data[key]['email_address'] == 'NaN':
        count_no_email += 1
print "Number of people in data set without an email address", count_no_email
print "As a percent of total", float(count_no_email) / len(enron_data.keys())

# What about any POIs without an email addresses?
count_no_POI_email = 0
for key in enron_data.keys():
    if enron_data[key]['email_address'] == 'NaN' and enron_data[key]['poi']:
        count_no_POI_email += 1
print "Number of POIs without an email address", count_no_POI_email
print "As a percent of total", float(count_no_POI_email) / len(enron_data.keys())

##########################

# So what information do we have for Joseph Hirko?
matching = [s for s in enron_data.keys() if "HIRKO" in s]
print matching
print enron_data['HIRKO JOSEPH']
