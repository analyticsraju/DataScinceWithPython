#PCA: Converts data to multi(1000) dimensional to finite(100) dimensional data by linear algebra(eigen vector, covarience, matrix)
#PCA: eigen vector of covaraince matrix of given data.(in maths terms.)
import numpy as np

migration_matrix = np.array([[0.8,0.05],[0.2,0.95]])#squre matrix
before_population = np.array([[100],[100]])#eigen vector
print(before_population)

for i in list(range(1,100,1)):
    after_population = migration_matrix.dot(before_population)
    print("after year ", i , ":", after_population)
    before_population = after_population

np.linalg.eig(migration_matrix)#matrix

#eigen vector of any symmetric matrix are orthogonal to each other
m1 = np.array([[1,2],[2,1]])
np.linalg.eig(m1)


m2 = np.array([[1,2,3],[2,4,6],[3,6,5]])
np.linalg.eig(m2)