import numpy as np
from sklearn.cluster import KMeans
import pandas as pd
data='wind.xlsx'
data=pd.read_excel('wind.xlsx') #导入信息
d=data['Temp']
print(d)
d=np.array(d)
d=[[i] for i in d]
print('原始数据:',d)
#聚类器
estimator = KMeans(n_clusters=9)#构造聚类器
estimator.fit(d)#聚类
label_pred = estimator.labels_ #获取聚类标签
centroids = estimator.cluster_centers_ #获取聚类中心
inertia = estimator.inertia_ # 获取聚类准则的总和
print('类别:',label_pred)
print('聚类中心:',centroids)
