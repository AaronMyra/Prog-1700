#Stock Purchase
costPerShare=25.625
numberOfShares=400.0
markdown=costPerShare*numberOfShares
print("Markdown Value = {0}".format(float(markdown)))

#Break-Even Point
FixedCost=5000.0
PricePerUnit=8.0
CostPerUnit=6.0
BreakEvenPoint=FixedCost/(PricePerUnit-CostPerUnit)
print("BreakEvenPoint = {0}".format(float(BreakEvenPoint)))

#Saving Account
Balance=100.0
Balance=Balance*1.05+100
Balance=Balance*1.05+100
Balance=Balance*1.05
Balance=round(Balance + str(2))
print("Balance = ", Balance)

#Profit From Stock
PurchasePrice=10.0
SellingPrice=15.0
PercentProfit=100*(SellingPrice-PurchasePrice)
print("Profit = " + str(PercentProfit))

#Projectile Motion
InitialHeight=5.0
InitialVelocity=50.0#FPS
Height=-16*(3*3)+(50*3)+5
print("Final Height = {0}".format(Height))