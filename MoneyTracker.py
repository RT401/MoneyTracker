#####
## Saving requirements
import json
import os
fileName = "MoneyTracker.txt"

#####
## Value trackers [total_spent, income, fuel, food, needs, wants]
weekly_Spent = []
monthly_Spent = []
yearly_Spent = []

#####
## Basic Add to values functions
def Add_Val(location, val):
    if(location > 1):
        Add_Val(0, val)
    
    weekly_Spent[location] += val
    monthly_Spent[location] += val
    yearly_Spent[location] += val

def add_paycheck(val):
    Add_Val(1, val)

def fuel_Spent(val):
    Add_Val(2, val)
    
def food_Spent(val):
    Add_Val(3, val)

def needs_Spent(val):
    Add_Val(4, val)

def wants_Spent(val):
    Add_Val(5, val)
    
#####
## Function to reset the spends on week changes
def set_Payday(date):
    # setup live date functionality
    return

def update_week():
    weekly_Spent.clear

def update_Month():
    monthly_Spent.clear

def update_Year():
    yearly_Spent.clear


#####
## Save and load functionality
def save():
    data = {
        "weekly_Spent": weekly_Spent,
        "monthly_Spent": monthly_Spent,
        "yearly_Spent": yearly_Spent
    }
    
    if not os.path.exists(fileName):
        # Create the file
        with open(fileName, "w") as file:
            json.dump(data, file)
        print(f"File '{fileName}' created and saved.")
    else:
        # Overwrite existing file
        with open(fileName, "w") as file:
            json.dump(data, file)
        print(f"File '{fileName}' updated.")

def load():
    with open(fileName, "r") as file:
        data = json.load(file)

    return(
        data.get("weekly_Spent", []),
        data.get("monthly_Spent", []),
        data.get("yearly_Spent", [])
    )

#####
## Main loop

class main:
    ## check for load
    load()

    ## setup loop
    main_Loop = True
    if(main_Loop == True):
        ## Display functions

        ## ask for input

        ## validate input

        ## run functionality
        main_Loop = False
    
    ## if quit save then quit
    save()
    quit()