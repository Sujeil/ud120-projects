#!/usr/bin/python

from tools.feature_format import featureFormat, targetFeatureSplit
from sklearn.cross_validation import train_test_split
import pickle
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.metrics import accuracy_score, mean_squared_error, r2_score

"""
    Starter code for the regression mini-project.
    
    Loads up/formats a modified version of the data set
    (why modified?  we've removed some trouble points
    that you'll find yourself in the outliers mini-project).

    Draws a little scatter plot of the training/testing data

    You fill in the regression code where indicated:
"""    

dictionary = pickle.load(open("../final_project/final_project_dataset_modified.pkl", "r"))


# list the features you want to look at--first item in the
# list will be the "target" feature
features_list = ["expenses", "salary"]
data = featureFormat(dictionary, features_list, remove_any_zeroes=True)
target, features = targetFeatureSplit(data)

# training-testing split needed in regression, just like classification

feature_train, feature_test, target_train, target_test = \
    train_test_split(features, target, test_size=0.5, random_state=42)
train_color = "b"
test_color = "r"

# Create linear regression object
reg = LinearRegression()

# Train the model using the training sets
reg.fit(feature_train, target_train)

# Make predictions using the testing set
prediction = reg.predict(feature_test)

# The coefficients
print "Coefficients or slope:", reg.coef_

# The intercept
print "Intercept:", reg.intercept_

# Stats on test data
print "\nStats on test data"
print "R-squared score:", reg.score(feature_test, target_test)

print "\nStats on training data"
print "R-squared score", reg.score(feature_train, target_train)

# The mean squared error
print "\nMean squared error: %.2f", mean_squared_error(feature_test, prediction)

# The coefficient of determination: 1 is perfect prediction
print "Coefficient of determination:", r2_score(feature_test, prediction)


# draw the scatter plot, with color-coded training and testing points

for feature, target in zip(feature_test, target_test):
    plt.scatter( feature, target, color=test_color ) 
for feature, target in zip(feature_train, target_train):
    plt.scatter( feature, target, color=train_color ) 

# labels for the legend
plt.scatter(feature_test[0], target_test[0], color=test_color, label="test")
plt.scatter(feature_test[0], target_test[0], color=train_color, label="train")


# draw the regression line, once it's coded
try:
    plt.plot(feature_test, reg.predict(feature_test))
except NameError:
    pass

reg.fit(feature_test, target_test)
print "Coefficients or slope:", reg.coef_
plt.plot(feature_train, reg.predict(feature_train), color="b")

plt.xlabel(features_list[1])
plt.ylabel(features_list[0])
plt.legend()
plt.show()
