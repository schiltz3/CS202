def future():
    print("THis program calculates the furture value of a 10-year investment")

    principal = eval(input("Enter the initial principal: "))
    apr = eval(input("Enter the annual interest rate: "))

    principal = principal * (1 + apr) ** 10

    print("The value in 10 years is:", principal)
