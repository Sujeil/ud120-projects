#!/usr/bin/python

from sklearn.cross_validation import train_test_split
from sklearn.linear_model import LinearRegression
import pickle
import numpy
import matplotlib.pyplot as plt
from outliers.outlier_cleaner import outlierCleaner

# load up some practice data with outliers in it
ages = pickle.load(open("practice_outliers_ages.pkl", "r"))
net_worths = pickle.load(open("practice_outliers_net_worths.pkl", "r"))


# ages and net_worths need to be reshaped into 2D numpy arrays
# second argument of reshape command is a tuple of integers: (n_rows, n_columns)
# by convention, n_rows is the number of data points
# and n_columns is the number of features

ages = numpy.reshape(numpy.array(ages), (len(ages), 1))
net_worths = numpy.reshape(numpy.array(net_worths), (len(net_worths), 1))

ages_train, ages_test, net_worths_train, net_worths_test = \
    train_test_split(ages, net_worths, test_size=0.1, random_state=42)


# Create linear regression object
reg = LinearRegression()

# Train the model using the training sets
reg.fit(ages_train, net_worths_train)

# Make predictions using the testing set
prediction = reg.predict(ages_test)

# The coefficients
print "Coefficients or slope:", reg.coef_

# The intercept
print "Intercept:", reg.intercept_

# Stats on test data
print "\nStats on test data"
print "R-squared score:", reg.score(ages_test, net_worths_test)

print "\nStats on training data"
print "R-squared score", reg.score(ages_train, net_worths_train)

try:
    plt.plot(ages, reg.predict(ages), color="blue")
except NameError:
    pass
plt.scatter(ages, net_worths)
plt.show()


# identify and remove the most outlier-y points
cleaned_data = []
try:
    predictions = reg.predict(ages_train)
    cleaned_data = outlierCleaner(predictions, ages_train, net_worths_train)
except NameError:
    print "your regression object doesn't exist, or isn't name reg"
    print "can't make predictions to use in identifying outliers"







# only run this code if cleaned_data is returning data
if len(cleaned_data) > 0:
    ages, net_worths, errors = zip(*cleaned_data)
    ages = numpy.reshape(numpy.array(ages), (len(ages), 1))
    net_worths = numpy.reshape(numpy.array(net_worths), (len(net_worths), 1))

    # refit your cleaned data!
    try:
        reg.fit(ages, net_worths)
        plt.plot(ages, reg.predict(ages), color="blue")

        # The coefficients
        print "Coefficients or slope:", reg.coef_

        # The intercept
        print "Intercept:", reg.intercept_

        # Stats on test data
        print "\nStats on test data"
        print "R-squared score:", reg.score(ages_test, net_worths_test)

        print "\nStats on training data"
        print "R-squared score", reg.score(ages_train, net_worths_train)

    except NameError:
        print "you don't seem to have regression imported/created,"
        print "   or else your regression object isn't named reg"
        print "   either way, only draw the scatter plot of the cleaned data"
    plt.scatter(ages, net_worths)
    plt.xlabel("ages")
    plt.ylabel("net worths")
    plt.show()


else:
    print "outlierCleaner() is returning an empty list, no refitting to be done"

