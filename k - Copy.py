import csv
import matplotlib.pyplot as plt
import numpy as np
import math
import matplotlib.cm as cm
import itertools
with open('newSheet.csv') as input, open('NewSheet1.csv', 'w') as output:
    non_blank = (line for line in input if line.strip())
    output.writelines(non_blank)
with open('newSheet1.csv', 'rb') as f:
    reader = csv.reader(f)
    data = map(tuple, reader)

#data=[1,3,5,7,13,22,26,31,29,30,4]
data.sort()
k_arr=[]
print 'Enter the Number of clusters:'
n=int(raw_input())
for num in range(0,n,1):
    print 'Enter the x,y co-ordinates of cluster ',num+1
    k_arr_temp=list(map(float,raw_input().split()))
    k_arr.append(k_arr_temp)
d={}
d_name={}
d_old={}
d_name_old={}
temp=n
k='k'
for t in range(0,10,1):
    d={}
    print k_arr
    for i in data:
        j=0
        dist=[]
        while(temp!=0):
            dist.append(math.sqrt(pow(k_arr[j][0]-float(i[2]),2)+pow(k_arr[j][1]-float(i[3]),2)))
            #print dist
            temp=temp-1
            j=j+1
        temp=n
        value_k=dist.index(min(dist))
        if k+str(value_k) not in d:
            d[k+str(value_k)]=[[float(i[2]),float(i[3])]]
            d_name[k+str(value_k)]=[i[4]]
        else:
            d[k+str(value_k)].append([float(i[2]),float(i[3])])
            d_name[k+str(value_k)].append(i[4])
    print d
    print "end of ieration ",t
    if d_old!=d:
        d_old=d
        d_name_old=d_name
        #print d_old
        #print d
        print d_name
        k_arr=[]
        
        for key,value in d.items():
            total_x=0
            total_y=0
            for sub_value in value:
                total_x+=sub_value[0]
                total_y+=sub_value[1]
            mean_x=total_x/len(value)
            mean_y=total_y/len(value)
            k_arr.append([mean_x,mean_y])
        k_arr.sort()
        print k_arr
    else:
        break
print "out of loop"

colors = itertools.cycle(["red", "blue", "green","violet","yellow","orange"])
#colors = iter(cm.rainbow(np.linspace(0, 1, len(ys))))

_, ax = plt.subplots(2)
temp_x=[]
temp_y=[]
for temp1 in data:
    temp_x.append(temp1[2])
    temp_y.append(temp1[3])

ax[0].scatter(temp_x,temp_y,color='black')
ax[0].set_title("Initial distribution")

k_arr_x=[]
k_arr_y=[]
for value in k_arr:
    k_arr_x.append(value[0])
    k_arr_y.append(value[1])
ax[1].scatter(k_arr_x,k_arr_y,marker='X',color='black')
ax[1].set_title("After clustering color partition")
for key,value in d.items():
    k_x=[]
    k_y=[]
    for mark in value:
        k_x.append(mark[0])
        k_y.append(mark[1])
    ax[1].scatter(k_x,k_y,color=next(colors))
plt.show()
'''
k0_x=[]    
k0_y=[]
k1_x=[]
k1_y=[]
k_arr_x=[]
k_arr_y=[]
for value in d["k0"]:
    k0_x.append(value[0])
    k0_y.append(value[1])
for value in d["k1"]:
    k1_x.append(value[0])
    k1_y.append(value[1])
for value in k_arr:
    k_arr_x.append(value[0])
    k_arr_y.append(value[1])
plt.scatter(k0_x,k0_y,color='red')
plt.scatter(k1_x,k1_y,color='blue')
plt.scatter(k_arr_x,k_arr_y,marker='X',color='black')
plt.show()
'''


