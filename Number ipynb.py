seconds_in_minute = 60
minutes_in_hour = 60
seconds_in_hour = seconds_in_minute * minutes_in_hour
print(f"There are {seconds_in_hour} seconds in an hour.")
hours_in_day = 24
seconds_in_day = hours_in_day * seconds_in_hour
print(f"There are {seconds_in_day} seconds in an day.")
calculation_1 = round(float(seconds_in_hour/seconds_in_day),4)
print(f"The answer to question is (3.5) is {calculation_1} rounded to 4 decimal places.")
calculation_2 = int((seconds_in_hour//seconds_in_day))
print(f"The answer to question is (3.5) is {calculation_2}.")