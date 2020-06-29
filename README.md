# console-credit-calculator

Is a credit calculator using CLI

Examples: 

Input: python calculator.py --type=diff --principal=1000000 --periods=10 --interest=10

Output:

Month 1: paid out 108334
Month 2: paid out 107500
Month 3: paid out 106667
Month 4: paid out 105834
Month 5: paid out 105000
Month 6: paid out 104167
Month 7: paid out 103334
Month 8: paid out 102500
Month 9: paid out 101667
Month 10: paid out 100834
 
Overpayment = 45837

Input: python calculator.py --type=annuity --principal=1000000 --periods=60 --interest=10

Output:

Your annuity payment = 21248!
Overpayment = 274880

Try:
python calculator.py --help
