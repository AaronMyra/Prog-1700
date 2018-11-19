#Don't forget to rename this file after copying the template
#for a new program!
"""
Student Name:   Aaron Myra
Program Title:  Imperial To Metric Conversion
Description:    Converts values from imperial to metric
"""

def main(): #<-- Don't change this line!
    #Write your code below. It must be indented!

    #Input
    print("\nImperial to Metric Converter")
    print("\nPlease enter the following values")
    #Prompt the user to input data
    imperialTons=float(input("\tTons: "))
    imperialStones=float(input("\tStones: "))
    imperialPounds=float(input("\tPounds: "))
    imperialOunces=float(input("\tOunces: "))
    metricConversion=1000

    #Process
    #Convert weight entirely into ounces using the provided formula
    totalOunces=35840*imperialTons+224*imperialStones+16*imperialPounds+imperialOunces
    kilos=totalOunces/35.274
    metricTons=kilos/metricConversion
    totalKilos=kilos-(int(metricTons)*metricConversion)
    totalGrams=(kilos-int(kilos))*metricConversion
    
    
    #Output
    print("\nYour values in metric are: ")
    print("\n\tMetric Tons: {0}".format(int(metricTons)))
    print("\tKilograms: {0}".format(int(totalKilos)))
    print("\tGrams: {0:.1f}\n".format(totalGrams))
    
    #Your code ends on the line above

#.Do not change any of the code below!
if __name__ == "__main__":
    main()