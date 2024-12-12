sandwich_orders = ['jirou','niurou','gourou','gourou','gourou','gourou','zhurou']
finished_sandwiches = []
print(f"gourou maiwanle.")
while 'gourou' in sandwich_orders:
    sandwich_orders.remove('gourou')
while sandwich_orders:
    finished_sandwiche = sandwich_orders.pop()
    print(f"\nI made your {finished_sandwiche} sandwich.")
    finished_sandwiches.append(finished_sandwiche)
print(finished_sandwiches)