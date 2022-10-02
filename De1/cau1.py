arr1 = [1, 3, 5, 7, 9, 10]
arr2 = [2, 4, 6, 8]
# a
# Cách 1
# arr1[-1:] = arr2 
# print(arr1)

# Cách 2 
# arr1 = arr1[:len(arr1) - 1]
# arr1 += arr2
# print(arr1)

# Cách 3
# arr1 = arr1[:len(arr1) - 1]
# arr1.extend(arr2)
# print(arr1)

# b
# a = [1,2,3]
# b = [4,5,6]
# c = [10,11,12]
# d = [7,8,9]
# arr = [a, b, c ,d]
# print(max(arr, key=sum))
