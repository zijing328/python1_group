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
#followed by the 200?  Fix it so it does. (done)
x = 10
print(x)
y = 20
print(x * y)
# 

#6 done
color_name = 'blue'
color_string = f'My favorite color is {color_name}, what is yours?' 
print(color_string)

#7 done
color = 'My favorite color is {}, what is yours?'.format('yellow')
print(color)

#8 done
color = 'red'
my_string_color = f'My favorite color is {color}, what is yours?'
print(my_string_color)

#### answer the following questions by adding lines, but without changing the code given

#9 done 
# make the entries in this list unique
schools = {'harris', 'booth', 'crown', 'harris', 'harris'}
print(schools)


#10 change the 'dog' entry to 'cat' (done)
animals = tuple(['bird', 'horse', 'dog', 'fish'])
animals_edit = list(animals)
animals_edit[2] = 'cat'
animals = tuple(animals_edit)
print(animals)

#11 separate the words in this string into entries in a list, with only lower-case
#letters, e.g. ['i', 'love', 'how', ... done
my_sent = 'All that snow we had this winter sure was fun!'
word_list = my_sent.lower().split()
print(word_list)
