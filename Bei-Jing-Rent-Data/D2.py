# -*- coding: utf-8 -*-
"""
Created on Thu Nov 21 14:36:44 2024

@author: Lenovo
"""
#地区分析
import pandas as pd
import matplotlib.pyplot as plt

# 读取Excel文件
file_path = 'bj_danke_cleaned.xlsx'
df = pd.read_excel(file_path)

# 统计每个位置1的房源数量
location_counts = df['位置1'].value_counts()

# 按照数量降序排列
location_counts = location_counts.sort_values(ascending=False)

# 绘制柱状图
plt.figure(figsize=(10, 8))
location_counts.plot(kind='bar')
plt.title('房源数量按位置1分布')
plt.xlabel('位置1')
plt.ylabel('房源数量')
plt.xticks(rotation=45)  # 旋转x轴标签，以便更好地显示
plt.tight_layout()  # 自动调整子图参数, 使之填充整个图像区域
plt.savefig('地区分析D2.png', bbox_inches='tight')  #将生成的图片保存
plt.show()


