#常见数据类型---->type()用于获取指定的字面量或变量的类型
# print(type("Hello"))
#
# print(type(10))
# print(type(3.14))
# print(type(True))
# print(type(False))
# print(type(None))
#
# num = -100
# print(type(num))
#
# #isinstance(数据,类型) 检查数据是否属于指定的类型-->bool值---->是True,否则False
# print(isinstance(num,int))
# print(isinstance(num,float))
# print(isinstance(num,bool))



# #字符串
# # 定义字符串的三种方式
# s1 = "Hello"#双引号定义
# s2 = 'Python'#单引号定义
# s3 = """
# Hello:
#     欢迎大家进入python学习!
# """ #三引号定义的字符串(多行字符串)
#
# print(s1)
# print(s2)
# print(s3)
#
# print(isinstance(s1, str))
# print(isinstance(s2, str))
# print(isinstance(s3, str))
#
# # 定义字符串---->It's very good
# #转义字符\'(单引号) \"(双引号) \n(换行符) \t(相当于tab缩进)
# msg = 'It\'s very good'
# print(msg)
#
# msg2 = "Hello 的意思就是\"您好\""
# print(msg2)
#
#
# print("\t欢迎大家进入课程!\n\t记得一键三连")



# #字符串拼接
# s1 = "人生苦短" "我用python" ",OK"
# print(s1)
#
# msg1 = "人生苦短"
# msg2 = "我用python"
# print("龟叔说:" + msg1 + "," + msg2)
#
# #案例  ---->str(int数字)----将int类型转为字符串; +号只能拼接字符串与字符串
# name = "A"
# age = 20
# pro = "地理信息科学"
# hobby = "Python,打cs"
# print("大家好,我是" + name + ",今年" + str(age) +  "岁,学习的专业是" + pro + ",爱好" + hobby)


# 字符串格式化------>占位符---->%s(会将数据自动转化为字符串)
# name = "A"
# age = 20
# pro = "地理信息科学"
# hobby = "Python,打cs"
# print("大家好,我是%s,今年%s岁,学习的专业是%s,爱好%s"%(name,age,pro,hobby))

#字符串格式化---->f"内容{变式/表达式}"
name = "A"
age = 20
pro = "地理信息科学"
hobby = "Python,打cs"
print(f"大家好,我是{name},今年{age}岁,学习的专业是{pro},爱好{hobby}")#(企业推荐)

