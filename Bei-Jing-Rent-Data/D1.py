# -*- coding: utf-8 -*-
"""
Created on Thu Nov 21 13:41:23 2024

@author: Lenovo
"""
#前15房价分析
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties

# 设置matplotlib的字体为支持中文的字体
plt.rcParams['font.sans-serif'] = ['SimHei']  # 'SimHei' 是一种常用的中文黑体字体
plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号

# 读取Excel文件
df = pd.read_excel('bj_danke_cleaned.xlsx')

# 清理数据，移除任何包含空值的行
df_cleaned = df.dropna(subset=['价格', '小区'])

# 将价格列转换为数值类型，无法转换的值将被设置为NaN
df_cleaned['价格'] = pd.to_numeric(df_cleaned['价格'], errors='coerce')

# 再次清理数据，移除价格列中为NaN的行
df_cleaned = df_cleaned.dropna(subset=['价格'])

# 提取价格和小区名称列
price_subway = df_cleaned[['价格', '小区']]

# 对价格进行排序
sorted_price_subway = price_subway.sort_values(by='价格')

# 选择价格最低的前15个
top_15 = sorted_price_subway.head(15)

# 打印结果
print(top_15)

# 绘制柱状图
plt.figure(figsize=(12, 18))  # 增加图表的尺寸
plt.barh(top_15['小区'], top_15['价格'])
plt.xlabel('价格（元/月）')
plt.ylabel('小区')
plt.title('价格最低的前15个小区')
plt.gca().invert_yaxis()  # 反转y轴，使得价格最低的小区在上方

# 旋转小区名称以便它们能够更好地适应图表空间
plt.xticks(rotation=90)  # 旋转x轴标签（小区名称）90度
plt.savefig('前15的房价分析D1.png', bbox_inches='tight')  #将生成的图片保存
plt.show()