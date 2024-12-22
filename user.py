class User():
    def __init__(self, first_name, last_name, email, password):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = password

    def describe_user(self):
        print(f"First Name: {self.first_name}")
        print(f"Last Name: {self.last_name}")
        print(f"Email: {self.email}")
        print(f"Password: {self.password}")

    def greet_user(self):
        print(f"Hello, {self.first_name} {self.last_name}!")

# 创建 user 实例
user = User('John', 'Doe', '1255213','343331')
user.describe_user()
user.greet_user()
