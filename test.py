import timeit
from itertools import combinations


def buildProducts(data, products):
    products.clear()
    for line in data.splitlines():
        if (not line.split()[1] in products):
            products.append(line.split()[1])


def apriori(data, products):
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


def getF1(products, apriori_table, min):
    F1 = []
    for product in products:
        count = 0
        for transaction in apriori_table.values():
            if product in transaction:
                count += 1
        if count >= min:
            F1.append(product)
    return F1



def apriorigen(F, k):
    print(k)
    for item in F:
        print(item)

    if k == 1:
        return combinations(F, 2)
    else:
        newF = []
        for i in F:
            for j in F:
                if i[k - 2] == j[k - 2] and i[k - 1] != j[k - 1]:
                    temp = []
                    for elem in i:
                        temp.append(elem)
                    temp.append(j[k - 1])
                    newF.append(temp)
    return newF


def alg(F,k, all, apriori_table, min):
    tempF = apriorigen(F, k)
    k += 1
    if k == 5:
        return
        
    newF = []
    for combination in tempF:
        count = 0
        for transaction in apriori_table.values():
            i = 0
            for product in combination: 
                if product in transaction:
                    i+=1
            if i == len(combination):
                count += 1
        if count >= min:
            newF.append(combination)
   
    for elem in newF:
        all.append(elem)
    alg(newF, k, all, apriori_table, min)
    


        



def main():
    min = 2
    data = open('product.txt').read()
    products = []

    buildProducts(data, products)
    apriori_table = apriori(data, products)

    for item in apriori_table:
        print(item, apriori_table[item])
 
    F1 = getF1(products, apriori_table, min)
    print("<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<F1>>>>>>>>>>>>>>>>>>>>>>>>>>")
    print(F1)

    all = []
    F = alg(F1, 1, all, apriori_table, min)
    print("<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<ALLLL>>>>>>>>>>>>>>>>>>>>>>>>>>")
    print(len(all))

    print(type(all))
    

    

main()
#elapsed_time = timeit.timeit(main, number=100)/100
#print(elapsed_time)




