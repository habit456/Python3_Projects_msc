def dont_give_me_five(start, end):
    """finds the length of a range of values from start to end,
    excluding any number that contains 5 in it (like 151)"""
    my_list = [a for a in range(start, end + 1)]
    result = []
    for n in my_list:
        if list(str(n)).count('5') == 0:
            result.append(n)
    return len(result)


print(dont_give_me_five(1, 50))


def dont_give_me_five_improved(start, end):
    """in can be used on strings"""
    return len([a for a in range(start, end + 1) if '5' not in str(a)])


print(dont_give_me_five_improved(1, 50))