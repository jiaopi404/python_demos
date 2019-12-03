# demo print_line_demo
def print_line(num):
    print("*" * num)


def print_multi_lines(row_num, num):
    temp = 0
    while temp < row_num:
        print_line(num)
        temp = temp + 1


print_multi_lines(3, 10)
