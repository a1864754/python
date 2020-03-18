# 从Scikit-learn加载Fisher的鸢尾植物数据集
print("从Scikit-learn加载Fisher的鸢尾植物数据集")
from sklearn.datasets import load_iris

iris = load_iris()
print(iris)
print("-" * 50)

# 得到NumPy的nparray和pandas的DataFrame
print("得到NumPy的nparray和pandas的DataFrame")
import pandas as pd
import numpy as np

print('Your pandas version is %s' % pd.__version__, )
print('Your NumPy version is %s' % np.__version__, )
iris_nparray = iris.data
iris_dataframe = pd.DataFrame(iris.data, columns=iris.feature_names)
iris_dataframe['group'] = pd.Series([iris.target_names[k] for k in iris.target], dtype="category")
print("-" * 50)

# iris_nparray
# iris.data[:]
print(iris_dataframe)
# iris_dataframe['group']
print("-" * 50)

print("计算花萼的平均值和花瓣的平均值")
# 度量集中化趋势
# 计算花萼的平均值和花瓣的平均值
print(iris_dataframe.mean(numeric_only=True))
print("-" * 50)

print("计算花萼的中位数和花瓣的中位数")
# 计算花萼的中位数和花瓣的中位数
print(iris_dataframe.median(numeric_only=True))
print("-" * 50)

print("方差均值")
# 方差均值
print(iris_dataframe.std())
print("-" * 50)

print("每一个量化变量的max和min之间的差")
# 每一个量化变量的max和min之间的差
print(iris_dataframe.max(numeric_only=True) - iris_dataframe.min(numeric_only=True))
print("-" * 50)

print("峰度kurtosis")
# 使用分数位来工作
# 定义正态化度量
# 峰度kurtosis
from scipy.stats import kurtosis, kurtosistest

k = kurtosis(iris_dataframe['petal length (cm)'])
zscore, pvalue = kurtosistest(iris_dataframe['petal length (cm)'])
print('Kurtosis %0.3f z-score %0.3f p-value %0.3f' % (k, zscore, pvalue))
print("-" * 50)

print("偏斜度skewness")
# 偏斜度skewness
from scipy.stats import skew, skewtest

k = skew(iris_dataframe['petal length (cm)'])
zscore, pvalue = skewtest(iris_dataframe['petal length (cm)'])
print('skewtest %0.3f z-score %0.3f p-value %0.3f' % (k, zscore, pvalue))
print("-" * 50)

print("为分类型数据计数")
# 为分类型数据计数
iris_binned = pd.concat([
    pd.qcut(iris_dataframe.iloc[:, 0], [0, .25, .5, .75, 1]),
    pd.qcut(iris_dataframe.iloc[:, 1], [0, .25, .5, .75, 1]),
    pd.qcut(iris_dataframe.iloc[:, 2], [0, .25, .5, .75, 1]),
    pd.qcut(iris_dataframe.iloc[:, 3], [0, .25, .5, .75, 1]),
], join='outer', axis=1)
print("-" * 50)

print("理解频率")
# 理解频率
print(iris_dataframe['group'].value_counts())
print(iris_binned['petal length (cm)'].value_counts())
print(iris_binned.describe())
print("-" * 50)

print("创建列联表")
# 创建列联表
print(pd.crosstab(iris_dataframe['group'], iris_binned['petal length (cm)']))
print("-" * 50)

# 理解相关性
# 使用协方差和关联性
iris_dataframe.cov()
print("-" * 50)

# 相关性（标准化变量之后协方差估计）
print(iris_dataframe.corr())
print("-" * 50)

print("相关性平均化")
# 相关性平均化
print(iris_dataframe.corr() ** 2)
print("-" * 50)

print("非参数相关性")
# 非参数相关性
from scipy.stats import spearmanr
from scipy.stats import pearsonr

spearmanr_coef, spearmanr_p = spearmanr(iris_dataframe['sepal length (cm)'],
                                        iris_dataframe['sepal width (cm)'])
pearsonr_coef, pearsonr_p = pearsonr(iris_dataframe['sepal length (cm)'],
                                     iris_dataframe['sepal width (cm)'])
print('pearson correlant %0.3f | spearson correlation %0.3f' % (pearsonr_coef, spearmanr_coef))
print("-" * 50)

print("考虑表格的卡方检验")
# 考虑表格的卡方检验
from scipy.stats import chi2_contingency

table = pd.crosstab(iris_dataframe['group'], iris_binned['petal length (cm)'])
chi2, p, dof, expected = chi2_contingency(table.values)
print('chi2-square %0.2f p-value %0.3f' % (chi2, p))
print("-" * 50)

print("创建Z评分标准化")
# 修改数据分布
# 正态分布
# 创建Z评分标准化
from sklearn.preprocessing import scale

stand_sepal_width = scale(iris_dataframe['sepal width (cm)'])
X = stand_sepal_width
print(X)
print("-" * 50)

print("转换成其他著名分布")
# 转换成其他著名分布
tranformations = {'X': lambda X: X, '1/X': lambda X: 1 / X, 'X**2': lambda X: X ** 2,
                  'X**3': lambda X: X ** 3, 'log(X)': lambda X: np.log(X)}
for transformation in tranformations:
    pearsonr_coef, pearsonr_p = pearsonr(iris_dataframe['sepal length (cm)'],
                                         tranformations[transformation](iris_dataframe['sepal width (cm)']))
    print('Tranformation:%s\t Pearson\'s r:%0.3f' % (transformation, pearsonr_coef))
print("-" * 50)
