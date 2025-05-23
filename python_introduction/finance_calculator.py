monthlyIncome= int(input("Enter your monthly income: "))
monthlyExpenses= int(input("Enter your total monthly expenses: "))

monthlySavings = monthlyIncome - monthlyExpenses

annualInterestRate =0.05
projectedSavings = monthlySavings * 12 + (monthlySavings * 12 * annualInterestRate)
print("Your projected savings is ", monthlySavings) 
print("Projected savings after one year, with interest, is: ", projectedSavings)