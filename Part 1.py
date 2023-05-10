#<10 - Extemely cold
#10 - 30 - cold
#31 - 45 - good
#46 - 70 - Warm
#71 - 85 - Hot
#>86 - Extremly hot
def temperature_reading():
    Maryland_temp = int(input("Enter Maryland temperature"))
    Texas_temp = int(input("Enter Texas temperature"))
    Maine_temp = int(input("Enter Maine temperature"))

    print(temperature_dector("Maryland, Maryland_temp"))
    print(temperature_detector("Texas, Texas_temp"))
    print(temperature_detector("Maine, Maine_temp"))
    print(favourable(Maryland_temp,Texas_temp,Maine_temp))






temperature_reading()
