import matplotlib.pyplot as plt

# 设置字体大小为10
plt.rcParams['legend.fontsize'] = 10
# 设置字体格式为Times New Roman
plt.rcParams['font.family'] = 'Times New Roman'

# plt.rcParams['mathtext.fontset'] = 'stix'

# plt.rcParams['font.size'] = 14.0
# plt.rcParams['legend.fontsize'] = 12.5

fig = plt.figure(figsize=(6, 4), dpi=100)


# X轴数据
x = [1, 2, 3, 4, 5]

# Y轴数据
y = [1, 4, 9, 16, 25]

# 创建折线图
plt.plot(x, y)

# 添加标签和标题
plt.xlabel('X轴')
plt.ylabel('Y轴')



# 显示图形
plt.show()