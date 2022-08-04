import re

def names():
    simple_string = """Amy is 5 years old, and her sister Mary is 2 years old. 
    Ruth and Peter, their parents, have 3 kids."""

    # YOUR CODE HERE
    print(simple_string)
    print(re.findall("[A-Z]\w+",simple_string))

names()
