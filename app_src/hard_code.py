import json
from .classDefs import Driver, Location, User, CauseDriver, Ride

destA = Location("28.638068585681683", "77.2431723630461")
destB = Location("28.613175687241263", "77.2295421916846")

sourceA = Location("28.53607952285118", "77.15074362716206")
sourceB = Location("28.531315967110796", "77.2931663826448")

fareAB = 500
fareAA = 600
fareBA = 400
fareBB = 300

DriverAname = "Ashok"
DriverAcar = "Alto"
DriverArating = "4.2"
DriverAkyd = "Ashok is from Ludhiana. Ashok has 3 children, 2 boys and one girl. Ashok likes listening to Neha Kakkar in his free time."
DriverAcarno = "DL-0702"
DriverAneedinfo = ""
DriverAamtraised = 10000
DriverAamtneeded = 25000

DriverBname = "Rakesh"
DriverBcar = "Honda Jazz"
DriverBrating = "4.9"
DriverBkyd = "Rakesh is from Bihar. Rakesh lives alone in Rangpuri. He has a pet cat called Tommy. Rakesh's family lives in his village to take care of his grandparents."
DriverBcarno = "DL-0157"

DriverCname = "Sima"
DriverCcar = "Maruti Swift Desire"
DriverCrating = "4.5"
DriverCkyd = "Sima is from UP. "
DriverCcarno = "DL-4221"
DriverCneedinfo = "Sima's husband died and both her parents are suffering from lung cancer. She urgently needs money for their treatment."
DriverCamtraised = 20000
DriverCamtneeded = 250000
