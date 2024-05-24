def counter_add():
    def inner_func(num):
        return num + 5

    return inner_func


k = int(input())
cnt = counter_add()
print(cnt(k))
