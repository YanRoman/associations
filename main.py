import eel


eel.init("web")

products = []
transactions = {}
info = []
minsupport = 1


@eel.expose
def take_py(dataFile): 
    buildProducts(dataFile)
    # print(getProducts())

    buildTransactions(dataFile)
    # for key, value in transactions.items():
    #     print("{0}: {1}".format(key, value))

    buildInfo()
    print(info)


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
    for firstProduct in products:
        for secondProduct in products: 
            countAB = 0
            countA = 0
            countB = 0
            if firstProduct != secondProduct:
                #Кол-во транзакций содержащих A и B
                for transaction in transactions.values():
                    print(transaction)
                    if firstProduct in transaction and secondProduct in transaction:
                        countAB+=1
                    if firstProduct in transaction:
                        countA+=1
                    if secondProduct in transaction:
                        countB+=1

                print(countA)
                if countA != 0:
                    #Поддержка
                    s = countAB * 100 / len(transactions)
                    #Достоверность
                    c = countAB  * 100 / countA
                    #Лифт
                    l = c / (countB * 100 / len(transactions))
                    if s >= minsupport:
                        temp = [firstProduct, secondProduct, str(round(s, 2)), str(round(c, 2)), str(round(l, 2))]
                        info.append(temp)
                    




eel.start("main.html")


    
