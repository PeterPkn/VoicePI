import python_weather
import asyncio

# import the module


async def getweather(city: str):
    # declare the client. format defaults to metric system (celcius, km/h, etc.)
    client = python_weather.Client(format=python_weather.METRIC)

    # fetch a weather forecast from a city
    weather = await client.find(city)

    # returns the current day's forecast temperature (int)
    forecast_message = ""
    for forecast in weather.forecasts:
        forecast_message += f"{str(forecast.date)}, {forecast.sky_text}, {forecast.temperature} \n"

    # close the wrapper once done
    await client.close()
    return {"temperature": weather.current.temperature, "weather": weather.current.sky_text, "forecast": forecast_message}


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    a = loop.run_until_complete(asyncio.gather(getweather("vienna")))[0]
    print(a["temperature"])
    print(a["weather"])
    print(a["forecast"])
    # loop.close()
