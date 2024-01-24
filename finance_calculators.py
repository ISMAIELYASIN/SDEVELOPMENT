import math

#user inputs either investment or bond
investment_bond = input(str("Enter either Investment or Bond:\n" )).lower()

#if user inputs investment the prompts user to enter amouts for calculation
if investment_bond == "investment":

        
        pr = float(input("Enter amount for investment:\n"))

        rate = float(input("Enter interest rate: \n" ))

        r = (rate/100)

        time = float(input("Enter investment in years: \n"))

        simple_compound = str(input("Select 'Simple' or 'Compound' interest. \n")).lower()

if      simple_compound == "simple":

        simple_compound = pr*(1 + r * time)

        total = simple_compound

        print (f"Interest earned over {time} years: {total:.2f}".format())

elif    simple_compound == "compound":

        simple_compound = pr*math.pow((1+r),time)

        total = simple_compound

        print (f"Interest earned over {time} years: {total:.2f}".format())

#if user inputs investment the prompts user to enter amouts for calculation
elif investment_bond == "bond":


        pri = float(input("Enter value of the house: \n"))

        intr = float(input("Enter interest rate: \n" ))

        i = ((intr/100)/12)/12

        no = float(input("Enter the duration in months: \n"))

        monthly = float(math.floor((i*pri)/(1 - (1+i)**(-no))))

        print(f"Monthly repayment: {monthly:.2f}".format())

#no classification
else:

        print("Enter a valid input.")