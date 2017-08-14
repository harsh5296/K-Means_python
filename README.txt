K-Means Cluster

I know that direct libraries are available to group similar datasets
like Scikit and directly call into functions 
eg. Python
from sklearn.cluster import kMeans
x=[]   #dataset
kmeans=kMeans(n_clusters=3)
kmeans.fit(X)

Still, I wanted to code it when I first Learned it during my curriculum.

1. Open k-Copy.py
2. Feed a csv file and change the name at line 7
3. Enter the number of clusters 
4. On Each line Enter the x,y co-ordinates of cluster center
5. The plot represents the initial and after distribution with cross marks as cluster centers. 

#Max number of clusters: 6