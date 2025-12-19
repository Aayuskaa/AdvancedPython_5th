# Variables and Input

# 1. Create a variable my_age and print it
my_age = 20   
print("My age:", my_age)

''' output:
 My age: 20  '''

# 2. Ask user for favorite food and print a message
favorite_food = input("Enter your favorite food: ")
print("Your favorite food is", favorite_food)

''' output: 
Enter your favorite food: pizza
Your favorite food is pizza'''

# Type Conversion

# 1. Convert string "42" to integer
num_str = "42"
num_int = int(num_str)   # converting string to integer
print("Converted integer:", num_int)

''' output:
Converted integer: 42  '''

# 2. Convert float 3.14159 to string
pi = 3.14159
pi_str = str(pi)   # converting float to string
print("Converted string:", pi_str)

''' output:
Converted string: 3.14159  '''

# Strings

# 1. Concatenate two strings
concat = "Hello" + " " + "World!"
print(concat)

''' output:
Hello World! '''

# 2. Extract the third character from "Python"
word = "Python"
third_char = word[2]   # index starts from 0
print("Third character:", third_char)

''' output:
Third character: t  '''

# 3. Take a sentence and print first five words
sentence = input("Enter a sentence: ")
words = sentence.split()   # split sentence into words
print("First five words:", " ".join(words[:5]))

''' output: 
 Enter a sentence: Hi I am Aayuska Bhandari and studying at hcoe
First five words: Hi I am Aayuska Bhandari '''