#You Li
#As always, attempt your lab without searching for solutions online unless otherwise noted

#1: This code does not run!  Try it and examine the errors, then figure out what needs to
#be changed to make it work.  Do not create any, global variables, delete any existing
#code, or cut and paste existing code to new locations.

a = 10

def first_func(b=20):
    c = 30
    value = b+c+second_func()
    return value

def second_func(d=40):
    e = 50
    value = a + d + e
    return value

result = first_func()
print(result)

#2: Take this code from last week's lab and write functions so that the final
#execution looks like:
#answer = {key_func(k):val_func(v) for k, v in start_dict.items()}

from datetime import datetime
start_dict = {'noah': '2/23/1999',
              'sarah':'9/1/2001',
              'zach': '8/8/2005'}
#turn it into {'Noah': datetime.datetime(1999, 2, 23),
#              'Sarah': datetime.datetime(2001, 9, 1),
#              'Zach': datetime.datetime(2005, 8, 8)}

def date_transform(k, v):
    processed_k = k.capitalize()
    processed_v = datetime.strptime(v, '%m/%d/%Y').date()
    return processed_k, processed_v

answer = {date_transform(k, v)[0]: date_transform(k, v)[1] for k, v in start_dict.items()}
print(answer)


#3: A zscore is one term to describe data transformed to have mean zero and
#standard deviation one, given by: x - x_mean / x_std
#Write a function that takes any list-like object as a positional argument,
#then returns an object of the same dimensions with the zscores for the series.
#Use these two imported functions, and test your results on several lists of
#values
from numpy import mean, std

def zscore_function(my_list):
    x_mean = mean(my_list)
    x_std = std(my_list)
    processed_list = [(x - x_mean) / x_std for x in my_list]
    return processed_list

mylist = [1, 2, 3, 4, 5]
result = zscore_function(mylist)
print(result)

#4: A modified zscore uses the "median absolute deviation" to better handle
#outliers in the data, where the MAD is calculated by:
#  1. x - the median of the series
#  2. the absolute values of the results from 1
#  3. the median of the results from 2
#and finally, replace the standard deviation in the formula for the zscore from
#question 3 with the results from this process: x - x_mean / MAD
#
#Copy the function you created in 3 and create an optional key word argument that
#lets you override the default zscore calculation to instead use the modified
#version. This function should work in both question 3 and 4 without needing to
#change how you call it in part 3, because of its default behavior
from numpy import median, absolute

def MAD_calculate(my_list):
    group_median = median(my_list)
    group_mean = mean(my_list)
    individual_median = [absolute(x-group_median) for x in my_list]
    MAD = median(individual_median)
    processed_list = [(x - group_mean) / MAD for x in my_list]
    return processed_list

mylist = [1, 2, 3, 4, 5]
result = MAD_calculate(mylist)
print(result)

#
from numpy import mean, std, median, absolute

def zscore_function(my_list, modified=False):
    if modified:
        return MAD_calculate(my_list)
    else:
        x_mean = mean(my_list)
        x_std = std(my_list)
        processed_list = [(x - x_mean) / x_std for x in my_list]
        return processed_list

def MAD_calculate(my_list):
    group_median = median(my_list)
    group_mean = mean(my_list)
    individual_median = [absolute(x-group_median) for x in my_list]
    MAD = median(individual_median)
    processed_list = [(x - group_mean) / MAD for x in my_list]
    return processed_list

mylist = [1, 2, 3, 4, 5]

#default zscore calculation method
result1 = zscore_function(mylist)
print("Default zscore calculation:", result1)

#MAD zscore calculation method
result2 = zscore_function(mylist, modified=True)
print("Modified zscore calculation:", result2)

