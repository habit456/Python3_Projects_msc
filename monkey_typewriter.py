import random


def monkey_typewriter(goal):
    alphabet = 'abcdefghijklmnopqrstuvwxyz '
    sentence = ''
    count = 0
    while sentence != goal:
        sentence = ''
        count += 1
        for i in range(len(goal)):
            sentence += alphabet[random.randrange(27)]
    print('sentence: ', sentence)
    print('count: ', count)


print(monkey_typewriter('z'))
