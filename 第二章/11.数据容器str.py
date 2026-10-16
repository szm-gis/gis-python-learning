# 字符串 基本操作 -->字符串不可修改
# s = "Hello-Python"
#
# print(s[4])
# print(s[-8])
#
# for i in s:
#     print(i)
#
#
# #切片
# print(s[0:5:1])
# print(s[:5:1])
# print(s[:5])
#
# # print(s[6::1])
# print(s[6:])

#常用方法
"""
find()查找第一次的位置 count()统计次数 upper()大写 lower()小写 slist()切割 strip()去除字符串两端的空白字符或指定字符
replace()替换 startswith()/endswith 检查字符串 返回布尔值
"""

#案例
# mail = input("请输入您的邮箱: ")
# if mail.count("@") == 1 and mail.count(".") >= 1:
#     print(f"mail是合法的邮箱")
# else:
#     print(f"mail是非法的邮箱")
# #方法二
mail = input("请输入您的邮箱: ")
if mail.count("@") == 1 and "." in mail:
    print(f"mail是合法的邮箱")
else:
    print(f"mail是非法的邮箱")
#in运算符
