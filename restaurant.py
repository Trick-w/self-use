class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"餐馆名称: {self.restaurant_name}")
        print(f"菜系类型: {self.cuisine_type}")

    def open_restaurant(self):
        print(f"{self.restaurant_name} 正在营业")

# 创建 restaurant 实例
restaurant = Restaurant("美味餐厅", "中餐")
print(restaurant.restaurant_name)
print(restaurant.cuisine_type)
restaurant.describe_restaurant()
restaurant.open_restaurant()

# 创建三个 restaurant 实例
restaurant1 = Restaurant("川菜馆", "川菜")
restaurant2 = Restaurant("粤菜馆", "粤菜")
restaurant3 = Restaurant("湘菜馆", "湘菜")

restaurant1.describe_restaurant()
restaurant2.describe_restaurant()
restaurant3.describe_restaurant()
