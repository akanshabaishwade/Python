def hello():
    print("function1")
    print("function2")
    print("function3")
fun = hello(), "function"

def login():
    Name = input("enter your name in funciton: ")
    Class = input("enter your class in funciton: ")
    school = input("enter your school in funciton: ")
    pin = input("enter your pin in funciton: ")

login()

def hello(name):
    print('Hello ' + name)

hello('anshu')


import random


def getanswer(answerNumber):
    if answerNumber == 1:
        return "am red"
    elif answerNumber == 2:
        return "am black"
    elif answerNumber == 3:
        return "am green"
    elif answerNumber == 4:
        return "reply busy try again"
    elif answerNumber == 5:
        return "ask again later"


r = random.randint(1, 5)
fortune = getanswer(r)
print(fortune)

# same
print(getanswer(random.randint(1, 5)))
