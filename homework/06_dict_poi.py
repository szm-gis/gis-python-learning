dh_pois = [
    {"name":"德化火车站","lon":118.24,"lat":25.29},
    {"name":"德化一中","lon":118.22,"lat":25.31},
    {"name":"石牛山","lon":118.25,"lat":25.33},
           ]
for p in dh_pois:
    print(f"名称{p['name']},经度{p['lon']},纬度{p['lat']}")
names = [p["name"] for p in dh_pois]
print(names)
print(p['type'])
