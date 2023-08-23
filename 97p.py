y = int(input("Enter the year:\n"))

if y % 4 == 0 and y % 100 != 0 or y % 400 == 0:
    print("Your year is a leap year :)")
else:
    print("Your year is not a leap year :)")