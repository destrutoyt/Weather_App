def identify_alerts(temp_value, wind_value, aiq_value, visibility_value):
    alerts = []

    try:
        temp_value = int(temp_value)
    except ValueError as e:
        temp_value = 0  # Provide a default value or handle as needed
        with open('log.txt', 'a') as f:
            f.write(f'\nDEBUG: Temperature value not found: {e}')
            f.close()

    try:
        wind_value = float(wind_value)
    except ValueError as e:
        wind_value = 0.0
        with open('log.txt', 'a') as f:
            f.write(f'\nDEBUG: Wind value not found: {e}')
            f.close()
    try:
        aiq_value = int(aiq_value)
    except ValueError as e:
        aiq_value = 0
        with open('log.txt', 'a') as f:
            f.write(f'\nDEBUG: Air Quality value not found: {e}')
            f.close()
    try:
        visibility_value = int(visibility_value)
    except ValueError as e:
        visibility_value = 0
        with open('log.txt', 'a') as f:
            f.write(f'\nDEBUG: Visibility value not found: {e}')
            f.close()

    # Temp Check
    if temp_value >= 30:
        alerts.append("ALERT! Temperature is above 30. Stay hydrated!")

    # Wind Check
    if wind_value >= 32.7:
        alerts.append("WARNING! Winds are high enough to threat a life. Seek shelter!")
        if wind_value >= 37.6:
            alerts.append("STORM ALERT! Winds are above 37.6m/s. Seek shelter ASAP!")
    elif 24.4 <= wind_value <= 32.7:
        alerts.append("WARNING! Winds are quite strong. Be careful outdoors!")

    # Air Quality Check
    if aiq_value >= 201:
        alerts.append("WARNING! Air quality is Very Unhealthy. Shelter is recommended!")
    elif 151 <= aiq_value <= 201:
        alerts.append("WARNING! Air quality is Unhealthy. Wear a mask!")
    elif 101 <= aiq_value <= 151:
        alerts.append("WARNING! Air quality is Unhealthy For Sensitive Groups")
    elif 51 <= aiq_value <= 101:
        alerts.append("WARNING! Air quality is Moderate")
    elif aiq_value <= 50:
        alerts.append("Air quality is good. Enjoy the fresh air!")

    # Visibility Check
    if visibility_value >= 5000:
        alerts.append("Visibility is good for most activities!")
    elif visibility_value <= 4999:
        alerts.append("WARNING! Visibility is decreasing. Avoid speeding!")
    elif visibility_value <= 1000:
        alerts.append("ALERT! Visibility is limited. Avoid driving!")

    return alerts
