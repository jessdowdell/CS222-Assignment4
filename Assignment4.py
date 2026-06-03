import requests

#This is the first web service endpoint for Muncie, IN using lat and long.
points_url = "https://api.weather.gov/points/40.1934,-85.3864"

#Sends request to the first URL and gets JSON data
response = requests.get(points_url)
data = response.json()

# This is the second web service endpoint 
# Gets forcast URL from inside the properties section
forecast_url = data["properties"]["forecast"]

# Sends request to forecast URl and gets JSON data
forecast_response = requests.get(forecast_url)
forecast_data = forecast_response.json()

# Gets the list of forecast periods
periods = forecast_data["properties"]["periods"]

# Loop through all 14 forecast periods
for period in periods:

    # Displays the name of the forecast period
    print("Name: ", period["name"])

    # Displays the temperature
    print("Temperature: ", period["temperature"])

    # Displays the detailed forecast
    print("Forecast: ", period["detailedForecast"])
    # Prints a blank line between forecasts
    print()

