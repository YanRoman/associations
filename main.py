import eel
from itertools import combinations


eel.init("web")

products = []
transactions = {}
info = []
minsupport = 1


@eel.expose
def take_py(dataFile): 
    buildProducts(dataFile)
    buildTransactions(dataFile)
    buildInfo()


@eel.expose
def getProducts():
    return products


@eel.expose
def getInfo():
    return info


def buildProducts(data):
    for line in data.splitlines():
        if (not line.split()[1] in products):
            products.append(line.split()[1])


def buildTransactions(data):
    lines = data.splitlines()
    temp = []

    for i in range(0, len(lines)):
        if lines[i].split()[0] in transactions:
            transactions[lines[i].split()[0]].append(lines[i].split()[1])
        else:
            temp = []
            temp.append(lines[i].split()[1])
            transactions[lines[i].split()[0]] = temp


def buildInfo():
    list = []
    for i in range(1, len(products)):
        list += combinations(products, i)

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


eel.start("main.html")


    
