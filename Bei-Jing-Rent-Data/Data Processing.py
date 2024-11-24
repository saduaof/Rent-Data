# -*- coding: utf-8 -*-
"""
Created on Thu Nov 21 13:28:57 2024

@author: Lenovo
"""
#数据清洗过程
import pandas as pd

# 1. 读取Excel文件
file_path = 'C:/Users/Lenovo/Desktop/shuju/RentData/bj_danke_11.xlsx'  # Excel文件路径
df = pd.read_excel(file_path)

# 2. 显示数据框架的前几行
print("数据框架的前几行：")
print(df.head())

# 3. 检查数据框架的信息
print("\n数据框架的信息：")
print(df.info())

# 4. 清理数据
# 去除空值
df_cleaned = df.dropna()

# 去除空列
df_cleaned = df_cleaned.dropna(axis=1)

# 去除重复值
df_cleaned = df_cleaned.drop_duplicates()

# 定义一个函数来检查和删除乱码数据
def remove_garbage_data(row):
    for col in df_cleaned.columns:
        if isinstance(row[col], str) and '\ufffd' in row[col]:  # '\ufffd'是常见的乱码字符
            return None  # 或者可以设置为特定的值，例如np.nan
    return row

# 应用函数去除乱码数据
df_cleaned = df_cleaned.apply(remove_garbage_data, axis=1).dropna()

# 5. 保存清理后的数据到新的Excel文件
cleaned_file_path = 'C:/Users/Lenovo/Desktop/shuju/RentData/bj_danke_cleaned.xlsx'  # 清理后文件的保存路径
df_cleaned.to_excel(cleaned_file_path, index=False)

print("\n清理后的数据已保存至", cleaned_file_path)