def main():

     #INPUT - # form user
    print("Welcome To The Coffee Shop!")
    print("This program will calculate total cost based on how many cups of coffee you order!")
    numberOfCups = input("Please enter the number of cups you wish to order: ")

    #PROCESSING - Price * number of cups
    coffeePrice = 1.25
    total = coffeePrice * float(numberOfCups)
    taxRate = 1.15
    #OUTPUT - Message to user, indicating total cost
    print("Cost before tax:  $",total)
    taxedTotal = total * taxRate
    print("Cost after tax:  $",taxedTotal)

main()