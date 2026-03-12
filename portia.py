#Author: Aynura Erejepbaeva
#Date: Jan 19, 2026
#Purpose: How Rich Am I? Comparing Brutus' wealth to Portia

BRUTUS_INTEREST_RATE = 1.05
total_interest_brutus = 0
PORTIA_INTEREST_RATE = 1.04
total_interest_portia = 0

def my_wealth():
    INITIAL_DEPOSIT_BRUTUS = 1
    total_wealth_brutus = INITIAL_DEPOSIT_BRUTUS

    INITIAL_DEPOSIT_PORTIA = 100000 #how much money Portia started with
    total_wealth_portia = INITIAL_DEPOSIT_PORTIA

    year = 0
    while total_wealth_brutus <= total_wealth_portia:
        total_wealth_brutus = total_wealth_brutus*1.05
        total_interest_brutus = total_wealth_brutus - INITIAL_DEPOSIT_BRUTUS

        total_wealth_portia = total_wealth_portia*1.04
        total_interest_portia = total_wealth_portia - INITIAL_DEPOSIT_PORTIA

        year = year + 1 #one year for both persons

    print("Total interest for Brutus", total_interest_brutus)
    print("Total wealth for Brutus", total_wealth_brutus)

    print("Total interest for Portia", total_interest_portia)
    print("Total wealth for Portia", total_wealth_portia)

    print("Year", year)

my_wealth()