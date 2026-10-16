daily_km = 50        # 每天飞多少
total_km = 0         # 账本：累计里程
day = 0              # 飞到第几天

while total_km<=500:        # 还没超过 500，就继续飞（注意是 超过）
    day = day + 1          # 天数 + 1
    total_km = daily_km + total_km      # 账本记一笔

print(f"第{day}天 累计{total_km}km")   # 第几天 + 累计多少公里，两个都要
