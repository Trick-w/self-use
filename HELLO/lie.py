class Restaurant:  
    def __init__(self, restaurant_name, cuisine_type):  
        self.restaurant_name = restaurant_name  
        self.cuisine_type = cuisine_type  

    def describe_restaurant(self):  
        print(f"Restaurant Name: {self.restaurant_name}")  
        print(f"Cuisine Type: {self.cuisine_type}")  

    def open_restaurant(self):  
        print(f"{self.restaurant_name} is now open!")  

# 创建一个名为 restaurant 的实例  
restaurant = Restaurant("The Great Eatery", "Italian")  

# 打印属性  
print(restaurant.restaurant_name)  
print(restaurant.cuisine_type)  

# 调用方法  
restaurant.describe_restaurant()  
restaurant.open_restaurant()  

# 创建三个餐馆实例  
restaurant1 = Restaurant("Food Paradise", "Asian")  
restaurant2 = Restaurant("Spicy Town", "Indian")  
restaurant3 = Restaurant("Sushi World", "Japanese")  

# 调用 describe_restaurant() 方法  
restaurant1.describe_restaurant()  
restaurant2.describe_restaurant()  
restaurant3.describe_restaurant()  