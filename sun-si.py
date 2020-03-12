from datetime import datetime
from astral.geocoder import database, lookup
from astral.sun import sun
from dateutil import tz

loc = lookup("Ljubljana", database())

print('Lokacija: %s/%s' % (loc.name, loc.region))
print('Časovni pas: %s' % loc.timezone)
print('Zemljepisna širina: %.02f, Zemljepisna dolžina: %.02f\n' % (loc.latitude, loc.longitude))

date_now = datetime.now()
s = sun(loc.observer, date=date_now)

print("Datum: " + date_now.strftime("%d.%m.%Y"))
print('Zora:         %s' % s['dawn'].astimezone(tz.tzlocal()).strftime("%H:%M:%S"))
print('Sončni vzhod: %s' % s['sunrise'].astimezone(tz.tzlocal()).strftime("%H:%M:%S"))
print('Sončni zahod: %s' % s['sunset'].astimezone(tz.tzlocal()).strftime("%H:%M:%S"))
print('Mrak:         %s' % s['dusk'].astimezone(tz.tzlocal()).strftime("%H:%M:%S"))
