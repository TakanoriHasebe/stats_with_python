import numpy as np

# ランダムに標本から選ぶ
# size = 1でサンプルサイズが１, replace = Falseで同じ魚は選ばれない
# １つの魚を選ぶ
np.random.choice(fish_5, size=1, replace=False)

# 3つの魚を選ぶ
# seedあり
np.random.seed(1)
np.random.choice(fish_5, size=3, replace=False)









