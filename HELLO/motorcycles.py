motorcycles = ['honda','yamaha','suzuki']
print(motorcycles)
motorcycles[0]='ducati'
print(motorcycles)
#列表末尾添加append
motorcycles.append('honda')
print(motorcycles)
#列表插入insert
motorcycles.insert(1,'bentian')
print(motorcycles)
#删除del
del motorcycles[0]
print(motorcycles)
del motorcycles[-1]
print(motorcycles)
#调用删除pop
popped_motorcyles = motorcycles.pop()
print(motorcycles)
print(popped_motorcyles)
motorcycles.insert(1,'www')
print(motorcycles)
fist_owend = motorcycles.pop(1)
print('The  '+fist_owend.upper()+'.')
#删除具体值
too_motorcycles = 'bentian'
motorcycles.remove(too_motorcycles)
print(motorcycles)
