import pandas as pd

protein = pd.read_table('protein.txt', sep='\t')
protein.head()
print(protein.columns)
print(protein.shape)
protein.info()
sprotein = protein.drop(['Country'], axis=1)
sprotein.head()
from sklearn import preprocessing

sprotein_scaled = preprocessing.scale(sprotein)
print(sprotein_scaled)
from sklearn.cluster import KMeans

NumberOfClusters = range(1, 20)
Kmeans = [KMeans(n_clusters=i) for i in NumberOfClusters]
score = [Kmeans[i].fit(sprotein_scaled).score(sprotein_scaled) for i in range(len(Kmeans))]
score
import matplotlib.pyplot as plt

plt.plot(NumberOfClusters, score)
plt.xlabel('Number of Clusters')
plt.ylabel('Score')
plt.title('Elbow Curve')
plt.show()
myKmeans = KMeans(algorithm="auto", n_clusters=5, n_init=10, max_iter=200)
myKmeans.fit(sprotein_scaled)
print(myKmeans)
y_kmeans = myKmeans.predict(sprotein)
print(y_kmeans)


def print_kmcluster(k):
    for i in range(k):
        print('聚类', i)
        ls = []
        for index, value in enumerate(y_kmeans):
            if i == value:
                ls.append(index)
                print(protein.loc[ls, ['Country', 'RedMeat', 'Fish', 'Fr&Veg']])


print_kmcluster(5)
