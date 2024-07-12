
# MOJE ŘEŠENÍ
print("Vítejte v aplikaci na určování přestupného roku")
year = int(input("Zadejte rok, který chcete zkontrolovat:\n"))
month = input("Zadejte měsíc u kterého chcete zjistit počet dnů:\n")

def prestupny_rok(rok):
  if rok % 4 == 0:
    if rok % 100 == 0:
      if rok % 400 == 0:
        return f"Rok {rok} je přestupný"
      else:
        return f"Rok {rok} není přestupný"
    else:
      return f"Rok {rok} je přestupný"
  else:
    return f"Rok {rok} není přestupný"

year_result = prestupny_rok(year)

days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
list_of_month = ["leden", "únor", "březen", "duben", "květen", "červen", "červenec", "srpen", "září", "říjen", "listopad", "prosinec"]

if "je přestupný" in year_result:
  days_in_month[1] = 29

if month in list_of_month:
    index = list_of_month.index(month)

days = days_in_month[index] 

print(f"{year_result} a měsíc {month} má {days} dnů.")

# #ŘEŠENÍ DAVIDA ŠETKA

# def leap(user_year):
#   if user_year % 4 == 0:
#     if user_year % 100 == 0:
#       if user_year % 400 == 0:
#         return True
#       else:
#         return False
#     else:
#       return True
#   else:
#     return False

# def days(user_year, user_month):
#   days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
#   leap_result = leap(user_year)
#   if leap_result == True and user_month == 2:
#     return 29
#   else:
#     return days_in_month[user_month - 1]

# year = int(input("Zadejte rok, který chcete zkontrolovat:\n"))
# month = int(input("Zadejte měsíc u kterého chcete zjistit počet dnů:\n"))
# result = days(year, month)
# print(f"Počet ve zvoleném měsíci je: {result}")