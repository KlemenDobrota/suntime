import datetime
from astral import Astral

city_name = 'Ljubljana'

a = Astral()
a.solar_depression = 'civil'

city = a[city_name]

print('Lokacija: %s/%s\n' % (city_name, city.region))

timezone = city.timezone
print('Časovni pas: %s' % timezone)

print('Zemljepisna širina: %.02f; Zemljepisna dolžina: %.02f\n' % (city.latitude, city.longitude))
datum = datetime.date.today()
sun = city.sun(date=datum, local=True)
print("Datum: " + datum.strftime("%d.%m.%Y"))
print('Zora:         %s' % sun['dawn'].strftime("%H:%M:%S"))
print('Sončni vzhod: %s' % sun['sunrise'].strftime("%H:%M:%S"))
print('Sončni zahod: %s' % sun['sunset'].strftime("%H:%M:%S"))
print('Mrak:         %s' % sun['dusk'].strftime("%H:%M:%S"))