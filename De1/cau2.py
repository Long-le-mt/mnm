str = "w3resource"

dict = {}

# Cách 1
# for x in str:
#     if x in dict :
#         dict[x] += 1
#     else:
#         dict[x] = 1

# Cách 2 
# for x in str:
#     dict[x] = dict.get(x, 0) + 1
    
# print(dict)