def survey_dream_destinations():  
    destinations = []  # 创建一个空列表来存储用户的梦想度假胜地  

    print("欢迎参加梦想度假胜地调查！")  
    
    while True:  
        destination = input("如果你可以去世界上的一个地方旅游，你会去哪里？（输入'结束'以结束调查）: ")  
        
        if destination.lower() == '结束':  
            break  # 如果用户输入'结束'，则退出循环  
        
        destinations.append(destination)  # 将用户输入添加到列表中  
        print(f"你输入的梦想度假胜地是: {destination}")  

    print("\n感谢你参加调查！你梦想的度假胜地有：")  
    for i, place in enumerate(destinations, start=1):  
        print(f"{i}. {place}")  # 打印出所有用户输入的度假胜地  

# 调用函数运行程序  
survey_dream_destinations()