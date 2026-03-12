#Author: Aynura Erejepbaeva
#Date: Jan 19, 2026
#Purpose: How Rich Am I? For Brutus

BRUTUS_INTEREST_RATE = 1.05 #calculated
total_interest = 0 #global value

def my_wealth():
    INITIAL_DEPOSIT = 1 #Brutus had one dollar
    total_wealth = INITIAL_DEPOSIT
    year = 0 #from year 0 to 2023
    while year < 2023:
        total_wealth = total_wealth*1.05
        total_interest = total_wealth - INITIAL_DEPOSIT
        year = year + 1

    print("Total interest ", total_interest)
    print("Total wealth", total_wealth)

my_wealth()