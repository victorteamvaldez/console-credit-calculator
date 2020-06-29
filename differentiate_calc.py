import math

def differentiate_payment(args):
    credit_principal = args.principal
    credit_interest = args.interest / (100*12)
    number_of_months = args.periods
    monthly_payments = []

    principal_by_month = credit_principal / number_of_months
    for month in range(1,number_of_months + 1):
        interest_by_month = credit_interest * (credit_principal - ((credit_principal * (month - 1)) / number_of_months))
        monthly_payments.append(math.ceil(principal_by_month + interest_by_month))

    for ind, ammount in enumerate(monthly_payments):
        print(f'Month {ind}: paid out {ammount}')
    print(f'Overpayment = {sum(monthly_payments) - credit_principal}')

    