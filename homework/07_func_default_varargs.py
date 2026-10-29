# #1
#
# def format_coord(lon, lat, unit="度"):   #定义函数
#     return f"{lon:.4f}{unit}, {lat:.4f}{unit}"  #返回字符串
# print(format_coord(118.235234,25.492966))    #调用函数
# print(format_coord(118.235234,25.492966,"°"))

#2

def count_pois(*names):
    if names:
        for i, name in enumerate(names):
            print(f"第{i + 1}个:{name}")
        print(f"一共{len(names)}个POI")
    if not names:
        print("没有传入POI")
count_pois("德化一中", "德化二中", "德化三中", "德化八中","德化职校")
count_pois()
count_pois("德化九仙山")
