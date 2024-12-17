def show_magicians(magicians):
    for magician in magicians:
        print(magician)

def make_great(magicians):
    great_magicians = []  
    for magician in magicians:  
        great_magicians.append(f"{magician} the Great")  
    return great_magicians

magicians = ['David Copperfield', 'Harry Houdini', 'Penn & Teller', 'David Blaine']

# 打印原始魔术师名字  
print("原始魔术师名单:")  
show_magicians(magicians)  

# 创建包含“the Great”的新魔术师名单  
great_magicians = make_great(magicians)  

# 打印修改后的魔术师名字  
print("\n修改后的魔术师名单:")  
show_magicians(great_magicians)

# 确认原始魔术师名单是否未被修改  
print("\n验证原始魔术师名单:")  
show_magicians(magicians)