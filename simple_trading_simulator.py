# This simulator is used to test the effectiveness of 
# risk management strategies in trading.
# User can see the performance of their trading strategies 
# when pairing with their own risk management strategies.

# Importing random to generate random number between 0 and 1
from random import random

# Importing the datetime to get the current date and time
from datetime import datetime

# Importing matplotlib to plot the graph
import matplotlib.pyplot as plt

# This function is created to simulate a single trade
def simOneTrade(winRate):
    if random() <= winRate / 100:
        return "win"
    else:
        return "loss"

# This function is created to calculate current dollar risk per trade
def calcCurrentRiskPerTrade(riskPerTrade, currentCap):
    return riskPerTrade * currentCap / 100

# This function will calculate profit or loss after each trade
def calcProfitLoss(tradeResult, currentRiskPerTrade, riskRewardRatio):
    if tradeResult == "win":
        return currentRiskPerTrade * riskRewardRatio
    else:
        return -currentRiskPerTrade

# This function will update the current capital after each trade
def updateCurrentCapital(currentCap, capitalChange):
    return currentCap + capitalChange

# This function will check if the user is profitable
def isProfitable(currentCap, initCap):
    return currentCap > initCap

# This function will check if the user broke even
def isBrokenEven(currentCap, initCap):
    return currentCap == initCap

# This function will display every trade
def displayTrades(display):
    return display.lower() == "yes"

# This function will simulate multiple trades and 
# output the results based on the number of trades selected
def simMultiTrades(repeat, initCap, winRate, riskRewardRatio, riskPerTrade, display):
    # Initialize the variables
    winCount = 0
    lossCount = 0
    currentCap = initCap
    longestWinStreak = 0
    longestLossStreak = 0
    currentWinStreak = 0
    currentLossStreak = 0
    maxDrawdown = 0
    maxProfitRunup = 0
    peak = initCap
    trough = initCap
    capital_history = [currentCap]

    # Looping through the number of executions
    for trade in range(repeat):
        currentRiskPerTrade = calcCurrentRiskPerTrade(riskPerTrade, currentCap)
        tradeResult = simOneTrade(winRate)
        capitalChange = calcProfitLoss(tradeResult, currentRiskPerTrade, riskRewardRatio)
        currentCap = updateCurrentCapital(currentCap, capitalChange)
        capital_history.append(currentCap)

        # Increase the win or loss count based on the trade result
        if tradeResult == "win":
            winCount += 1
            currentWinStreak += 1
            currentLossStreak = 0
            if currentWinStreak > longestWinStreak:
                longestWinStreak = currentWinStreak
        else:
            lossCount += 1
            currentLossStreak += 1
            currentWinStreak = 0
            if currentLossStreak > longestLossStreak:
                longestLossStreak = currentLossStreak

        # Calculate drawdown and run-up
        if currentCap > peak:
            peak = currentCap
        if currentCap < trough:
            trough = currentCap
        drawdown = (peak - currentCap) / peak * 100
        runup = (currentCap - trough) / trough * 100
        if drawdown > maxDrawdown:
            maxDrawdown = drawdown
        if runup > maxProfitRunup:
            maxProfitRunup = runup

        # Displaying the result of each trade if user opts for it
        if displayTrades(display):
            print("")
            print(f"----------Trade no. {trade + 1}----------")
            print(f'Current risk per trade: ${currentRiskPerTrade:,.2f}')
            print("Trade result:   ", tradeResult)
            if tradeResult == "win":
                print(f'Capital change: +${capitalChange:,.2f}')
            else:
                print(f'Capital change: -${abs(capitalChange):,.2f}')
            print(f'Current capital: ${currentCap:,.2f}')

    returnOnInvestment = (currentCap - initCap) / initCap

    # Calculating the statistics
    width = 50
  
    print('\n' + '-' * width)
    print('SIMULATION RESULTS'.center(width))
    print('-' * width)
    print(f'You won {winCount} trades'.center(width))
    print(f'You lost {lossCount} trades'.center(width))
    print("")
    print(f'Longest win streak: {longestWinStreak} trades'.center(width))
    print(f'Longest loss streak: {longestLossStreak} trades'.center(width))
    print(f'Max run-up: {maxProfitRunup:.2f}%'.center(width))
    print(f'Max drawdown: {maxDrawdown:.2f}%'.center(width))
    print("")
    print(f'Your final capital is ${currentCap:,.2f}'.center(width))
  
    if isBrokenEven(currentCap, initCap):
        print('You broke even'.center(width))
    elif isProfitable(currentCap, initCap):
        print(f'You made a profit of ${currentCap - initCap:,.2f}'.center(width))
        print(f'Your ROI is {returnOnInvestment:,.2%}'.center(width))
    else:
        print(f'You lost ${initCap - currentCap:,.2f}'.center(width))
        print(f'Your ROI is {returnOnInvestment:,.2%}'.center(width))
  
    print('-' * width + '\n')

    # Plotting the capital change over time
    plotCapitalChange(capital_history, initCap)

    # Log the results
    logStats(winCount, lossCount, initCap, winRate, riskRewardRatio, currentCap, repeat, longestWinStreak, longestLossStreak, maxDrawdown, maxProfitRunup)

# This function will plot the capital change over time
def plotCapitalChange(capital_history, initCap):
    trades = list(range(len(capital_history)))
    pct_change = [(cap - initCap) / initCap * 100 for cap in capital_history]

    fig, ax1 = plt.subplots()

    ax1.plot(trades, capital_history, 'b-')
    ax1.set_xlabel('Number of Trades')
    ax1.set_ylabel('Capital ($)', color='b')
    ax1.tick_params('y', colors='b')

    ax2 = ax1.twinx()
    ax2.plot(trades, pct_change, 'r-')
    ax2.set_ylabel('Percentage Change (%)', color='r')
    ax2.tick_params('y', colors='r')

    plt.title('Capital Change Over Number of Trades')
    plt.show()

# This function will log each multi trade simulation 
# to include the date/time and the details of the simulation
def logStats(winCount, lossCount, initCap, winRate, riskRewardRatio, currentCap, repeat, longestWinStreak, longestLossStreak, maxDrawdown, maxProfitRunup):
    file = open("log.txt", "a")

    # Create a date/time object to get the current date and time
    now = datetime.now()

    # Formatting the output of the date and time to dd/mm/YY H:M:S
    dt_string = now.strftime("%d/%m/%Y %H:%M:%S\n")
    file.write("\n\nDate and time = " + dt_string)

    # Writing the statistics to a file
    returnOnInvestment = (currentCap - initCap) / initCap
    file.write('------------SIMULATION RESULTS------------\n')
    file.write(f'You simulated {repeat} trades\n')
    file.write(f'Your strategy win rate was {winRate:.2f}%\n')
    file.write(f'Your R:R was {riskRewardRatio}\n')
    file.write(f'Your initial capital is ${initCap:,.0f}\n')
    file.write(f'You won {winCount} trades\n')
    file.write(f'You lost {lossCount} trades\n')
    file.write(f'Longest win streak: {longestWinStreak} trades\n')
    file.write(f'Longest loss streak: {longestLossStreak} trades\n')
    file.write(f'Max run-up: {maxProfitRunup:.2f}%\n')
    file.write(f'Max drawdown: {maxDrawdown:.2f}%\n')
    file.write(f'Your final capital is ${currentCap:,.2f}\n')

    if isBrokenEven(currentCap, initCap):
        file.write('You broke even\n')
    elif isProfitable(currentCap, initCap):
        file.write(f'You made a profit of ${currentCap - initCap:,.2f}\n')
        file.write(f'Your ROI is {returnOnInvestment:,.2%}\n')
    else:
        file.write(f'You lost ${initCap - currentCap:,.2f}\n')
        file.write(f'Your ROI is {returnOnInvestment:,.2%}\n')

    file.write('------------------------------------------\n')

# The main function as the point of entry
def main():
    print("")
    print('$-----------------------------------------$')
    print('| WELCOME TO THE SIMPLE TRADING SIMULATOR |')
    print('$-----------------------------------------$')
    print("")

    # The user will be prompted to enter the number of trades
    while True:
        try:
            repeat = int(input("How many trades would you want to simulate?\n>> "))
            break
        except ValueError:
            print("Invalid input. Please enter a number.")

    # The user will be prompted to enter the initial capital
    while True:
        try:
            initCap = int(input("Enter your initial capital\n>> $"))
            break
        except ValueError:
            print("Invalid input. Please enter a number.")

    # The user will be prompted to enter the win rate of strategy
    while True:
        try:
            winRate = float(input("Enter the win rate % of your strategy\n>> "))
            break
        except ValueError:
            print("Invalid input. Please enter a number.")

    # The user will be prompted to enter the risk reward ratio
    while True:
        try:
            riskRewardRatio = float(input("Enter the risk reward ratio of your strategy\n>> "))
            break
        except ValueError:
            print("Invalid input. Please enter a number.")

    # The user will be prompted to enter the risk per trade
    while True:
        try:
            riskPerTrade = float(input("Enter the % of total capital risking each trade\n>> "))
            break
        except ValueError:
            print("Invalid input. Please enter a number.")

    # The user will be prompted to enter if they want to display the trades
    while True:
        display = input("\nDo you want to display EVERY trade?\n'y' for yes\n'n' for no\n>> ")
        if display.lower() == "y" or display.lower() == "n":
            break
        else:
            print("Invalid input. Please enter yes or no.")

    # Calling the function to simulate the trades based on user's inputs
    simMultiTrades(repeat, initCap, winRate, riskRewardRatio, riskPerTrade, display)

    # The user will be asked if they want to run another simulations
    while True:
        display = input("Do you want to run another simulation?\n'y' for yes\n'n' for no\n>> ")
        if display.lower() == "y":
            main()
        elif display.lower() == "n":
            print("\nThank you for using the simple trading simulator!")
            break
        else:
            print("Invalid input. Please enter 'y' or 'n'.")

if __name__ == "__main__":
    main()
