# docs.python.org/3/library/functions.html#open
# 7:11:30 Harvard CS50’s Introduction to Programming with Python – Full University Course

name = input("What's your name? ")

file = open("names.txt", "a")
file.write(name)
file.close()