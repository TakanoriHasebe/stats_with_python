import numpy as np

# ランダムに標本から選ぶ
# size = 1でサンプルサイズが１, replace = Falseで同じ魚は選ばれない
# １つの魚を選ぶ
np.random.choice(fish_5, size=1, replace=False)

# 3つの魚を選ぶ
# seedあり
np.random.seed(1)
np.random.choice(fish_5, size=3, replace=False)



はじめまして
「Pythonで学ぶあたらしい統計学の教科書」を勉強しています。
とてもわかりやすいです。
ch04での
x = np.arange(start=1, stop=7.1, step=0.1)
の等差数列は
平均：４, 分散：３.１００
となり、分散０.６４ではありません。
なぜ、正規分布となるのでしょうか。

よろしくお願いいたします。








