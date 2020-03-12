from datetime import datetime
from astral.geocoder import database, lookup
from astral.sun import sun
from dateutil import tz

loc = lookup("London", database())

print('Location: %s/%s' % (loc.name, loc.region))
print('Timezone: %s' % loc.timezone)
print('Latitude: %.02f; Longitute: %.02f\n' % (loc.latitude, loc.longitude))

date_now = datetime.now()
s = sun(loc.observer, date=date_now)

print("Date: " + date_now.strftime("%d.%m.%Y"))
print('Dawn:    %s' % s['dawn'].astimezone(tz.tzlocal()).strftime("%H:%M:%S"))
print('Sunrise: %s' % s['sunrise'].astimezone(tz.tzlocal()).strftime("%H:%M:%S"))
print('Sunset:  %s' % s['sunset'].astimezone(tz.tzlocal()).strftime("%H:%M:%S"))
print('Dusk:    %s' % s['dusk'].astimezone(tz.tzlocal()).strftime("%H:%M:%S"))
