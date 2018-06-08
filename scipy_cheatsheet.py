# ライブラリのimport
import scipy as sp
from scipy import stats
import statsmodels.formula.api as smf
import statsmodels.api as sm
# 表示桁数の指定
%precision 3

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

# 平方根
sp.sqrt(num)

# 相関行列
sp.corrcoef(x, y)

# 四分位点
# 下から25%にくる値
fish_data_3 = np.array([1,2,3,4,5,6,7,8,9])
stats.scoreatpercentile(fish_data_3, 25)

# 四分位点
# 下から75%にくる値
stats.scoreatpercentile(fish_data_3, 75)

# stats.norm.pdf関数は確率密度を計算可能
# loc : 平均値, scale : 標準偏差
stats.norm.pdf(x = x, loc = 4, scale = 0.8)

# 累積分布関数
# loc : 平均値, scale : 標準偏差, x : 値
stats.norm.cdf(loc = 4, scale = 0.8, x = 3)

# t検定
# t検定をしたいデータを入れる
stats.ttest_rel(after, before)

# 対応のないt検定
stats.ttest_ind(after, before, equal_var = False)

# 平均２乗誤差を利用
# 2変数のモデル化
lm_model = smf.ols(formula = "beer ~ temperature", data = beer).fit()

# 推定結果
lm_model.summary()

# 気温のみのAIC
lm_model.aic




