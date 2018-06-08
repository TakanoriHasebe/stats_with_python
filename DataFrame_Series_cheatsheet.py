# pandasからSeries, DataFrameの読み込み
import pandas as pd
from pandas import Series, DataFrame

# クリップボードから読み込み
nfl_frame = pd.read_clipboard()

# DataFrameの列の名前が取り出せる
nfl_frame.columns

# 複数の列にアクセスする
nfl_frame[['Team', 'First NFL Season']]

# 新しいDataFrameを作成する
DataFrame(nfl_frame, columns=['Team', 'First Season'])

# 新しいDataFrameを作成する
# 存在しないカラムを作成するとnullが入る
DataFrame(nfl_frame, columns=['Team', 'First NFL Season', 'Stadium'])

# 列名でなく、行名でアクセスする
nfl_frame.ix[3]

# indexを付与してSeries形式で作成する
stadiums = Series(["Levi's Stadium", "AT&T Stadium"], index=[4,0])

# Series形式で作成したstadiumを代入する
nfl_frame['Stadiums'] = stadiums

# 作成したStadiumsを削除する
del nfl_frame['Stadiums']

# csvを読み込み
*_df = pd.read_csv('train.csv')

# 読み込んだDataFrameの情報を表示
*_df.info()

# DataFrameを関数に適用している。
def male_female_child(passenger):
    age, sex = passenger
    if age < 16:
        return 'child'
    else:
        return sex
    
titanic_df['person'] = titanic_df[['Age', 'Sex']].apply(male_female_child, axis=1)

# nanを削除
drop_na = titanic_df['Cabin'].dropna()

# 最初の1文字目を取得する
levels = []
for level in drop_na:
    levels.append(level[0])

# listをDataFrame化
cabin_df = DataFrame(levels)
    
# DataFrameに名前をつける
cabin_df.columns = ['Cabin']    
    
# 上記のcabin_dfからTを取り除いた
cabin_df = cabin_df[cabin_df.Cabin != 'T']  

# 列名の中の文字ともう１つの列を指定して抜き出し
before = paired_test_data.query('medicine == "before"')["body_temperature"]

# csv形式で読み込み
df = pd.read_csv('test.csv')

# 複数の列を削除
drop_col = ["Sex", "Age", "SibSp", "Parch", "Ticket", "Fare", "Cabin", "Embarked"]    
df.drop(drop_col, axis=1, inplace=True)

# csv形式で出力
df.to_csv("result.csv", index=False)
    
    
    
    
    
    
    
    