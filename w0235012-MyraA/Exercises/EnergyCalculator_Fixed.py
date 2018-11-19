"""
Student Name:  Geoff Gillespie  
Program Title:  Energy Calculator - BROKEN
Description:   Debugging practice

Student Name:  Aaron Myra  
Program Title:  Energy Calculator - Fixed
Description:   Debugging practice
"""

def main(): #<-- Don't change this line!
    
    print("Energy Calculator")
    print("\nThis program will calculate how much you pay for electricity for")
    print("a particular device, based on the wattage of the device and how")
    print("many hours the device was in use.")
    print("\nCalculations are based on a cost of 12.65 cents per kiloWatt hour.")

    #BUG BELOW - Price In Watts
    #kwhPrice = 12.65
    kwhPrice = 0.1265
    avgDaysInAMonth = 30.42
    monthsInYear = 12
    hoursInADay = 24
    wattsToKiloWatts = 1000

    deviceWattage = float(input("\nEnter the wattage of the device: "))
    hoursUsedPerDay = float(input("Enter how many hours per day the device is in use: "))

    #BUG BELOW - Wrong Mathamatical Equation
    #costPerHour = ((deviceWattage /100) * kwhPrice) / 100
    costPerHour = (deviceWattage / 1000) * kwhPrice
    #BUG BELOW - Mathamatical Error
    #costPerDay = hoursUsedPerDay
    costPerDay = costPerHour * hoursUsedPerDay
    #BUG BELOW - (* 60) Is Uns=nessary
    #costPerMonth = avgDaysInAMonth * costPerDay * 60
    costPerMonth = avgDaysInAMonth * costPerDay
    costPerYear = monthsInYear * costPerMonth
    kwhPerDay = (deviceWattage /1000) * hoursUsedPerDay

    #BUG BELOW - Same Place Holder Used
    #print("\nElectrical cost for a device using {0:.2f} watts for {0} hour per day:".format(deviceWattage, hoursUsedPerDay))
    print("\nElectrical cost for a device using {0:.2f} watts for {1} hour per day:".format(deviceWattage, hoursUsedPerDay))
    #BUG BELOW - Wrong Decimal Format
    #print("\tCost Per Hour:\t${0:.1f}".format(costPerHour))
    print("\tCost Per Hour:\t${0:.2f}".format(costPerHour))
    #BUG BELOW - Wrong Decimal Format
    #print("\tCost Per Day:\t${0:.4f}".format(costPerDay))
    print("\tCost Per Day:\t${0:.2f}".format(costPerDay))
    #BUG BELOW - Wrong Decimal Format
    #print("\tCost Per Month:\t${0:.5f}".format(costPerMonth))
    print("\tCost Per Month:\t${0:.2f}".format(costPerMonth))
    #BUG BELOW - Wrong Variable Used
    #print("\tCost Per Year:\t${0:.2f}".format(costPerMonth))
    print("\tCost Per Year:\t${0:.2f}".format(costPerYear))
    print("\tkWh Per Day:\t{0:.2f}".format(kwhPerDay))

    #Your code ends on the line above

#Do not change any of the code below!
if __name__ == "__main__":
    main()