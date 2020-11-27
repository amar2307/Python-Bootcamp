#If the bill was $150.00, split between 5 people, with 12% tip. 
#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60
#Tip: You might need to do some research in Google to figure out how to do this.

print("Welcome to the Tip Calculator!")
bill=float(input("What was the total bill? $"))
tip=int(input("What percentage tip would you like to give? "))
num_people=int(input("How many people to split the bill? "))

tip_perc=tip/100
total_tip=bill*tip_perc
total_bill=bill+total_tip
share=round(total_bill/num_people,2)

print(f"Each person should pay: ${share}")
