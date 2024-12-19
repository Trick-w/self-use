class User:  
    def __init__(self, first_name, last_name, age, location):  
        self.first_name = first_name  
        self.last_name = last_name  
        self.age = age  
        self.location = location  

    def describe_user(self):  
        print(f"User Name: {self.first_name} {self.last_name}")  
        print(f"Age: {self.age}")  
        print(f"Location: {self.location}")  

    def greet_user(self):  
        print(f"Hello, {self.first_name}! Welcome back!")  

# 创建多个表示不同用户的实例  
user1 = User("Alice", "Smith", 30, "New York")  
user2 = User("Bob", "Johnson", 25, "Los Angeles")  
user3 = User("Charlie", "Brown", 35, "Chicago")  

# 调用方法  
user1.describe_user()  
user1.greet_user()  

user2.describe_user()  
user2.greet_user()  

user3.describe_user()  
user3.greet_user()  