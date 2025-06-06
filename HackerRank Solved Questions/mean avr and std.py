import numpy
array=input().split()
n=int(array[0])
m=int(array[1])
arr=[]
for i in range(n):
    arr.append([*map(int,input().split())])
arr=numpy.array(arr)
print(numpy.mean(arr,axis=1))
print(numpy.var(arr,axis=0))
print(round(numpy.std(arr,axis=None),11))