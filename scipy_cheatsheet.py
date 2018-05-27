# ライブラリのimport
import scipy as sp
from scipy import stats

# scipyで合計値を算出
sp.sum(fish_data)

# 平均値
sp.mean(fish_data)

# 標本分散
sp.var(fish_data, ddof=0)

# 普遍分散
sp.var(fish_data, ddof=1)

# 標準偏差
sp.std(fish_data, ddof=1)

# 平均
mu = sp.mean(fish_data)

# 最大値
sp.amax(fish_data)

# 最小値
sp.amin(fish_data)

# 中央値
sp.median(fish_data)

# 四分位点
# 下から25%にくる値
fish_data_3 = np.array([1,2,3,4,5,6,7,8,9])
stats.scoreatpercentile(fish_data_3, 25)

# 四分位点
# 下から75%にくる値
stats.scoreatpercentile(fish_data_3, 75)

