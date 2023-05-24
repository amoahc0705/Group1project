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