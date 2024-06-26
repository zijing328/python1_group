#You Li
#Unless otherwise noted, try solving these using class content and without searching online

#1
#Modify this code so that when i is 5 it doesn't print anything (including Finished!)
#and instead moves directly onto 6, while leaving it unchanged for other values of i
i = 0
while i < 10:
    if i < 5:
        print('little')
    elif i == 5:
        i += 1
        continue
    elif i > 5:
        print('big')
    else:
        print('what happened?')
    
    if i != 5:
        print('Finished!')
    i += 1
        
        
    
#2
#Write a for loop that prints this pattern:
#HINT: you can write a for-loop inside of a for-loop

#1
#1 2
#1 2 3
#1 2 3 4

for i in range(1,5):
    for n in range(1,i+1):
        print(n, end = ' ')
    print()

#3
start_list = [[2, 3, 4], [6, 8, 9]]
#turn it into [1,    2,   3, 4   ]  
#NOTE:  The spacing is just to show which numbers are converted to which
#HINTS: There are three steps here: mapping, filtering, and flattening the nested lists
#       Try doing this in a for-loop, then try doing it in a list comprehension
#       You may need to check StackOverflow for how to flatten a nested list
start_list1 = start_list[0]
start_list2 = start_list[1]

mapped1 = [i for i in start_list1]
mapped2 = [n for n in start_list2]

filtered1 = [l//2 for l in start_list1 if l % 2 == 0]
filtered2 = [l//2 for l in start_list2 if l % 2 == 0]

my_list = []

my_list.extend(filtered1)
my_list.extend(filtered2)

print(my_list)

#4
import datetime
start_dict = {'noah': '2/23/1999',
              'sarah':'9/1/2001',
              'zach': '8/8/2005'}
#turn it into {'Noah': datetime.datetime(1999, 2, 23),
#              'Sarah': datetime.datetime(2001, 9, 1),
#              'Zach': datetime.datetime(2005, 8, 8)}
#HINTS: The datetime library has a function that turns strings of the right format into dates
#       Again, start with a for-loop, but make a dictionary comprehension in the end

end_dict = {}
for key, val in start_dict.items():
    date_obj = datetime.datetime.strptime(val, '%m/%d/%Y').date()
    end_dict[key.capitalize()] = date_obj
print(end_dict)
