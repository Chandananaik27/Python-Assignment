import numpy

my_array = input().split()
n = int(my_array[0])
m = int(my_array[1])
arr = []
for i in range(n):
    arr.append([*map(int, input().split())])
arr = numpy.array(arr)

maximum = (numpy.min(arr, axis=1))
print(numpy.max(maximum))

