def printMessage():
    print("\nHello World\n")
    return

printMessage()


def printMessage(name):
    print("Hello {0}!\n".format(name))
    return

printMessage("Geoff")


def getMessage(message, name):
    newMesssage = ("{0} {1}!\n".format(message, name))
    return newMesssage

result = getMessage("Hello", "Aaron")
print(result)

def main():
    productTax = 4 * 1
    productTwo = 4 * 2
    return productTax, productTwo

totalCost = main()
s=totalCost[0]
y=totalCost[1]
print(s)
print(y)
print("First product = {0}, Second product = {1}\n".format(s,y))


taxRate=1.15

def tax(price, taxRate):
    productWithTax = price * taxRate
    return productWithTax

def products():
    productPrice = float(input("Enter the price of the product: $"))
    total = tax(productPrice, taxRate)
    print("The final cost is ${0:.2f}".format(total))

products()
products()
products()
products()