#input
hockeyTeam=input("What is the name of the hockey team? ")
wins=input("How many wins does the {0} have? ").format(hockeyTeam)
loses=input("How many loses does the {0} have? ")
    
#Process 
totalGames=int(wins)+int(loses)
percentage=100
winPercent=(int(wins)/total)*percentage
    
#Output
print("The {0} have {1} wins and {2} loses, with a win percentage of {3:.4f}. ".format(hockeyTeam, wins, loses, winPercent))
