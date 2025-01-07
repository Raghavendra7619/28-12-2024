a=[10,10,20]
for x in a:
    print(x,'-->',a.count(x))
    print(set[a.count(x for x in a)])

a=[10,10,20]
for x in set (a):
    print(x,'-->',a.count(x))
    print([a.count(x) for x in set(a)])


val='armani'
vowels='aeiou'
for x in val:
    if x in vowels:
        print(x)