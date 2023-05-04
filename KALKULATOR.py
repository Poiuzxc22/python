from pyowm import OWM
from pyowm.utils import config
from pyowm.utils import timestamps

owm = OWM('66f99e8d7ee552272ccc8b7153b918a1', language="ru")
mgr = owm.weather_manager()

gorod=input("в каком городе/стране: ")

observation = mgr.weather_at_place(gorod)
w = observation.weather

print(w)