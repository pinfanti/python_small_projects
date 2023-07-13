# Defining if it is a leap year or not:
def is_leap(year):
  if year % 4 == 0:
    if year % 100 == 0:
      if year % 400 == 0:
        return True
      else:
        return False
    else:
      return True
  else:
    return False

# Function to check how many days in a year:
def days_in_month(given_year, given_month):
  month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31] 
  month_days_leap = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]  
  if given_month > 12 or given_month < 1:
      return "invalid information (month)"
  elif is_leap(given_year) == True:
    final_leap_day = month_days_leap[given_month-1]
    return final_leap_day
  else:
    final_day = month_days[given_month-1]
    return final_day

# Get user info and return to the user how many days there is in that month of that year:  
print("Please insert numbers when asked about the year and month to not break the program")
year = int(input("Enter a year (integer): "))
month = int(input("Enter a month (integer 1-12): "))
days = days_in_month(year, month)
print(f"There are {days}")
