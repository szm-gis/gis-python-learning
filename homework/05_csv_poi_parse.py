#原始csv数据
line = "德化一中,118.22,25.31,中学"
#拆分line 需要用一个东西接住
parts = line.split(",")
print(parts)
#取出
name = parts[0]
lon = parts[1]
lat = parts[2]
lei = parts[3]
print(f"名称{name},经度{lon},纬度{lat}")

#转出小数也要用东西接住
lon = float(lon)
lat = float(lat)
print(lon+lat)