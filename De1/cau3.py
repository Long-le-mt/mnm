arr = [('item1', '12.20'), ('item2', '15.10'), ('item3', '24.5')]
# giảm dần
print(sorted(arr, key=lambda x: float(x[1]), reverse=True))
# tăng dần
print(sorted(arr, key=lambda x: float(x[1])))
