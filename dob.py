# Write your code here :-)
from datetime import date

def get_dob():
    dob = input("DoB [yyyymmdd]: ")
    if int(dob) < 10000000:
        raise RuntimeError("Invalid date of birth")
    yyyy = dob[:4]
    mm = dob[4:6]
    dd = dob[6:]
    return int(yyyy), int(mm), int(dd)

def get_today():
    today = date.today()
    tyear = today.year
    tmonth = today.month
    tday = today.day
    return tyear, tmonth, tday

def calculate_age(dob, today):
    #
    # Unpack the dob & today into
    # individual elements
    #
    year, month, day = dob
    tyear, tmonth, tday = today

    age = tyear - year
    if tmonth >= month:
        if tmonth == month:
            if tday < day:
                age -= 1
            elif tday == day:
                print("Congratulations!")
    else:
        age -= 1

    return age

dob = get_dob()
today = get_today()
age = calculate_age(dob, today)
print("You are", age, "years old")