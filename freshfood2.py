# Name: Matthew Weeks
# Prog Purpose: This program finds the pay for Fresh Food employees


import datetime

############### define global variables #############
# define tuition rate and fees

#        C    S      J    M     FED  ST SS    MED
#        0    1     2     3     4    5  6     7 
RATES = (16.5,15.75,15.75,19.5,.12,.03,.062,.145)

# define global variables
hours_worked = 0
job_code = ""
gross_pay = 0
fed_amt = 0
state_amt = 0
social_sec_amt = 0
med_amt = 0
total_ded = 0
net_pay = 0

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
    global job_code,hours_worked
    job_code = input (" \nEnter job code: \n C for Cashier\n S for Stocker\n J for Janitor\n M for Maintenance ")
    hours_worked= int(input(" How many hours did employee work?  "))

def perform_calculations ():
    global gross_pay, fed_amt, state_amt, social_sec_amt, med_amt, total_ded, net_pay
    rate = 0
    if job_code == "C" or job_code == "c":
        rate = RATES[0]
    if job_code == "S" or job_code == "s":
        rate = RATES[1]
    if job_code == "J" or job_code == "j":
        rate = RATES[2]
    if job_code == "M" or job_code == "m":
        rate = RATES[3]
    
    gross_pay = hours_worked * rate
    fed_amt = gross_pay * RATES[4]
    state_amt = gross_pay * RATES[5]
    social_sec_amt = gross_pay * RATES[6]
    med_amt = gross_pay * RATES[7]
    total_ded = fed_amt + state_amt + social_sec_amt + med_amt
    net_pay = gross_pay - total_ded
    
def display_results ():
    dashes = '--------------------------------------------'
    print(dashes)
    print('****** Fresh Foods ***********')
    print(' Paycheck')
    print( str(datetime.datetime.now()))
    print(dashes)
    print('Gross pay           $ ' + format(gross_pay,'10,.2f'))
    print('Federal income Tax  $ ' + format(fed_amt,'10,.2f'))
    print('State income Tax    $ ' + format(state_amt,'10,.2f'))
    print('Social Security Tax $ ' + format(social_sec_amt,'10,.2f'))
    print('Medicare            $ ' + format(med_amt,'10,.2f'))
    print('Total Deductions    $ ' + format(total_ded,'10,.2f' ))
    print('Net Pay             $ ' + format(net_pay,'10,.2f' ))
    print(dashes)
    print(str(datetime.datetime.now()))

########## call on main program to execute ###########
main()
          
