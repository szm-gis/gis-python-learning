#不确定循环次数用while

import random
random_num = random.randint(1,100)

while True:
    num = int(input("请输入一个数字: "))
    if num > random_num:
        print("大了!")
    elif num < random_num:
        print("小了")
    else:
        print("炸了!")
        break

print("随机生成的数字是",random_num)