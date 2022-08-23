# Solution to Problem Set 1, Part C from
# MITOPEN Python course - https://ocw.mit.edu/courses/6-0001-introduction-to-computer-science-and-programming-in-python-fall-2016/
# by Lars Saalbrink
# 21/8 2022

print("Enter the starting salary: ")
annual_salary = float(input())

total_cost = 1000000.0
semi_annual_raise = 0.07
portion_down_payment = 0.25
current_savings = 0
r = 0.04
months_for_saving = 36

monthly_salary = annual_salary / 12
target = total_cost * portion_down_payment

search_steps = 1
high = 1.0
low = 0.0
saving_rate_guess = (high + low) / 2.0
poverty_flag = 0
#print("Guess number ",search_steps,": ",saving_rate_guess)
current_savings = 0
for m in range(0,months_for_saving):
  current_savings += monthly_salary * saving_rate_guess + ((current_savings * r)/12)
  if(not m % 6):
    monthly_salary *= (1.0 + semi_annual_raise)

#print("\nSavings: ",current_savings,"\n")

while((target > (current_savings+50)) or (target < (current_savings-50))):
  if(saving_rate_guess >= 0.9999):
    print("It is not possible to pay the down payment in three years.")
    poverty_flag = 1
    break

  #print("target: ",target,"\n")
  if(target > current_savings):
    #print("Øger")
    low = saving_rate_guess
  else:
    #print("Sænker")
    high = saving_rate_guess
  saving_rate_guess = (high + low) / 2.0

  search_steps += 1
  #print("Guess number ",search_steps,": ",saving_rate_guess)
  current_savings = 0
  monthly_salary = annual_salary / 12
  for m in range(0,months_for_saving):
    current_savings += monthly_salary * saving_rate_guess + ((current_savings * r)/12)
    if(not m % 6):
      monthly_salary *= (1.0 + semi_annual_raise)
  
  #print("\nSavings: ",current_savings,"\n")

if(not poverty_flag):
  print("Best savings rate: ",saving_rate_guess)
  print("Steps in bisection search: ",search_steps)


