def identify_alerts(temp_value, wind_value, aiq_value, visibility_value):
    alerts = []
    try:
        temp_value = int(temp_value)
    except ValueError:
        temp_value = 0  # Provide a default value or handle as needed

    try:
        wind_value = float(wind_value)
    except ValueError:
        wind_value = 0.0  # Provide a default value or handle as needed

    try:
        aiq_value = int(aiq_value)
    except ValueError:
        aiq_value = 0  # Provide a default value or handle as needed

    try:
        visibility_value = int(visibility_value)
    except ValueError:
        visibility_value = 0  # Provide a default value or handle as needed

    if temp_value >= 30:
        alerts.append("ALERT! Temperature is above 30. Stay hydrated!")
    else:
        alerts.append("Stay hydrated and don't forget your umbrella!")
    if wind_value <= 24.4:
        alerts.append("Winds are low! Enjoy the weather!")
    elif wind_value >= 24.5:
        alerts.append("WARNING! Winds could be dangerous for some outdoor activities!")
    elif wind_value >= 32.7:
        alerts.append("WARNING! Winds is high enough to threat a life. Seek shelter!")
    else:
        alerts.append("STORM ALERT! Winds is above 37.6m/s. Seek shelter ASAP!")
    if aiq_value <= 50:
        alerts.append("Air quality is good. Enjoy the fresh air!")
    elif aiq_value >= 51:
        alerts.append("WARNING! Air quality is Moderate")
    elif aiq_value >= 101:
        alerts.append("WARNING! Air quality is Unhealthy For Sensitive Groups")
    elif aiq_value >= 151:
        alerts.append("WARNING! Air quality is Unhealthy. Wear a mask!")
    elif aiq_value >= 201:
        alerts.append("WARNING! Air quality is Very Unhealthy. Shelter is recommended!")
    elif aiq_value == 0:
        alerts.append("No Air Quality Data Reported")
    else:
        alerts.append("ALERT! Air quality is considered a hazard. Seek shelter and wear a mask!")
    if visibility_value >= 5000:
        alerts.append("Visibility is good for most activities!")
    elif visibility_value <= 4999:
        alerts.append("WARNING! Visibility is decreasing. Avoid speeding!")
    elif visibility_value <= 1000:
        alerts.append("ALERT! Visibility is limited. Avoid driving!")
    elif visibility_value == 0:
        alerts.append("No Visibility Data Reported")
    else:
        alerts.append("ALERT! Extremely poor visibility detected. DO NOT DRIVE OR GO OUTSIDE!")

    return alerts
