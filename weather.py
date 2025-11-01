import requests

API_KEY = "2c3704ba01b9b3eca851e459df0af67e"  # <-- Replace with your OpenWeatherMap API key

def get_weather(city):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    response = requests.get(url)

    if response.status_code != 200:
        print("Error fetching weather data. Please check the city name.")
        return

    data = response.json()
    print(f"Current weather in {city}:")
    print(f"Temperature: {data['main']['temp']}°C")
    print(f"Humidity: {data['main']['humidity']}%")
    print(f"Condition: {data['weather'][0]['description'].capitalize()}")

def main():
    print("Welcome to Weather Dashboard!")
    while True:
        city = input("Enter city name (or 'exit' to quit): ")
        if city.lower() == 'exit':
            print("Goodbye!")
            break
        get_weather(city)

if __name__ == "__main__":
    main()
