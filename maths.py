import random as r


def maths():
    x = r.randint(0, 1000)
    y = r.randint(0, 1000)
    answer = x * y
    question = input("What is %d * %d?" % (x, y))
    if question == str(answer):
        print("Correct!")
    else:
        print("Incorrect!")
    again = input("Again? 1/Y, 2/N.")
    if again == "1":
        maths()


maths()
