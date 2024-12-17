def make_album(artist_name, album_title, song_count=None):  
    """创建描述音乐专辑的字典"""  
    album = {  
        'artist': artist_name,  
        'title': album_title,  
    }  
    if song_count is not None:  
        album['song_count'] = song_count  
    return album  

# 创建三个不同专辑的字典  
album1 = make_album('Taylor Swift', '1989', 13)  
album2 = make_album('Adele', '25')  
album3 = make_album('Ed Sheeran', 'Divide', 12)  

# 打印每个返回的值  
print(album1)  
print(album2)  
print(album3)  

# 用户输入专辑信息  
while True:  
    print("\n请输入专辑的歌手和名称（或输入 'q' 退出）：")  
    
    artist_name = input("歌手姓名: ")  
    if artist_name.lower() == 'q':  
        break  
    
    album_title = input("专辑名称: ")  
    if album_title.lower() == 'q':  
        break  
    
    song_count_input = input("专辑歌曲数量（可选，直接按回车跳过）: ")  
    song_count = int(song_count_input) if song_count_input.isdigit() else None  
    
    # 使用输入的信息调用函数  
    new_album = make_album(artist_name, album_title, song_count)  
    
    # 打印创建的专辑字典  
    print("\n您创建的专辑信息:")  
    print(new_album)  

print("感谢您的参与！")  