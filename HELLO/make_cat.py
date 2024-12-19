def make_cat(maker,mise,**abtions):
    """创造一个字典，包含制作汽车的一切详细信息"""
    make_cat_x = {}
    make_cat_x['maker'] = maker
    make_cat_x['mise'] = mise
    for key,value in abtions.items():
        make_cat_x[key] = value
    return make_cat_x
car = make_cat('subaru', 'outback', color='blue', tow_package=True)
print(car)