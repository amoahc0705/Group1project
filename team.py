def Texas_detector(Texas_temp):
    if Texas_temp <10:
        return "Texas is Extremely cold"
    elif Texas_temp >=10 and Texas_temp <=30:
        return "Texas is cold"
    elif Texas_temp >=31 and Texas_temp <=45:
        return "Texas is good"
    elif Texas_temp >=46 and Texas_temp <=70:
        return "Texas is warm"
    elif Texas_temp >=71 and Texas_temp <=85:
        return "Texas is hot"
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
