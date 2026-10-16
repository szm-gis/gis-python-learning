# #纬度 lat，经度 lon（或 lng），一个字母都不能错。
#
# for i in range(0,11):
#
#     lat = 24 + i * 0.1
#     print(f"纬度{lat}")

for i in range(11):
    lat = 24 + i * 0.1          # lat，不是 let
    print(f"纬度 {lat:.1f}°N")   # :.1f = 保留1位小数，误差被强制抹掉