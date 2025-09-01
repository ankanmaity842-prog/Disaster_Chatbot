def get_context(user_input):
    if "earthquake" in user_input.lower():
        return "You are a disaster management expert helping students prepare for earthquakes."
    elif "flood" in user_input.lower():
        return "You are a disaster management expert helping students prepare for floods."
    elif "fire" in user_input.lower():
        return "You are a disaster management expert helping students prepare for fires."
    elif "cyclone" in user_input.lower():
        return "You are a disaster management expert helping students prepare for cyclone."
    else:
        return "You are a general disaster preparedness assistant for students."