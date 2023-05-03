def Maryland_detector(Maryland_temp) :
    if Maryland_temp < 10:
        return "Maryland is Extremely Cold"
    elif Maryland_temp >= 10 and Maryland_temp <= 30 :
        return "Maryland is Cold"
    elif Maryland_temp >=31 and Maryland_temp <= 45 :
        return "Maryland is Good"
    elif Maryland_temp >= 46 and Maryland_temp <= 70 :
        return "Maryland is Warm"
    elif Maryland_temp >=71 and Maryland_temp <= 85 :
        return "Maryland is Hot"
    else:
        return "Maryland is Extremely Hot"
