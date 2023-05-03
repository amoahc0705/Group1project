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


def Maine_detector(Maine_temp):
    if Maine_temp <10:
        return "Maine is Extremely cold"
    elif Maine_temp >=10 and Maine_temp <=30:
        return "Maine is cold"
    elif Maine_temp >=31 and Maine_temp <=45:
        return "Maine is good"
    elif Maine_temp >=46 and Maine_temp <= 70:
        return "Maine is warm"
    elif Maine_temp >=71 and Maine_temp <= 85:
        return "Maine is hot"
    else:
        return "Maine is extremely  Hot"
    def favourable(Maryland_temp, Texas_temp, Maine_temp):
        if Maryland_temp >=50 and Maryland_temp <=70 and Texas_temp >=50 and Texas_temp <=70 and Maine_temp>=50 and Maine_temp<=70:
            return min(Maryland_temp, Texas_temp, Maine_temp), "is most favourable"
        elif Maryland_temp>=50 and Maryland_temp <=70:
            return "Maryland is  most favourable"
        elif Texas_temp >=50 and Texas_temp <=70:
            return "Texas is most favourable"
        elif Maine_temp >=50 and Maine_temp <= 70:
            return "Maine is most favourable"
        else:
            return "Dial 911 for Help!"