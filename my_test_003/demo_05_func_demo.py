# func demo


def sort_list(var_list, reverse_flag):
    if reverse_flag:
        var_list.sort(reverse=True)
    else:
        var_list.sort()

    return var_list


my_list = [2, 4, 1, 5, 8]

print(sort_list(my_list, True))


def stu_info(stu_name, gender=False):
    gender_info = 'boy' if not gender else 'girl'
    stu = {'stu_name': stu_name, 'gender_info': gender_info}
    return stu


print(stu_info('cyk'))



