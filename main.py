import eel


eel.init("web")


@eel.expose
def take_py(dataFile): 
    buildProducts(dataFile)
    print(getProducts())


@eel.expose
def getProducts():
    return products

products = []
def buildProducts(data):
    for line in data.splitlines():
        if (not line.split()[1] in products):
            products.append(line.split()[1])

# products = set()
# def getProducts(data):
#     for line in data:
#         print(line)
            

eel.start("main.html")
