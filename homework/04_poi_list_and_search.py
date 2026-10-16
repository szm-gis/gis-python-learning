# #德化常用POI名称列表
# dh_pois = ["德化火车站","德化一中","石牛山","万达广场","县医院","嘉德新苑","德化八中","德化二中","德化三中","德化六中"]
#
# print("第三个POI是", dh_pois[2])# 下标从0 开始第三个是2
# print("最后一个POI是", dh_pois[-1])#-1表示倒数第一个
# print(f"一共有{len(dh_pois)}个POI") #len()数个数 f-string拼接

# dh_pois = [
#     ["德化火车站", 118.24, 25.29],
#     ["德化一中",   118.22, 25.31],
#     ["石牛山",     118.25, 25.33],
# ]
# for p in dh_pois:
#     #p是小列表 p[0]是名字 p[1]是经度 p[2]是纬度
#     print("名称",p[0],"经度",p[1],"纬度",p[2])

#建立一个空列表
# result = []
# #加入超市 用append
# result.append("大超市")
# print("第一次加入",result)
# result.append("中超市")
# print("第二次加入",result)
# result.append("中超市")
# print("第三次加入",result)
# #删除
# result.remove("中超市")
# for p in result:
#     print(p)


dh_pois = [
    ["德化火车站", 118.24, 25.29],
    ["德化一中",   118.22, 25.31],
    ["石牛山",     118.25, 25.33],
]
# # 排序
# dh_pois.sort(key=lambda p: p[2], reverse=True)
# print(dh_pois)
from operator import itemgetter

# 按纬度(p[2])从高到低排序
dh_pois.sort(key=itemgetter(2), reverse=True)

# 打印排序后的结果
print(dh_pois)

#筛选
new_pois = [p for p in dh_pois if p[1]>118.23]
print(new_pois)

# 删除
name = input("请输入你要删除的名字: ")
for p in dh_pois:
    if p[0] == name:
        dh_pois.remove(p)
        print("已删除",name)
        break
else:
    print("请输入正确的名字")


