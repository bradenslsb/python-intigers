
sentence = 'The quick brown fox jumped over the lazy dog.'

sentence = sentence.replace('quick', 'slow')

print(sentence.replace('quick', 'slow'))
print(sentence)


url = "   https://google.com    "
url2 = "https://google.com"
url3 = "https://google.com"
url4 = "https://google.com"
url5 = "https://google.com"

print(url.strip())
print(url2.strip("https://")) #this will mess with the security.
print(url3.lstrip("https://"))
print(url4.rstrip(".com"))
print(url5.strip("https://" ".com").capitalize())


heading = "Python: An Introduction"

header, _, subheader = heading.partition(": ")

print(header)
print(subheader)

heading2 = "Python: An Introduction, and Python: Advanced"

header2, _, subheader2 = heading2.partition(": ")

print(header2)
print(subheader2)


tags = "python, coding, programming, development"

list_of_tags = tags.split(",") #meaning its going to remove that item and put the rest in a list.

print(list_of_tags)

list_of_tags = tags.split() #puts every element in the list.

print(list_of_tags)


heading = "Python: An Introduction"

heading_list = heading.split(": ")

print(heading_list)

heading2 = "Python: An Introduction, and Python: Advanced"

heading_list_2 = heading2.split(": ")

print(heading_list_2)


api_data = "5"
greeting = "hi there" 
greeting2 = "hithere"

print(api_data.isalpha()) #if its the alphabet
print(greeting.isalpha()) #doesn't count spaces
print(greeting2.isalpha())

print(api_data.isnumeric()) #if its a number
print(greeting.isnumeric())

from functools import reduce

def expontent (num, num_two):
    li = [num] * num_two
    return reduce((lambda x, y: x * y), li)

print(expontent(10, 2))

users = ["Kristine", "Tiffany", "Jordan"]

print(users)

users.insert(0, "Anthony")

print(users)

users.append("Ian")

print(users)

tags = ['python', 'development', 'tutorials', 'code']

number_of_tags = len(tags)
last_item = tags[-1]
index_of_last_item = tags.index(last_item)

print(number_of_tags)
print(last_item)
print(index_of_last_item)

tags2 = [
  'python',
  'development',
  'tutorials',
  'code',
  'programming',
  'computer science'
]

tag_range = tags2[1:-1:2]
tag_range = tags2[::-1]

print(tag_range)

tags2.sort(reverse=True)

print(tags2)


sale_prices = [
  100,
  83,
  220,
  40,
  100,
  400,
  10,
  1
  
]

sale_price_list = len(sale_prices) 
sale_prices.sort() 
  
if sale_price_list % 2 == 0: 
    median1 = sale_prices[sale_price_list//2] 
    median2 = sale_prices[sale_price_list//2 - 1] 
    median = (median1 + median2)/2
else: 
    median = sale_prices[sale_price_list//2] 
print(median) 