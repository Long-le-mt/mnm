arr1 = [1, 3, 5, 7, 9, 10]
arr2 = [2, 4, 6, 8]
# a
arr1[:1] = arr2
print( arr1)

# b

a = [1,2,3]
b = [4,5,6]
c = [10,11,12]
d = [7,8,9]
arr = [a, b, c ,d]
print(min(arr, key=sum))

# 3

arr = [('item1', '12.20'), ('item2', '15.10'), ('item3', '24.5')]
# giảm dần
print(sorted(arr, key=lambda x: float(x[1]), reverse=True))
# tăng dần
print(sorted(arr, key=lambda x: float(x[1])))