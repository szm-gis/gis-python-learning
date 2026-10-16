# # if条件判断:如果分数超过680 我就去清华读书
# scroe = 700
# if scroe > 680:
#     print("欢迎你来清华读书")
#     print("也恭喜你即将踏入精彩的大学生活")
# print("-------------------")

# 案例
# ok_account = "12345678"
# ok_password = "666666"
# account = input("请输入您的账号: ")
# password = input("请输入您的密码: ")
# if account == ok_account and password == ok_password:
#     print("登陆成功")
#     print("欢迎进入")
#
# if account != ok_account or password != ok_password:
#     print("登录失败")
#     print("请检查您的账号和密码")


# ok_account = "12345678"
# ok_password = "666666"
# account = input("请输入您的账号: ")
# password = input("请输入您的密码: ")
# if account == ok_account and password == ok_password:
#     print("登陆成功")
#     print("欢迎进入")
# else:
#     print("登录失败!")
#     print("账号或密码错误")

# #案例
# year = int(input("请输入需要判定的年份:"))
#
# if (year % 100 != 0 and year % 400 == 0) or (year % 400 == 0):
#     print(f"{year}是闰年")
# else:
#     print(f"{year}是平年")
#
# num = int(input("请输入需要判定的数字: "))
# if num % 2 == 0:
#     print("您输入的数字是偶数")
# else:
#     print("您输入的数字是奇数")
#
#
# age = input("请输入您的年龄: ")
# if int(age) <18:
#     print("您还是未成年人!")
# else:
#     print("您已经成年了")
#
# num = int(input("请输入一个数字:"))
# if num > 0:
#     print("您输入的是正数")
# elif num < 0:
#     print("您输入的是负数")
# else:
#     print("您输入的是0")
#
#
# account = input("请输入您的账户")
# password = input("请输入您的密码")
#
# a = int(input("请输入第一个边的边长: "))
# b = int(input("请输入第二个边的边长: "))
# c = int(input("请输入第三个边的边长: "))

#
# #pass 是空语句 起语法占位的作用
# if a + b > c and b + c > a and a + c > b:
#     if a == b and b == c:
#         print(f"{a} {b} {c} 这三个边长构成等边三角形 ~")
#     elif a == b or b == c or a == c:
#         print(f"{a} {b} {c} 这三个边长构成等腰三角形 ~")
#     else:
#         print(f"{a} {b} {c} 这三个边长构成普通三角形")
# else:
#     print(f"{a} {b} {c}这三个边长不能构成三角形 !!!")
#

# use = int(input("请输入您的用电量: "))
# if use < 2800:
#     money = use * 0.4883
#     print(f"您需要缴纳电费{money} 元 ")
# elif 2800 <= use <= 4800:
#     money = use * 0.5383
#     print(f"您需要缴纳电费{money} 元")
# else:
#     money = use * 0.7883
#     print(f"您需要缴纳电费{money} 元")