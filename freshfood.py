# Name: Matthew Weeks
# Prog Purpose: This program finds the cost of tuition & fees for PVCC students


import datetime

############### define global variables #############
# define tuition rate and fees
Tuition_IN = 155
Tuition_OUT = 331.60
INST_FEE = 1.75
STU_ACT_FEE = 2.90
CAP_FEE = 23.50

# define global variables
num_credits = 0
total = 0
scholar_amt = 0
residency = 1
balance = 0

######### define program functions ########
def main():
    more_data = True
    get_user_data()
    perform_calculations()
    display_results()
    yesno = input("\nDO you want to process more data? (Y/N) : ")
    if yesno == "no" or yesno == "N" :
        more_date = False
        print ("Thank you for using our app.") 
def get_user_data():
    global residency, num_credits, scholar_amt
    residency = int (input ("Residenct status :\nEnter; \n\t1 for In-state \n\t2 for Out-of-state  "))
    num_credits = int (input ("Number of credits: "))
    scholat_amt = int(input(" Amount of scholatship awarded: "))

def perform_calculations () :
    global tuition_amt, inst_amt, act_amt, cap_amt, total, balance
    if residency == 2: # 2 means out of state
        tuition_amt = num_credits * Tuition_OUT
        cap_amt = num_credits * CAP_FEE
    else:
        tuition_amt = num_credits * Tuition_IN
        cap_amt = 0
    
    inst_amt = num_credits * INST_FEE
    act_amt = num_credits * STU_ACT_FEE
    
    total = tuition_amt + inst_amt + act_amt + cap_amt
    balance = total - scholar_amt
    
def display_results ():
    dashes = '--------------------------------------------'
    print('--------------------------------------------')
    print('****** Piedmont Virginia College ***********')
    print('Tuition and Fees Report')
    print( str(datetime.datetime.now()))
    print(dashes)
    print('tuition   $ ' + format(tuition_amt,'2,.2f'))
    print('inst_amt  $ ' + format(inst_amt,'2,.2f'))
    print('act_amt   $ ' + format(act_amt,'2,.2f'))
    print('cap_amt   $ ' + format(cap_amt,'2,.2f'))
    print('total     $ ' + format(total,'2,.2f'))
    print('balance   $ ' + format(balance,'2,.2f' ))
    print(dashes)
    print(str(datetime.datetime.now()))

########## call on main program to execute ###########
main()
          
