from sklearn import decomposition
import seaborn as sns
import pandas as pd

#create dataframe with 100% correlation
df1 = pd.DataFrame({'x1':[10,20,30,40],'x2':[10,20,30,40]})
sns.jointplot('x1','x2',df1)
pca_full_corr = decomposition.PCA(n_components=1)
pca_full_corr.fit(df1)
pca_full_corr.components_[0]
print(pca_full_corr.explained_variance_)
print(pca_full_corr.explained_variance_ratio_)#100% correlation
df1_pca = pca_full_corr.transform(df1)

#create dataframe with high correlation
df2 = pd.DataFrame({'x1':[10,20,30,40],'x2':[15,25,38,44]})
sns.jointplot('x1','x2',df2)
pca_high_corre = decomposition.PCA(n_components=1)
pca_high_corre.fit(df2)
pca_high_corre.components_[0]
print(pca_high_corre.explained_variance_)
print(pca_high_corre.explained_variance_ratio_)#99%correlation
df2_pca = pca_high_corre.transform(df2)
