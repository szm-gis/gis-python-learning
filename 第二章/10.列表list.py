# #列表名称 = [元素1,元素2,元素3,元素4,....] 列表的定义
# #下标         0    1     2    3
# #反向索引 -1 -2 -3 -4
# s = [1,2,95,213,"A","Hello"]
# print(type(s))
#
# #访问列表元素
# #获取
# print(s[0])
# print(s[-1])
#
# #修改
# s[5] = "abc"
# print(s)
#
# #删除
# del s[5]
# print(s)
#
# #循环遍历
# for item in s:
#     print(item)

#切片 包含开始 不包含结束索引 步长
# s = ["a","b","c","d","e","f","g","h","i","j"]
# print(s[0:5:1])


#列表的方法
#append() 在列表尾部加元素 s.append(10086)
#insert() 在指定索引之前加入元素 s.insert(0,92)
#remove() 移除第一个匹配到的元素 s.remove(72)
#pop() 删除指定位置元素 s.pop(2)
#sort 对列表进行排序(需数据类型一致) s.sort()
#reverse() 反转列表元素 s.reverse()


#案例
# num_list = []
# for i in range(10):
#     num = int(input("请输入一个有效的数字: "))
#     num_list.append(num)
# print("数字列表", num_list)
# num_list.sort()
# print("排列后的数字列表",num_list)
# print("最大值",num_list[-1])
# print("最小值",num_list[0])
# print("平均值",sum(num_list)/len(num_list))
# # #sum 求和 len 求个数 min 最小值 max最大值
#
#
# num_list2 = [i**2 for i in range(1,21)]
# print(num_list2)

num_list = [12,16,23,97,98,65,33,92,45,112,111]
new_list = [i**2 for i in num_list if i % 2 == 0]
print(new_list)