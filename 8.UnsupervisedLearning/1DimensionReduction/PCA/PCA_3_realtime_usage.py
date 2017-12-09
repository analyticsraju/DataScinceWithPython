import pandas as pd
from sklearn import decomposition

df1 = pd.DataFrame({
            'F1':[10,2,8,9,12],
            'F2':[20,4,16,18,24],
            'F3':[30,6,24,27,36]
        })

pca_train = decomposition.PCA()
pca_train.fit(df1)

print(pca_train.explained_variance_)
print(pca_train.explained_variance_ratio_)
print(pca_train.explained_variance_ratio_.cumsum())
#here any feature giving 100%
#reduce dimenstions to 1 after observing the ratio of variances along pcs
pca_test = decomposition.PCA(1)
pca_test.fit(df1)
print(pca_test.explained_variance_)
print(pca_test.explained_variance_ratio_)
print(pca_test.explained_variance_ratio_.cumsum())

#transform original data to new pc dimensions
df2 = pca_test.transform(df1)