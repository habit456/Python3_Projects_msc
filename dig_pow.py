def dig_pow(n, p):
    num_list = list(map(lambda a: int(a), list(str(n))))
    pow_plus = 0

    for i, v in enumerate(num_list):
        pow_plus += (v ** (p + i))

    k = pow_plus / n

    if k % 1.0 == 0.0:
        return int(k)
    else:
        return -1


print(dig_pow(46288, 3))
