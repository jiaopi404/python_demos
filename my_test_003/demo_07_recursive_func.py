# demo func: recursive


def recursive_func(num):
    if num == 1:
        return 1
    else:
        temp = recursive_func(num - 1)
        return num + temp


result_sum = recursive_func(22)

print('1 + 2 + 3 + ... + %s = %s' % (22, result_sum))


def sum_numbers(num):
    if num == 1:
        return 1

    # 假设 sum_numbers 能够完成 num - 1 的累加
    temp = sum_numbers(num - 1)

    # 函数内部的核心算法就是 两个数字的相加
    return num + temp


print(sum_numbers(2))
