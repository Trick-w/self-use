#永久排序 正排序sort 逆排序sort(reverse=True)
cars = ['bmw', 'audi', 'toyota', 'subaru'] 
cars.sort()
print(cars)
cars = ['bmw', 'audi', 'toyota', 'subaru'] 
cars.sort(reverse=True)
print(cars)
#临时排序 正sorted 逆向函数sorted()传递参数reverse=True。
cars = ['bmw', 'audi', 'toyota', 'subaru']
print("Here is the original list:") 
print(cars) 
print("\nHere is the sorted list:") 
print(sorted(cars)) 
print("\nHere is the original list again:") 
print(cars)
print(sorted(cars,reverse=True))
#倒着打印列表
cars = ['bmw', 'audi', 'toyota', 'subaru'] 
print(cars) 
cars.reverse() 
print(cars)
#列表长度
cars = ['bmw', 'audi', 'toyota', 'subaru']
len(cars)