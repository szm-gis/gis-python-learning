"""
    嵌套循环
    输入长M宽N的长方形

"""

#接受键盘录入

# m = int(input("请输入长方形的长度: "))
# n = int(input("请输入长方形的宽度: "))
#
# #print(*)自带换行效果
# for j in range(n):
#     for i in range(m):
#         print("*", end=" ")
#     print()

#
#
# # #打印99乘法表
# for i in range(1,10):
#     for j in range(1,i+1):
#         print(f"{j} x {i} = {i * j}",end="\t")
#     print()
#


# #案例1 根据输入的直角边的边长 打印等腰直角三角形
# i = int(input("请输入等腰直角三角形的边长: "))
# for i in range(1,i+1):
#     for j in range(1,i+1):
#         print("*",end="\t")
#     print("\t")


# 案例
#关键字 break 只能够出现在循环中 跳出循环
#关键字 continue 中断本次 继续下一次



while True:
    #1.接受输入用户名和密码
    username = input("请输入正确的用户名: ")
    password = input("请输入正确的密码: ")

    #2.校验是否为空
    if username == "" or password == "":
        print("输入的用户名或密码不能为空,请重新输入!")
        continue
    #3.判断是否为正确用户名和密码
    if username == "admin" and password == "888666":
        print("登陆成功")
        break
    elif username == "zhangsan" and password == "123456":
        print("登陆成功")
        break
    elif username == "xiaolan" and password == "0218":
        print("登陆成功")
        break
    else:
        print("登录失败")