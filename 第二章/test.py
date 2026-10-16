from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt
import os

# 设置中文字体
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

# Win7区域坐标范围
WIN7_LON_MIN = -77
WIN7_LON_MAX = -54
WIN7_LAT_MIN = -56
WIN7_LAT_MAX = -35

# SHP文件夹所在目录
SHP_BASE_DIR = r"D:\data"

# 12个月对应的文件夹关键字
months = {
    1: "A2024001",
    2: "A2024032",
    3: "A2024061",
    4: "A2024092",
    5: "A2024122",
    6: "A2024153",
    7: "A2024183",
    8: "A2024214",
    9: "A2024245",
    10: "A2024275",
    11: "A2024306",
    12: "A2024336",
}


# 画图函数
def plot_burn(month_num, shp_dir):
    # 自动找文件夹里的shp文件
    shp_path = None
    for f in os.listdir(shp_dir):
        if f.endswith('.shp'):
            shp_path = os.path.join(shp_dir, f.replace('.shp', ''))
            break

    if shp_path is None:
        print(f"未找到{month_num}月的shp文件")
        return

    # 创建地图
    fig = plt.figure(figsize=(8, 10))
    m = Basemap(
        projection='merc',
        llcrnrlon=WIN7_LON_MIN,
        llcrnrlat=WIN7_LAT_MIN,
        urcrnrlon=WIN7_LON_MAX,
        urcrnrlat=WIN7_LAT_MAX,
        resolution='i'
    )

    # 绘制陆地和国界
    m.drawcoastlines(linewidth=0.5)
    m.drawcountries(linewidth=0.5)
    m.fillcontinents(color='#f0f0f0', lake_color='white')

    # 读取并绘制shapefile
    m.readshapefile(shp_path, 'burn_date', color='red', linewidth=2, zorder=10)

    # 添加图题
    plt.title(f'2024年{month_num}月 Win7区域燃烧迹地分布图', fontsize=14, pad=20)

    # 添加指北针
    plt.annotate('N', xy=(0.95, 0.95), xycoords='axes fraction',
                 ha='center', va='center', fontsize=12,
                 bbox=dict(boxstyle='circle', fc='white', ec='black'))

    # 添加比例尺
    m.drawmapscale(
        WIN7_LON_MIN + 2, WIN7_LAT_MIN + 2,
        WIN7_LON_MIN, WIN7_LAT_MIN,
        200, barstyle='fancy', labelstyle='simple',
        units='km', fontsize=8
    )

    # 添加图例说明
    plt.text(0.02, 0.02, '燃烧迹地', transform=plt.gca().transAxes,
             bbox=dict(boxstyle='round,pad=0.5', fc='white', ec='red', alpha=0.8))

    plt.tight_layout()
    output_file = f"D:\\地理信息服务作业\\作业(SHP)\\Python_SHP_{month_num}月.png"
    plt.savefig(output_file, dpi=300, bbox_inches='tight')
    plt.close()
    print(f"已保存：{output_file}")


# 主函数
def main():
    for month_num, month_key in months.items():
        # 找到对应的shp文件夹
        shp_dir = None
        for d in os.listdir(SHP_BASE_DIR):
            if month_key in d and os.path.isdir(os.path.join(SHP_BASE_DIR, d)):
                shp_dir = os.path.join(SHP_BASE_DIR, d)
                break

        if shp_dir is None:
            print(f"未找到{month_num}月的文件夹")
            continue

        print(f"正在处理{month_num}月...")
        plot_burn(month_num, shp_dir)

    print("全部完成！")


if __name__ == "__main__":
    main()
