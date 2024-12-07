def main():
    print("this is a monthly payment loan calculator")
    print("")
    principle=float(input("loan of amount : "))
    apr =float(input("kitna laga annual interest rate : "))
    years=int(input("amount of years : "))
   
    monthly_interst_rate = apr / 1200 
    amount_of_month = years * 12
    monthly_payment = principle*monthly_interst_rate /(1-(1 + monthly_interst_rate)**(-amount_of_month))


    print("the monthly payment for this loan is : %.2f" % monthly_payment)
main()    
