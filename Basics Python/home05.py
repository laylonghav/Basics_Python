day_number = int (input("Enter a number from 1 to 6 : "))

day_name = ["Sunday","Monday","Turesday","Wednesday","Friday","Santurday"]

if 1<= day_number<=7:
    day_name = day_name[day_number-1]
    print(f"The day corresponding to {day_number}is {day_name}")
else:
    print("Invalid input. Please enter a number from 1 to 7.")    