my_pizzas = ['s','w','c','e','k']
friend_pizzas = my_pizzas[:]

my_pizzas.append('r')
friend_pizzas.append('l')

print('My favorite pizzas are:')
for my_pizza in my_pizzas:
    print(list(my_pizza))

print('My friend’s favorite pizzas are:')
for friend_pizza in friend_pizzas:
    print(friend_pizza)

my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]
my_foods.append('cannoli') 
friend_foods.append('ice cream') 
print("My favorite foods are:")
print(my_foods) 
for my_food in my_foods:
    print(my_food)
print("\nMy friend's favorite foods are:")
print(friend_foods)
print(list(friend_food for friend_food in friend_foods))