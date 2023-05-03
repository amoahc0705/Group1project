def temperature_reading():
Maryland_temp = int(input("Enter Maryland temperature: "))
Texas_temp = int(input("Enter Texas temperature: "))
Maine_temp = int(input("Enter Maine temperature: "))
#<10 - Extremely cold
#10 - 30 - Cold
#31 - 45 - Good
#46 - 70 - Warm
#71 - 85 - Hot
#>86 - Extremely hot
def temperature_reading():
    print (Maryland_detector(Maryland_temp))
    print (Texas_detector(Texas_temp))
    print (Maine_detector(Maine_temp))
    print (Favourable(Maryland_temp,Texas_temp, Maine_temp))

def Texas_detector(Texas_temp):
    if Texas_temp <10:
        return "Texas is Extremely cold"
    elif Texas_temp >=10 and Texas_temp <=30:
        return "Texas is cold"
    elif Texas_temp >=31 and Texas_temp <=45:
        return "Texas is Good"
    elif Texas_temp >=46 and Texas_temp <=70:
        return "Texas is Warm"
    elif Texas_temp >=71 and Texas_temp <=85:
        return "Texas is Hot"
    else:
        return "Texas is Extremely hot"

def Maryland_detector(Maryland_temp) :
    if Maryland_temp < 10:
        return "Maryland is Extremely Cold"
    elif Maryland_temp >= 10 and Maryland_temp <= 30 :
        return "Maryland is Cold"
    elif Maryland_temp >=31 and Maryland_temp <= 45 :
        return "Maryland is Good"
    elif Maryland_temp >= 46 and Maryland_temp <= 70 :
        return "Maryland is Warm"
    elif Maryland_temp >=

temperature_reading()