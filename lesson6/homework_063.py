lst1 = ['1', '2', 3, True, 'False', 5, '6', 7, 8, 'Python', 9, 0, 'Lorem Ipsum']
lst2 = []

# lst2 = [x for x in lst1 if type(x) == str] # alternative solution

for x in lst1:
    if type(x) == str:
        lst2.append(x)

print(lst2)
