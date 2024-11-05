from flask import Flask, render_template, request
import requests
from datetime import datetime

app = Flask(__name__)

# Replace with your actual Open Exchange Rates app_id
OPEN_EXCHANGE_APP_ID = '5bab483f62b64bb9b5297c8f35169bb6'

@app.route('/', methods=['GET', 'POST'])
def index():
    converted_amount = None
    selected_currency = None

    if request.method == 'POST':
        city_name = request.form['name']
        amount = request.form.get('amount', type=float)  # Get the amount to convert
        currency = request.form['currency']  # Get the selected currency

        # Weather API
        weather_url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=metric&APPID=f945b51fc87595b0eba9fe1836e90f8e'
        weather_response = requests.get(weather_url.format(city_name)).json()

        # Extract weather data
        temp = weather_response['main']['temp']
        weather = weather_response['weather'][0]['description']
        min_temp = weather_response['main']['temp_min']
        max_temp = weather_response['main']['temp_max']
        icon = weather_response['weather'][0]['icon']

        # Extract sunrise and sunset times
        sunrise_timestamp = weather_response['sys']['sunrise']
        sunset_timestamp = weather_response['sys']['sunset']
        sunrise_time = datetime.fromtimestamp(sunrise_timestamp).strftime('%I:%M %p')
        sunset_time = datetime.fromtimestamp(sunset_timestamp).strftime('%I:%M %p')

        # Currency Conversion using Open Exchange Rates API
        conversion_url = f'https://openexchangerates.org/api/latest.json?app_id={OPEN_EXCHANGE_APP_ID}'
        conversion_response = requests.get(conversion_url).json()
        
        # Get conversion rate for AED
        rates = conversion_response['rates']
        if 'AED' in rates and currency in rates:
            conversion_rate = rates[currency] / rates['AED']  # Convert AED to selected currency
            converted_amount = amount * conversion_rate if amount else 0
            converted_amount = round(converted_amount, 2)
            selected_currency = currency

        return render_template('index.html', 
                               temp=temp, weather=weather, 
                               min_temp=min_temp, max_temp=max_temp,
                               icon=icon, city_name=city_name, 
                               sunrise=sunrise_time, sunset=sunset_time,
                               converted_amount=converted_amount, 
                               selected_currency=selected_currency)

    return render_template('index.html', converted_amount=converted_amount, selected_currency=selected_currency)

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')
