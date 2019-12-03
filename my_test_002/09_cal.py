# demo cal


def cal(num1, num2, flag):
    if flag == "+":
        return num1 + num2
    elif flag == "-":
        return num1 - num2
    elif flag == "*":
        return num1 * num2
    elif flag == "/":
        try:
            temp = num1 / num2
        except ZeroDivisionError as e:
            temp = "exception occurred"
            print(e)

        return temp
    else:
        print("the calculator is bad")


print(cal(1, 2, "+"))
print(cal(1, 2, "-"))
print(cal(1, 2, "*"))
print(cal(1, 2, "/"))
