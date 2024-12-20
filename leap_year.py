def is_leapyear(year):
    if (year%4==0 and year%100!=0) or year%400==0 :
        return "Leap year"
    return "Not a Leap year"
year=int(input("Enter year"))
print(is_leapyear(year))
