def main():
    print("this program convert US dollers to Pounds Sterling")
    print()

    dollars =eval(input("enter amount in dollars : "))
    pound = convert_to_pounds(dollars)
    print("this is : ",pound," pounds.")
convert_to_pounds = lambda dollers:dollers*0.82
main()    
