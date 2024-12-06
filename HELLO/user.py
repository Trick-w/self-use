#current_users = ['aDmin','Baobo','jhon','hellen','even']
#new_users = ['Admin','baobo','jhosdn','helllen','ellen']
#for user in new_users:
#    if user.lower() in [current_user.lower() for current_user in current_users]:
#        print('\n请重新输入.')
#    else:
#        print('\n未注册使用.')

nums = range(1,10)
for num in nums:
    if num == 1:
        print('\n'+str(num)+'st')
    elif num == 2:
        print('\n'+str(num)+'nd')
    elif num == 3:
        print('\n'+str(num)+'rd')
    else:
        print('\n'+str(num)+'th')