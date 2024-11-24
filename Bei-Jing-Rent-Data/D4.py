# -*- coding: utf-8 -*-
"""
Created on Thu Nov 21 15:08:24 2024

@author: Lenovo
"""
#户型数量分析
import pandas as pd
import matplotlib.pyplot as plt


# 加载Excel文件
df = pd.read_excel('bj_danke_cleaned.xlsx')

# 统计不同户型的数量
house_counts = df['户型'].value_counts()

# 绘制柱状图
plt.figure(figsize=(10, 8))
plt.bar(house_counts.index, house_counts.values, color='skyblue')

# 添加标题和标签
plt.title('不同户型的住户数量分布')
plt.xlabel('户型')
plt.ylabel('数量')
plt.savefig('户型数量分析D4.png', bbox_inches='tight')  #将生成的图片保存
# 显示图表
plt.show()