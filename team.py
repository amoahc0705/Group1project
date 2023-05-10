
def favourable(Maryland_temp, Texas_temp, Maine_temp):
    if Maryland_temp >= 50 and Maryland_temp <=70 and Texas_temp >=50 and Texas_temp <= 70 and Maine_temp >=50 and Maine_temp <=70:
        if Maryland_temp < Texas_temp and Maryland_temp < Maine_temp:
            return "Maryland is most favourable"
        elif Texas_temp < Maryland_temp and Texas_temp < Maine_temp:
            return "Texas is most favourable"
        else:
            return "Maine is most favourable"
    elif Maryland_temp >=50 and Maryland_temp <=70:
        return "Maryland is most favourable"
    elif Texas_temp >=50 and Texas_temp <=70:
        return "Texas is most favourable"
    elif Maine_temp >=50 and Maine_temp <=70:
        return "Maine is most favourable"
    else:
        return "Dial 911 for help!"
