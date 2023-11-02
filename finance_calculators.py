import math

# Print out the two types of calculations the user can run (investment or bond) and what these two calculations will do
print("investment - to calculate the amount of interest you'll earn on your investment")
print("bond       - to calculate the amount you'll have to pay on a home loan")

# Ask the user to input any variation of 'investment' or 'bond', and if the user doesn't input either, output an error message
user_input = input("Enter either 'investment' or 'bond' from the menu above to proceed: ")

# Convert the user input to lowercase for coding comparison
user_input_lower = user_input.lower()

# Validate user input and perform selected calculation
if user_input_lower == "investment":
    # Print out that the user has selected investment
    print("You selected 'investment'.")
    
    # Define each variable and ask the user to fill out each variable that is needed to calculate their investment
    P = float(input("Please input the amount of money that you are depositing: "))
    interest_rate = float(input("Enter the interest rate (as a percentage): "))
    
    # Convert the inputted interest rate to a usable value
    r = interest_rate / 100
    t = int(input("Enter the number of years you plan on investing: "))
    interest = input("Enter 'simple' or 'compound' interest: ")
    
    # Prompt the user to choose simple or compound interest and calculate accordingly
    if interest.lower() == "simple":
        simple_interest = P * (1 + r * t)
        print(f"You will get back {round(simple_interest, 2)}.")  # Display the calculated as a cohrent result
    elif interest.lower() == "compound":
        compound_interest = P * math.pow((1 + r), t)
        print(f"You will get back {round(compound_interest, 2)}.")  # Display the calculated as a cohrent result
    else:
        print("Invalid input. Please enter either 'simple' or 'compound'.")
    
elif user_input_lower == "bond":
    # Print out that the user has selected bond
    print("You selected 'bond'.")

    # Define each variable and ask the user to fill out each variable that is needed to calculate their bond
    P = float(input("Please input the present value of your house: "))
    annual_interest_rate = float(input("Enter the interest rate (as a percentage): "))
    
    # Convert the entered annual interest rate to a monthly interest rate
    i = (annual_interest_rate / 100) / 12
    n = int(input("Enter the number of months you plan on repaying the bond: "))
    
    # Calculate the bond repayment using the provided formula and display the result as a cohrent setence
    repayment = (i * P)/(1 - (1 + i)**(-n))
    print(f"You will have to pay {repayment} each month to pay off your house")
    
else:
    print("Invalid input. Please enter either 'investment' or 'bond' from the menu above.")

