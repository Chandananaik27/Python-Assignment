import numpy
array=int(input())
arr=[]
for i in range(array):
    number=input().split()
    float_value=[]
    for x in number:
        float_value.append(float(x))
    arr.append(float_value)
arr = numpy.array(arr)
print(round(numpy.linalg.det(arr), 2))