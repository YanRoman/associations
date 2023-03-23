import timeit
import eel
from itertools import combinations


eel.init("web")


@eel.expose
def take_py(dataFile): 
    buildProducts(dataFile)
    buildTransactions(dataFile)
    buildInfo()  


products = []
transactions = {}
info = []
minsupport = 2


@eel.expose
def getProducts():
    return products


@eel.expose
def getInfo():
    return sorted(info, key=lambda item: item[4])[::-1]


def buildProducts(data):
    products.clear()
    for line in data.splitlines():
        if (not line.split()[1] in products):
            products.append(line.split()[1])


def buildTransactions(data):
    transactions.clear()
    lines = data.splitlines()
    temp = []

    for i in range(0, len(lines)):
        if lines[i].split()[0] in transactions:
            transactions[lines[i].split()[0]].append(lines[i].split()[1])
        else:
            temp = []
            temp.append(lines[i].split()[1])
            transactions[lines[i].split()[0]] = temp


def getList(list, i):
    if i >= len(products):
        return list
    list += combinations(products, i)
    return getList(list, i+1)

def buildInfo():
    info.clear()
    list = []
    list = getList(list, 1)
    for A in list:
        for B in list:
            x = 0
            for elemA in A:
                for elemB in B:
                    if elemA == elemB: 
                        x += 1
                        continue
            if x == 0:
                countAB = 0
                countA = 0
                countB = 0
                #Кол-во транзакций содержащих A и B
                for transaction in transactions.values():
                    if check(A, transaction) and check(B, transaction):
                        countAB += 1
                    if check(A, transaction):
                        countA += 1
                    if check(B, transaction):
                        countB += 1
                if countA != 0 and countB != 0:
                    #Поддержка
                    s = countAB * 100 / len(transactions)
                    #Достоверность
                    c = countAB  * 100 / countA
                    #Лифт
                    l = c / (countB * 100 / len(transactions))
                    if s >= minsupport:
                        temp = [clearStr(str(A)), clearStr(str(B)), str(round(s, 2)), str(round(c, 2)), str(round(l, 2))]
                        info.append(temp)
    

def check(arr1, arr2):
    count = 0
    for e in arr1:
        if e in arr2: count+=1
    if count == len(arr1):
        return True
    return False


def clearStr(str):
    chars = "'!,()\""
    return str.translate(str.maketrans('', '', chars))


elapsed_time = timeit.timeit(buildInfo, number=100)/100
print(elapsed_time)
eel.start("main.html")


    
