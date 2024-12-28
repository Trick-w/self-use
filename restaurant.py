class Restaurant:
    def __init__(self, restaurant_name, cuisine_type, number_served=0):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = number_served

    def set_number_served(self, number_served):
        self.number_served = number_served
    
    def increment_number_served(self, number_served):
        self.number_served += number_served

    def describe_restaurant(self):
        print(f"餐馆名称: {self.restaurant_name}")
        print(f"菜系类型: {self.cuisine_type}")
        print(f"就餐人数: {self.number_served}")
        
    def open_restaurant(self):
        print(f"{self.restaurant_name} 正在营业")

# 创建 restaurant 实例
restaurant = Restaurant("美味餐厅", "中餐")
print(restaurant.restaurant_name)
print(restaurant.cuisine_type)
restaurant.describe_restaurant()
restaurant.open_restaurant()

# 创建三个 restaurant 实例
restaurant1 = Restaurant("川菜馆", "川菜","13")

restaurant1.number_served = 10
restaurant1.increment_number_served(10)
restaurant1.increment_number_served(10)
restaurant1.describe_restaurant()
