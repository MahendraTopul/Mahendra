# Reverse a string and print it on console "Python Skills".
 
str = "Python Skills"
print(" Before reversing string: ",str)

str = str[::-1]
print(" After reversing string: ",str)

# Assign string to x variable in DD-MM-YYYY format
# Extract and print year from string.

x = "30-7-2003"

print(x[6:])

#In a small company, the average salary of three employees is Rs1000 per week.
# If one employee earns Rs1100 and other earns Rs500, how much will the third employee earn

average = 1000
e1 = 1100
e2 = 500

e3 = (average -(e1+e2)/3)*3

print("Salary of third employee is",e3)

# Write a program Convert a percentage to a fraction (To convert a percentage into fraction let say 30% to a fraction)

per = 70

Fraction = per / 100

print("Fraction of",per,"is",Fraction)
print(Fraction)

# write program -A train 340 m long is running at a speed of 45 km/hr.
# what time will it take to cross a 160 m long tunnel?

tunnel = 160

speed = 45000 / 3600

distance = 340 + 160

time = distance / speed

print("Time required to cross a tunnel is",time)