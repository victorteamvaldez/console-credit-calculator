

# write your code here
import math

def count_of_months(args):
    credit_principal = args.principal
    monthly_payment = args.payment
    credit_interest = args.interest / (100*12)
    
    value = monthly_payment / (monthly_payment - (credit_interest * credit_principal))
    number_of_months = math.ceil(math.log(value, 1+credit_interest))
    
    years = int(number_of_months / 12)
    months = number_of_months % 12
    
    if(years > 1 and months > 1):
        print(f'You need {years} years and {months} months to repay this credit!')
    elif(years > 1 and months == 0):
        print(f'You need {years} years to repay this credit!')
    elif(years == 1 and months == 0):
        print(f'You need {years} year to repay this credit!')
    elif(years == 1 and months > 1):
        print(f'You need {years} year and {months} months to repay this credit!')
    elif(years == 1 and months == 1):
        print(f'You need {years} year and {months} month to repay this credit!')
    elif(years == 0 and months > 1):
        print(f'You need {months} months to repay this credit!')
    elif(years == 0 and months == 1):
        print(f'You need {months} month to repay this credit!')

    print(f'Overpayment = {(number_of_months * monthly_payment) - credit_principal}')

def annuity_payment(args):
    credit_principal = args.principal
    number_of_months = args.periods
    credit_interest = args.interest / (100*12)
    interest_factor = math.pow((1 + credit_interest), number_of_months)
    annuity = math.ceil(credit_principal * ((credit_interest * interest_factor) / (interest_factor - 1)))
    print(f'Your annuity payment = {annuity}!')
    print(f'Overpayment = {(number_of_months * annuity) - credit_principal}')
    
    

def credit_principal_calculator(args):
    annuity_payment = args.payment
    number_of_months = args.periods
    credit_interest = args.interest / (100*12)
    
    interest_factor = math.pow(1 + credit_interest, number_of_months)
    credit_principal = math.floor(annuity_payment / ((credit_interest * interest_factor) / (interest_factor - 1)))
    print(f'Your credit principal = {credit_principal}!')
    print(f'Overpayment = {(annuity_payment * number_of_months) - credit_principal}')
    
    

