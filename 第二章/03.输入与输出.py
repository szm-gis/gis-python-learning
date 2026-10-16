# #键盘上获取数据
# #键盘输入的类型均是字符串类型
# name = input("请输入你的姓名: ")
# age = input("请输入你的年龄: ")
#
# print(f"您的姓名是 {name} ,年龄为 {age}")



#案例 银行卡ATM机取款
# 总金额
total = 10000

# 1.输入密码
password = input("请输入您的银行卡密码: ")
print(f"密码正确 {password}")

# 2.输入取款金额
num = input("请输入您的取款金额: ")

# 3.计算余额并输出
print(f"取款后余额为:{total - int(num)}")
