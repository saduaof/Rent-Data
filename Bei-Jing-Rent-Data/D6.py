# -*- coding: utf-8 -*-
"""
Created on Thu Nov 21 23:40:10 2024

@author: Lenovo
"""
#距离地铁站最近的前6种户型
import pandas as pd
import matplotlib.pyplot as plt
import re

# 读取Excel文件
df = pd.read_excel('bj_danke_cleaned.xlsx')

# 提取“地铁”列中的距离信息，并转换为数值型
# 正则表达式用于匹配字符串中的数字
df['地铁距离'] = df['地铁'].apply(lambda x: int(re.findall(r'\d+', x)[0]) if re.findall(r'\d+', x) else 0)

# 将“价格”列转换为数值型
df['价格'] = pd.to_numeric(df['价格'], errors='coerce')

# 计算价格与地铁站距离的相关性
correlation = df['价格'].corr(df['地铁距离'])

# 找出排名前6的户型
top_6_house_types = df['户型'].value_counts().head(6)

# 打印相关性结果
print(f"价格与地铁站距离的相关性系数为: {correlation}")

# 打印排名前6的户型
print("排名前6的户型:")
print(top_6_house_types)

# 可视化排名前6的户型数量
top_6_house_types.plot(kind='line', marker='o')  # 使用折线图并添加数据点标记
plt.title('距离地铁站最近的前6种户型')
plt.xlabel('House Type')
plt.ylabel('Count')
plt.xticks(rotation=45)  # 旋转x轴标签以便更好地显示
plt.savefig('距离地铁站最近的前6种户型D6.png', bbox_inches='tight')  #将生成的图片保存
plt.show()