import python_weather
import asyncio

# import the module


async def getweather(city: str):
    # declare the client. format defaults to metric system (celcius, km/h, etc.)
    client = python_weather.Client(format=python_weather.METRIC)

    # fetch a weather forecast from a city
    weather = await client.find(city)

    # returns the current day's forecast temperature (int)
    print(weather.current.temperature)

    # close the wrapper once done
    await client.close()
    return weather.current.temperature


async def getforecast(city: str):
    # declare the client. format defaults to metric system (celcius, km/h, etc.)
    client = python_weather.Client(format=python_weather.METRIC)

    # fetch a weather forecast from a city
    weather = await client.find(city)

    # get the weather forecast for a few days
    forecast_message = ""
    for forecast in weather.forecasts:
        forecast_message += f"{str(forecast.date)}, {forecast.sky_text}, {forecast.temperature}"

    # close the wrapper once done
    await client.close()
    return forecast_message

if __name__ == "__main__":
    functions = getforecast("vienna"), getweather("vienna")
    loop = asyncio.get_event_loop()
    a, b = loop.run_until_complete(asyncio.wait(functions))
    print(type(a))
    print(a)
    print(b)
    print("func_normal()={a}, func_infinite()={b}".format(**vars()))
    # loop.close()
