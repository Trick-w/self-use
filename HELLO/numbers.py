nums = [numss for numss in range(1,21)]
print (nums)

numbers = []
for number in range(1,1000001):
    numbers.append(number)
print(min(numbers))
print(max(numbers))
print(sum(numbers))

jishus = [jishu for jishu in range(1,21,2)]
print(jishus)

beishu_3 = list(range(3,30,3))
for beishu in beishu_3:
    print(beishu)

lifangs = [lifang**3 for lifang in range(1,11)]
for lifff in lifangs:
    print(lifff)

lifs = list(lift**3 for lift in range(1,11))
print(lifs)
