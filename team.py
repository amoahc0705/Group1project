def temperature_detector(state_name, temperature):
    if temperature <10:
        return state_name + "is Extremely cold"
    elif temperature >=10 and temperature <=30:
        return state_name+ "is cold"
    elif state_name >=31 and temperature <=45:
        return state_name + "is good"
    elif temperature >=46 and temperature <=70:
        return state_name + "is warm"
    elif temperature >=71 and temperature <=85:
        return state_name + "is hot"
    else:
        return state_name +"is Extremely Hot"