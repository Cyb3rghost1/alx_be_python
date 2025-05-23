monthlyIncome= int(input("Enter your monthly income: "))
monthlyExpenses= int(input("Enter your total monthly expenses: "))

monthlySavings = monthlyIncome - monthlyExpenses

annualInterestRate =0.05
projectedSavings = int(monthlySavings * 12 + (monthlySavings * 12 * annualInterestRate))
PS = f"${projectedSavings}."
MS = f"${monthlySavings}."
print("Your projected savings is", MS) 
print("Projected savings after one year, with interest, is:", PS)
