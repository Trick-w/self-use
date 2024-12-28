class User():
    """模拟用户信息"""
    def __init__(self, first_name, last_name, email, password,login_attempts=0):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = password
        self.login_attempts = login_attempts
    """重置登录次数"""
    def increment_login_attempts(self):
        self.login_attempts += 1
    def reset_login_attempts(self):
        self.login_attempts = 0
    """描述用户信息"""
    def describe_user(self):
        print(f"First Name: {self.first_name}")
        print(f"Last Name: {self.last_name}")
        print(f"Email: {self.email}")
        print(f"Password: {self.password}")
        print(f"Login Attempts: {self.login_attempts}")
    """问候用户"""
    def greet_user(self):
        print(f"Hello, {self.first_name} {self.last_name}!")

# 创建 user 实例
user = User('John', 'Doe', '1255213','343331',3)
user.increment_login_attempts()
user.increment_login_attempts()
user.increment_login_attempts()
user.describe_user()
user.greet_user()
user.reset_login_attempts()
user.describe_user()
user.greet_user()
