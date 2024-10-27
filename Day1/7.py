days = int(input("Enter the days: "))
years = days// 365
weeks = (days-(365*years))// 7
day = (days - (365*years)-(7*weeks))
print(f"{days} consist {years} years, {weeks} weeks, {day} days")

