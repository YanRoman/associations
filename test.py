import timeit
from itertools import combinations


def buildProducts(data, products):
    products.clear()
    for line in data.splitlines():
        if (not line.split()[1] in products):
            products.append(line.split()[1])


def getAprioriTable(data, products):
    apriori_table = {}
    lines = data.splitlines()

    for line in lines:
        if not line.split()[0] in apriori_table:
            for product in products:
                if product == line.split()[1]:
                    temp = [product]
            apriori_table[line.split()[0]] = temp
        else:
            for product in products:
                if product == line.split()[1]:
                    apriori_table[line.split()[0]].append(product) 
    return apriori_table


def apriori(F, k, aprioriTable, min):
    newF = []

    if k == 0:
        for item in F:
            count = 0
            for transaction in aprioriTable.values():
                if item in transaction:
                    count += 1
            if count >= min:
                newF.append(item)
        return newF

    if k == 1:
        tempF = []
        tempF += combinations(F, 2)
        temp = []
        for item in tempF:
            temp += [item[1], item[0]]
        tempF += temp

        for combination in tempF:
            count = 0
            for transaction in aprioriTable.values():
                if combination[0] in transaction and combination[1] in transaction:
                    count += 1
            if count >= min:
                newF.append(combination)
        return newF
    
    if k == 2:
        tempF = []
        for i in range (0, len(F)):
            for j in range (i + 1, len(F)):
                if F[i][0] == F[j][0] and F[i][1] != F[j][1]:
                    temp = [F[i][0], F[i][1], F[j][1]]
                    tempF.append(temp)

        for combination in tempF:
            count = 0
            for transaction in aprioriTable.values():
                if combination[0] in transaction and combination[1] in transaction and combination[2] in transaction:
                    count += 1
            if count >= min:
                newF.append(combination)
        return newF
        
    if k == 3:
        tempF = []
        for i in range (0, len(F)):
            for j in range (i + 1, len(F)):
                if F[i][0] == F[j][0] and F[i][1] == F[j][1] and F[i][2] != F[j][2]:
                    temp = [F[i][0], F[i][1], F[i][2], F[j][2]]
                    tempF.append(temp)
        
        for combination in tempF:
            count = 0
            for transaction in aprioriTable.values():
                if combination[0] in transaction and combination[1] in transaction and combination[2] in transaction:
                    count += 1
            if count >= min:
                newF.append(combination)
        return newF 
    
    # for i in range (0, len(F)):
    #     for j in range (i + 1, len(F)):
    #         flag = True
    #         for m in range(0, k - 2):
    #             if F[i][m] != F[j][m]:
    #                 flag = False
    #         if F[i][k-1] == F[j][k-1]:
    #             flag = False
    #         if flag:
    #             temp = []
    #             for m in range(0, k - 2):
    #                 temp.append(F[i][m])
    #             temp.append(F[i][k-1])
    #             temp.append(F[j][k-1])
                
    #     for combination in tempF:
    #         count = 0
    #         for transaction in aprioriTable.values():
    #             if combination[0] in transaction and combination[1] in transaction and combination[2] in transaction:
    #                 count += 1
    #         if count >= min:
    #             newF.append(combination)
    #     return newF 



def main():
    min = 2
    data = open('product.txt').read()
    products = []

    buildProducts(data, products)
    aprioriTable = getAprioriTable(data, products)

    F1 = apriori(products, 0, aprioriTable, min)
    F2 = apriori(F1, 1, aprioriTable, min)
    F3 = apriori(F2, 2, aprioriTable, min)
    F4 = apriori(F3, 3, aprioriTable, min)
    
    print('<<<<<<<<<<<<<<<<<<<<<<F1', F1)
    print('<<<<<<<<<<<<<<<<<<<<<<F2', F2)
    print('<<<<<<<<<<<<<<<<<<<<<<F3', F3)
    print('<<<<<<<<<<<<<<<<<<<<<<F4', F4)

main()
#elapsed_time = timeit.timeit(main, number=100)/100
#print(elapsed_time)




