# Yufei Liu, You Li, Zijing Zhao

#### fix the following errors!
#### do not use any web-based resources to figure them out

#1 done
x = 10
y = 20
print(x + y)

#2 done
my_list = [40, 50, 60, 70, 80, 100, 200, 400]
my_list_len = len(my_list)
print(my_list[my_list_len - 1])

#3 done
my_string = 'hello world'
print(my_string.upper())

#4 done
z = ['a', 'b', 'c']
z += 'd'

#5 run all these lines at once. why does the x not display 10, 
#followed by the 200?  Fix it so it does.(done)
x = 10
print(x)
y = 20
print(x * y)
# 

#6 done
color = 'My favorite color is %s, what is yours?' % blue
print(color)

#7 done
color = 'My favorite color is {}, what is yours?'.format("yellow")
print(color)

#8 done
color = f'My favorite color is {'red'}, what is yours?'
print(color)

#### answer the following questions by adding lines, but without changing the code given

#9 make the entries in this list unique (done)
schools = ['harris', 'booth', 'crown', 'harris', 'harris']
schools_unique = list(set(schools))
print(schools_unique)

#10 change the 'dog' entry to 'cat'
animals = tuple(['bird', 'horse', 'dog', 'fish'])

#11 separate the words in this string into entries in a list, with only lower-case
#letters, e.g. ['i', 'love', 'how', ...
my_sent = 'All that snow we had this winter sure was fun!'
