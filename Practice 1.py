list1 = [1, 2, 3, 4, 5, 6, 7]
dict1 = {}
for x in list1:
    if x % 2 != 0:
        dict1[x] = x**3
print(dict1)

list2 = [1, 2, 3, 4, 4, 5, 6, 6, 6, 7, 7]
set2 = set()
for x in list2:
    if x % 2 == 0:
        set2.add(x)
print(set2)

list3 = list(range(0, 100, 10))
list3 = []
for x in list3:
    if x != 0:
        list3.append(x)
print(list3)