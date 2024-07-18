import debugpy
import pandas as pd
import matplotlib.pyplot as plt
#
#
# df1 = pd.DataFrame({'薪水': [1000, 2000, 3000],
#                     '备注': ['一般', '良好', '优秀'],
#                     '绩效': [70, 80, 90]},
#                    index=['张三', '李四', '王五'])
# # print(df1)
#
# df1.to_csv('test0708.csv')
# df1.to_excel('test0708.xlsx')
#
# df2 = pd.read_csv('test0708.csv')
# # print(df2)
# df3 = pd.read_excel('test0708.xlsx')
# # print(df3)
#
# df_self = pd.read_excel('/Users/fanjindong/Desktop/数据预处理/Lecture/news_spider/news_spider/news(2).xlsx')
# # print(df_self)
#
# df4 = pd.read_excel('pandastest.xlsx', index_col=0)
# # print(df4.head(3))
# # print(df4.tail(2))
# # print(df4.info())
# # print(df4.describe())
#
# df4['newcolumn'] = range(1, len(df4)+1)
#
# df4_reverse = df4.iloc[::-1].reset_index(drop=True)
# print(df4_reverse)
#
# df4.drop('备注', axis=1, inplace=True)
# print(df4)
#
# df4 = pd.read_excel('pandastest.xlsx', index_col=0)
# df4['备注'] = df4['备注'].str.join(',')  # 字符之间插入分隔符
# print(df4)
#
# df4 = pd.read_excel('pandastest.xlsx', index_col=0)
# print(df4)
# # 单个值的运算
# df4['薪水'] = df4['薪水'] + 1000
# print(df4)
# # 长度相等列的运算
# df4['绩效薪水'] = df4['薪水'] * df4['绩效'] / 100
# print(df4)

# df5 = pd.read_excel('testlevel.xlsx', sheet_name='Sheet1', index_col=0)
# df6 = pd.read_excel('testlevel.xlsx', sheet_name='Sheet2', index_col=0)

# df7 = pd.concat([df5, df6])
# print(df7)

# df1 = pd.DataFrame({'语文': [76, 88, 87], '数学': [78, 98, 89], '英语': [66, 77, 89]}, index=['韩梅梅', '李磊', '王明'])
# df2 = pd.DataFrame({'体育': [89, 99], '生物': [76, 89]}, index=['韩梅梅', '孙强'])
# df3 = pd.merge(left=df1, right=df2, left_index=True, right_index=True, how='left')
# print(df3)

# df1 = pd.DataFrame({'语文': [76, 88, 87], '数学': [78, 98, 89], '英语': [66, 77, 89]}, index=['韩梅梅', '李磊', '王明'])
# df2 = pd.DataFrame({'体育': [89, 99], '生物': [76, 89]}, index=['韩梅梅', '孙强'])
# df3 = pd.merge(left=df1, right=df2, left_index=True, right_index=True, how='left')
# df4 = df3.dropna()
# print(df3)
# print(df4)

# df1 = pd.DataFrame({'体育': [89, 99], '生物': [87, 65]}, index=['韩梅梅', '王明'])
# df2 = pd.DataFrame({'体育': [89, 98], '生物': [87, 99]}, index=['韩梅梅', '孙强'])
# df3 = pd.concat([df1, df2])
# print(df3)
# df4 = df3.drop_duplicates()
# print(df4)

# df4 = pd.read_excel('pandastest.xlsx', index_col=0)
# print(df4.iloc[:3, :2])
# print(df4.iloc[:4, :])
# print(df4.iloc[:, :1])

# df4 = pd.read_excel('pandastest.xlsx', index_col=0)
# print(df4.loc[:, '绩效':'备注'])
# print(df4.loc['王五':'周八', :])
# print(df4.loc['王五':'周八', '绩效':'备注'])
# print(df4.loc[['王五', '周八'], '绩效':'备注'])
# print(df4.loc[:, :])
# print(df4['薪水'] == 1000)
# print(df4.loc[df4['薪水'] == 1000])
# print(df4.loc[df4['薪水'] == 1000, ['薪水', '绩效']])
# print(df4.loc[(df4['薪水'] >= 2000) & (df4['绩效'] == 90)])

# # 第一步: 读取数据
# df = pd.read_excel('testmatplotlib.xlsx')
# # 第二步: 将所需数据赋值给对应的变量
# df_year, df_Agriculture = df["Year"], df["Agriculture"]
# # 第三步: 用matplotlib中绘图框架的plot()方法绘制红色的折线图
# plt.plot(df_year, df_Agriculture, "-", color="lightblue", linewidth=2)
# # 添加横坐标轴标签
# plt.xlabel("Year")
# # 添加纵坐标轴标签
# plt.ylabel("Percent")
# # 添加标题
# plt.title("Percent of American women earn Agriculture's degree")
# plt.show()
#
# df = pd.read_excel('testmatplotlib.xlsx', index_col='Year')
# df_CS = df['Computer Science']
# df_MS = df['Math and Statistics']
# # 可以通过DataFrame的plot()方法直接绘制
# # color指定线条的颜色
# # style指定线条的样式
# # legend指定是否使用标识区分
# df_CS.plot(color='b', style='.-', legend=True)
# df_MS.plot(color='r', style='-', legend=True)
# plt.title("Percentage of Computer Science's degrees VS Math and Statistics's")
# plt.xlabel("Years")
# plt.ylabel("Percentage")
# plt.show()

# # 散点图
# df = pd.read_csv("iris.csv")
# # 原始数据中没有给出字段名, 在这里指定
# df.columns = ['sepal_len', 'sepal_wid', 'petal_len', 'petal_wid','species']
# # 用绘图框架的plot()方法绘图, 样式为".", 颜色为红色
# plt.plot(df["sepal_len"], df["sepal_wid"], ".", color="r")
# plt.xlabel("sepal length")
# plt.ylabel("sepal width")
# plt.title("Iris sepal length and width analysis")
# plt.show()

# 箱图
df = pd.read_csv("iris.csv")
# 原始数据中没有给出字段名, 在这里指定
df.columns = ['sepal_len', 'sepal_wid', 'petal_len', 'petal_wid','species']
df.plot(kind='box', y='sepal_len')
plt.ylabel("sepal length in cm")
plt.show()

# 饼图
df = pd.read_csv("iris.csv")
df.columns = ['sepal_len', 'sepal_wid', 'petal_len', 'petal_wid','species']
df["species"] = df["species"].apply(lambda x: x.replace("Iris-",""))
# 对species列进行分类并对sepal_len列进行计数
df_gbsp = df.groupby("species", as_index=False)["sepal_len"].agg({"counts": "count"})
# 对counts列的数据绘制饼状图.
plt.pie(df_gbsp["counts"], labels=df_gbsp["species"], autopct="%.2f%%")
plt.show()

# 柱状图
df = pd.read_csv("iris.csv")
df.columns = ['sepal_len', 'sepal_wid', 'petal_len', 'petal_wid','species']
df["species"] = df["species"].apply(lambda x: x.replace("Iris-",""))
df_gbsp = df.groupby("species").mean()
# 绘制"sepal_len"列柱形图
plt.bar(df_gbsp.index,df_gbsp["sepal_len"], width= 0.5 , color = "g")
plt.show()

# 直方图
df = pd.read_csv("iris.csv")
df.columns = ['sepal_len', 'sepal_wid', 'petal_len', 'petal_wid','species']
df["species"] = df["species"].apply(lambda x: x.replace("Iris-",""))
# hist()方法绘制直方图
plt.hist(df["sepal_wid"], bins=20, color="lightblue")
plt.show()
#修改为累加直方图, 透明度为0.7
plt.hist(df["sepal_wid"], bins=20, color="lightblue", cumulative=True, alpha = 0.7)