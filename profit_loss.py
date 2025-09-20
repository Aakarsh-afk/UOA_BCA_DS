# In this program we'll calculate the profit or loss, principal amount, rate of interest, simple interest, compound interest, and time period.

def calculate_simple_interest():
    principal = float(input("Enter the principal amount: "))
    rate = float(input("Enter the rate of interest (in %): "))
    time = float(input("Enter the time period (in years): "))
    
    simple_interest = (principal * rate * time) / 100
    total_amount = principal + simple_interest
    
    print(f"Simple Interest: {simple_interest}")
    print(f"Total Amount after {time} years: {total_amount}")

def calculate_compound_interest():
    principal = float(input("Enter the principal amount: "))
    rate = float(input("Enter the rate of interest (in %): "))
    time = float(input("Enter the time period (in years): "))
    n = float(input("Enter the number of times interest is compounded per year: "))
    
    total_amount = principal * ((1 + rate / (100 * n))**(n*time))
    compound_interest = total_amount - principal

    print(f"Compound Interest: {compound_interest}")
    print(f"Total Amount after {time} years: {total_amount}")

def calculate_profit_loss():
    cost_price = float(input("Enter the cost price: "))
    selling_price = float(input("Enter the selling price: "))
    
    if selling_price > cost_price:
        profit = selling_price - cost_price
        print(f"Profit: {profit}")
    elif cost_price > selling_price:
        loss = cost_price - selling_price
        print(f"Loss: {loss}")
    else:
        print("No profit, no loss.")

def rate_of_interest():
    principal = float(input("Enter the principal amount: "))
    time = float(input("Enter the time period (in years): "))
    interest = float(input("Enter the interest amount: "))
    
    rate = (interest * 100) / (principal * time)
    print(f"Rate of Interest: {rate}%")

def time_period():
    principal = float(input("Enter the principal amount: "))
    rate = float(input("Enter the rate of interest (in %): "))
    interest = float(input("Enter the interest amount: "))
    
    time = (interest * 100) / (principal * rate)
    print(f"Time Period: {time} years")

def principal_amount():
    rate = float(input("Enter the rate of interest (in %): "))
    time = float(input("Enter the time period (in years): "))
    interest = float(input("Enter the interest amount: "))
    
    principal = (interest * 100) / (rate * time)
    print(f"Principal Amount: {principal}")

choice = input("Choose an option:\n1. Simple Interest\n2. Compound Interest\n3. Profit/Loss\n4. Rate of Interest\n5. Time Period\n6. Principal Amount\nEnter your choice (1-6): ")

if choice == '1':
    calculate_simple_interest()
elif choice == '2':
    calculate_compound_interest()
elif choice == '3':
    calculate_profit_loss()
elif choice == '4':
    rate_of_interest()
elif choice == '5':
    time_period()
elif choice == '6':
    principal_amount()
else:
    print("Invalid choice. Please select a valid option.")