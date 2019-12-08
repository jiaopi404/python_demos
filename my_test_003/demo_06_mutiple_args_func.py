# demo multiple args func


def func(num, *args, **kwargs):
    print(num, args, kwargs)


func(1, 2, 3, 4, 5, 6, 'ssdf', 'note', ['hello'], {'name': 'cyk', 'gender': True})
