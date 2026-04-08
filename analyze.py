import pandas as pd
import matplotlib.pyplot as plt

# 读取数据
df = pd.read_csv("movies.csv")

# 转换评分为浮点数
df["rating"] = df["rating"].astype(float)

# 打印基础信息
print("电影总数：", len(df))
print("平均评分：", df["rating"].mean())
print("最高评分：", df["rating"].max())
print("最低评分：", df["rating"].min())

# 画评分分布图
plt.hist(df["rating"], bins=10)

plt.title("Movie Rating Distribution")
plt.xlabel("Rating")
plt.ylabel("Count")

plt.savefig("rating.png")