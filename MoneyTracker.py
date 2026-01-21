# Value trackers [total_spent, income, fuel, food, needs, wants]
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
## Main loop

class main:
    ## check for load

    ## setup loop
        ## Display functions

        ## ask for input

        ## validate input

        ## run functionality
    
    ## if quit save then quit