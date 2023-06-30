a = [21, 8]
p = 2
ind = 0
pro = []# простые числа
for i in range(43):
    if a[i] % 2 == 0:
        d = a[i] - 1
        a.append(d)
    else:
        d = a[i] + 21
        a.append(d)
#print(a)
#print(len(a))
#у нас готов массив со всеми элементами. Теперь ищем простые числа
for i in range(45):
    while a[ind] % p != 0:
        p += 1
    if p == a[ind]:
        pro.append(a[ind])
    p = 2
    ind += 1
print(pro)
