def counter_add(n):
    def inner_calc(num):
        return num + n
    return inner_calc


k = int(input())
cnt = counter_add(2)
print(cnt(k))
