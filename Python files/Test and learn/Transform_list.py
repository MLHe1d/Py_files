list_1 = list()
while True: 
    add_num = input('введи число')
    if add_num == 'stop':
        break
    list_1.append(add_num)


turple_1 = [list_1]; print ('Кортеж ', turple_1)
set_1 = set(list_1); print ('Множество ', set_1)
x = len(list_1)



dic_keys = list()

for i in range (0, x):
    
    dic_keys.append(i)


dict_1 =  dict(zip(list_1, dic_keys)); print('Cловарь ', dict_1)    