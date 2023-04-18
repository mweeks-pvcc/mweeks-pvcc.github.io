
          
# Name: Matthew Weeks
# Prog Purpose: This program finds the cost of PIZZA!


import datetime

############### define global variables #############
# define tuition rate and fees

#        S    M     L     X     ST  
#        0    1     2     3     4    
RATES= (9.99,12.99,14.99,17.99,.55)

# define global variables
number_pizza = 0
pizza_size = ""
sales_tax = RATES[4]
total = 0

######### define program functions ########
def main():
    more_data = True
    while more_data:
        get_user_data()
        perform_calculations()
        display_results()
        yesno = input("\nDo you want to process more data? (Y/N): ")
        if yesno == "n" or yesno == "N" :
            more_data = False
            print ("Thank you for using our app.") 

def get_user_data():
    global pizza_size,number_pizza
    pizza_size = input (" \nEnter Pizza Size: \n S for Small\n M for Meduim\n L for Large\n X for Extra Large ")
    number_pizza = int(input(" How many would you like ?  "))

def perform_calculations ():
    global number_pizza, pizza_size, sales_tax, total
    rate = 0
    if pizza_size == "S" or pizza_size == "s":
        rate = RATES[0]
    if pizza_size == "M" or pizza_size == "m":
        rate = RATES[1]
    if pizza_size == "L" or pizza_size == "l":
        rate = RATES[2]
    if pizza_size == "X" or pizza_size == "x":
        rate = RATES[3]
    
    total = number_pizza * rate + sales_tax
    
def display_results ():
    dashes = '--------------------------------------------'
    print(dashes)
    print('****** Pizza ***********')
    print(' Bill')
    print( str(datetime.datetime.now()))
    print(dashes)
    print("Pizza Size           " + pizza_size )
    print("Number of Pizzas     "  +  str(number_pizza))
    print('Sales Tax            $ ' + format(sales_tax,'5,.2f'))
    print('Total                $ ' + format(total,'5,.2f'))
   
    print(dashes)
    print(str(datetime.datetime.now()))

########## call on main program to execute ###########
main()
          
