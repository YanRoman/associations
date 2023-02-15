from itertools import combinations

# transactions = {
#     '001' : ['milkshake', 'pie'], #3 ^ 3 - 3
#     '002' : ['milkshake', 'pie', 'cola']
# }

# products = ['milkshake', 'pie', 'cola']


# def getInfo():
#     list = []
#     for i in range(1, len(products)):
#         list += combinations(products, i)

#     for A in list:
#         for B in list:
#             x = 0
#             for elemA in A:
#                 for elemB in B:
#                     if elemA == elemB: 
#                         x += 1
#                         continue
#             if x == 0:
#                 print(str(A) + ' --> ' + str(B))


# getInfo()
# def getInfo():
#     for transaction in transactions.values():
    
#         for i in range(0, len(transaction)):
#             for x in range (0, i):
#                 firstProducts = transaction[x : i] # first products

#             for x in range (0, i):
#                 secodProducts = transaction[x : i] # second products]
#                 if firstProducts != secodProducts:
#                     print(str(firstProducts) + ' ---> ' + str(secodProducts))

            

        
        
# getInfo()


arr1 = ['test1', 'test2']
arr2 = ['test3', 'test1', 'test2']

count = 0
for e in arr1:
    if e in arr2: count+=1
if count == len(arr1):
    print("+")
else:
    print('-')