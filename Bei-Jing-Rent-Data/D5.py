# -*- coding: utf-8 -*-
"""
Created on Thu Nov 21 15:43:36 2024

@author: Lenovo
"""
#前6的居住位置2的住户占比
import pandas as pd
import matplotlib.pyplot as plt

# 从Excel文件加载数据
df = pd.read_excel('bj_danke_cleaned.xlsx')

# 统计“位置2”字段中各个地区出现的次数
location_counts = df['位置2'].value_counts()

# 获取前6个最常见的地区
top_5_locations = location_counts.head(6)

# 绘制饼状图
plt.figure(figsize=(10, 8))
plt.pie(top_5_locations, labels=top_5_locations.index, autopct='%1.1f%%', startangle=140)
plt.title('Top 6 居住的位置2')
plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
plt.savefig('前6的居住位置2的住户占比D5.png', bbox_inches='tight')  #将生成的图片保存
# 显示图表
plt.show()