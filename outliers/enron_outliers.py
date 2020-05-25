#!/usr/bin/python

import pickle
import matplotlib.pyplot
from tools.feature_format import featureFormat, targetFeatureSplit


# read in data dictionary, convert to numpy array
data_dict = pickle.load(open("../final_project/final_project_dataset.pkl", "r"))

# list the features you want to look at--first item in the
# list will be the "target" feature
features = ["salary", "bonus"]
data_dict.pop("TOTAL", 0)
data = featureFormat(data_dict, features, remove_any_zeroes=True)
target, features = targetFeatureSplit(data)

for point in data:
    salary = point[0]
    bonus = point[1]
    matplotlib.pyplot.scatter(salary, bonus)

matplotlib.pyplot.xlabel("salary")
matplotlib.pyplot.ylabel("bonus")
matplotlib.pyplot.show()


