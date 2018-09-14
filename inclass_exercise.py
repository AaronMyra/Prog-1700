def main():
    #input
    hockeyTeam=input("What is the name of the hockey team? ")
    wins=input("How many wins does the " + hockeyTeam + " have? ")
    loses=input("How many loses does the "+ hockeyTeam + " have? ")
        
    #Process 
    totalGames=int(wins)+int(loses)
    percentage=100
    winPercent=(int(wins)/totalGames)*percentage
        
    #Output
    print("The {0} have {1} wins and {2} loses, with a win percentage of {3:.4f}. ".format(hockeyTeam, wins, loses, winPercent))
main()