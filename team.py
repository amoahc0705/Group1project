# <10 - Extremely cold
# 10 - 30 - cold
# 31 - 45 - good
# 46 - 70 - warm
# 71 - 85 - Hot
# >86 - Extremely hot
def temperature_reading():
    Maryland_temp = int(input("Enter maryland temperature: "))
    Texas_temp = int(input("Enter Texas temperature: "))
    Maine_temp = int(input("Enter Maine temperature: "))

    print(temperature_detector("Maryland", Maryland_temp))
    print(temperature_detector("Texas", Texas_temp))
    print(temperature_detector("Maine", Maine_temp))
    print(favourable(Maryland_temp, Texas_temp, Maine_temp))
def temperature_detector(state_name, temperature):
    if temperature < 10:
        return state_name + "is extremely cold"
    elif temperature >=10 and temperature <= 30:
        return state_name + "is cold"
    elif temperature >=31 and temperature <=45:
        return state_name + "is good"
    elif temperature >=46 and temperature <=70:
        return state_name + "is warm"
    elif temperature >=71 and temperature <=85:
        return state_name + "is hot"
    else:
        return "Texas is Extremely Hot"
def favourable(Maryland_temp, Texas_temp, Maine_temp):
    if Maryland_temp >=50 and Maryland_temp<=70 and Texas_temp >=50 and Texas_temp<=70 and Maine_temp>=50 and Maine_temp<=70:
        return min(Maine_temp, Texas_temp, Maine_temp), "is most favourable"
    elif Maryland_temp >=50 and Maryland_temp <=70:
        return "Maryland is most favourable"
    elif Texas_temp >=50 and Texas_temp <=70:
        return "Texas is most favourable"
    elif Maine_temp >=50 and Maine_temp <=70:
        return "Maine is most favourable"
    else:
        return "Dial 911 for Help!"
temperature_reading()