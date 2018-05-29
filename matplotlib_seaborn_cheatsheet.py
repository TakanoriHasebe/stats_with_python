# ライブラリのimport
import numpy as np
import pandas as pd
# 表示桁数の指定
%precision 3
from matplotlib import pyplot as plt
import seaborn as sns
sns.set()
# グラフをjupyter notebook内に表示
%matplotlib inline

sns.関数名(
 x = "x軸の列名",
 y = "y軸の列名",
 data = データフレーム,
 その他引数
)

# グラフのプロット, 保存
plt.plot(x, y, color='black')
plt.title("lineplot matplotlib") # タイトル
plt.xlabel("x") # x軸
plt.ylabel("y") # y軸
plt.savefig("01") # グラフの保存

# ヒストグラムの描画
sns.distplot(fish_data, bins = 5, color = 'black', kde = False)

# 箱ひげ図
sns.boxplot(x = "species", y = "length", data = fish_multi, color='gray')

# バイオリンプロット
sns.violinplot(x = "species", y = "length", data = fish_multi, color = 'gray')

# 棒グラフ
sns.barplot(x = "species", y = "length", data = fish_multi, color='gray')

# 散布図
# 散布図を描く
sns.jointplot(x="x", y="y", data=cov_data, color="black")

# ペアプロット
sns.pairplot(iris, hue='species', palette='gray')












