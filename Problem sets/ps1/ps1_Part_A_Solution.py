# Solution to Problem Set 1, Part A from
# MITOPEN Python course - https://ocw.mit.edu/courses/6-0001-introduction-to-computer-science-and-programming-in-python-fall-2016/
# by Lars Saalbrink
# 21/8 2022

print("Enter your annual salary: ")
annual_salary = float(input())
print("Enter the percent of your salary to save, as a decimal: ")
portion_saved = float(input())
print("Enter the cost of your dream home: ")
total_cost = float(input())

portion_down_payment = 0.25
current_savings = 0
r = 0.04
monthly_salary = annual_salary / 12

target = total_cost * portion_down_payment

number_of_months = 0
while(current_savings < target):
  number_of_months += 1
  current_savings += monthly_salary * portion_saved + ((current_savings * r)/12)

print("\nNumber of months: ",number_of_months)
