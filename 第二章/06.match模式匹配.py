# match case 模式匹配   case_指其他所有情况
# day = input("请输入星期几(1-7)")
#
# match day:
#     case "1":
#         print("周一:工作会议日")
#     case "2":
#         print("周二:学习培训日")
#     case "3":
#         print("周三:项目开发日")
#     case "4":
#         print("周四:代码审查日")
#     case "5":
#         print("周五:总结规划日")
#     case "6" | "7":
#         print("休息日")

num1 = float(input("请输入第一个数"))
num2 = float(input("请输入第二个数"))
oper = input("请输入运算符(+ - * /): ")

match oper:
    case "+":
        print(f"{num1} + {num2} = {num1 + num2}")
    case "-":
        print(f"{num1} - {num2} = {num1 - num2}")
    case "*":
        print(f"{num1} * {num2} = {num1 * num2}")
    case "/" if num2 != 0:
        print(f"{num1} / {num2} = {num1 / num2}")
    case _:
        print("操作不支持!!!")