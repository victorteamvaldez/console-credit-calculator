

# write your code here
import argparse, sys
import differentiate_calc as diff_calc
    


def error_parameters():
    sys.exit('Incorrect parameters')


#Program entry point
parser = argparse.ArgumentParser(description="Credit Calculator")
parser.add_argument('--t','--type', help="Describe the type of credit, Annuity or Diff (Differential)",
                    choices=['annuity', 'diff'])
parser.add_argument('--payment', help="The monthly pay ammount", type=int)
parser.add_argument('--interest', help="Yearly interest rate", type=float)
parser.add_argument('--periods', help="Number of months to repay", type=int)
parser.add_argument('--principal', help="Credit ammount - Principal", type=int)

args = parser.parse_args()

if len(vars(args)) < 5:
    error_parameters()

if not args.t: 
    error_parameters()
if not args.interest:
    error_parameters()

if args.t == 'diff':
    if args.payment:
        error_parameters()
    diff_calc.differentiate_payment(args)

if args.t == 'annuity':
    if not args.payment: annuity_payment()
    if not args.principal: credit_principal_calculator()
    if not args.periods: count_of_months()
