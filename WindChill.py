"""
    @Author: Afroz Basha
    @Date: 2021-08-24
    @Title: Finding Wind chill
"""
"""
Description:
    Using  Try & Except 
Parameter:
    windChill = 35.74 + 0.6215 * temperature + (0.4275 * temperature - 35.75) * pow(windSpeed, 0.16)
Return:
      It returns Wind Chill Value.
"""

try:
    """Finding Wind chill"""
    temp = int(input("Enter the Temperature '0' to '50' : "))
    if (temp >= 0) and (temp <= 50):
        windSpeed = int(input("Enter the Wind Speed '3' to '120' : "))
        if (windSpeed >= 3) and (windSpeed <= 120):
            windChill = 35.74 + 0.6215 * temp + (0.4275 * temp - 35.75) * pow(windSpeed, 0.16)
            print("Temperature = ", temp)
            print("Wind speed  = ", windSpeed)
            print("Wind chill  = ", windChill)
        else:
            print("Enter the Valid Wind Speed (3 to 120)")
    else:
        print("Enter the Valid Temperature (0 to 50)")
except ValueError:
    print("Please give the Valid input from given range")
