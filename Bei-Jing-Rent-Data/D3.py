# -*- coding: utf-8 -*-
"""
Created on Thu Nov 21 14:55:23 2024

@author: Lenovo
"""
#小区分析
import pandas as pd
import matplotlib.pyplot as plt


# 请确保你已经安装了pandas和openpyxl库
# pip install pandas openpyxl matplotlib

# 读取Excel文件
data = pd.read_excel('bj_danke_cleaned.xlsx')

# 提取价格和小区名称
data['小区'] = data['小区'].str.strip()  # 去除小区名称的空格
data['价格'] = pd.to_numeric(data['价格'], errors='coerce')  # 将价格转换为数字

# 找到房租最贵的前12个小区
top_12_expensive = data.groupby('小区')['价格'].mean().nlargest(12).reset_index()

# 按照价格升序排列
top_12_expensive = top_12_expensive.sort_values(by='价格')

# 绘制折线图
plt.figure(figsize=(10, 6))
plt.plot(top_12_expensive['小区'], top_12_expensive['价格'], marker='o')
plt.title('Top 12 Most Expensive Communities')
plt.xlabel('Community')
plt.ylabel('Average Rent Price')
plt.xticks(rotation=45)
plt.grid()
plt.tight_layout()
plt.savefig('小区分析D3.png', bbox_inches='tight')  #将生成的图片保存
plt.show()
