def is_leap_year(year):
  if year % 4 == 0:
    if yeardef % 100 == 0:
      if year % 400 == 0:
        return True
      else:
        return False
    else:
      return True
  else:
    return False


year = int(input("enter a year"))
if is_leap_year(year):
  print(year, "is a leap year")
else:
  print(year, "is not a leap year