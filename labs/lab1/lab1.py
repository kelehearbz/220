def interest():
    rate = eval(input("Hello! Please enter your annual interest rate. "))
    cycle = eval(input("How many days are in your billing cycle? "))
    day = eval(input("What day of that cycle did you make your payment? "))
    balance = eval(input("Great! Please enter your previous net balance. "))
    payment = eval(input("Please enter your payment amount."))

    days_before_end = cycle - day
    step1 = balance * cycle
    step2 = payment * days_before_end
    step3 = step1 - step2
    step4 = step3 / cycle

    average_daily_balance = step4
    monthly_interest_rate = rate / 12
    monthly_interest_charge = average_daily_balance * monthly_interest_rate

    print("Your monthly interest charge is ", monthly_interest_charge, " Have a great day! :)")
