import datetime
from astral import Astral

city_name = 'London'

a = Astral()
a.solar_depression = 'civil'

city = a[city_name]

print('Location: %s/%s\n' % (city_name, city.region))

timezone = city.timezone
print('Timezone: %s' % timezone)

print('Latitude: %.02f; Longitute: %.02f\n' % (city.latitude, city.longitude))
datum = datetime.date.today()
sun = city.sun(date=datum, local=True)
print("Date: " + datum.strftime("%d.%m.%Y"))
print('Dawn:    %s' % sun['dawn'].strftime("%H:%M:%S"))
print('Sunrise: %s' % sun['sunrise'].strftime("%H:%M:%S"))
print('Sunset:  %s' % sun['sunset'].strftime("%H:%M:%S"))
print('Dusk:    %s' % sun['dusk'].strftime("%H:%M:%S"))