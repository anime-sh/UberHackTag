import json
from app_src import User,Location,Payment,Driver,CauseDriver 

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
DriverAkyd = "Ashok is from Ludhiana. Ashok has 3 children, 2 boys and one girl. He is a big cricket fan, his favourite player is Ashwin. He does not get to spend much time with his family, but every moment spent with them is special for him. "
DriverAcarno = "DL-0702"
DriverAneedinfo = "Ashok's eldest daughter has reached college-going age, he will not be able to afford the college fees along with the expenses of his two other children, but he wants his daughter to get educated and be independant in the future. He does not want her to give up her dream to get get a college degree."
DriverAamtraised = 10000
DriverAamtneeded = 45000

DriverBname = "Rakesh"
DriverBcar = "Honda Jazz"
DriverBrating = "4.9"
DriverBkyd = "Rakesh is from Bihar. Rakesh lives alone in Rangpuri. He has a pet cat called Tommy. Rakesh's family lives in his village to take care of his grandparents."
DriverBcarno = "DL-0157"

DriverCname = "Sima"
DriverCcar = "Maruti Swift Desire"
DriverCrating = "4.5"
DriverCkyd = "Sima is from UP. She has shifted to Delhi with her parents for thei cancer treatment. "
DriverCcarno = "DL-4221"
DriverCneedinfo = "Sima's husband died and both her parents are suffering from lung cancer. She urgently needs money for their treatment."
DriverCamtraised = 20000
DriverCamtneeded = 250000

UserAname = "Alpha"
UserPhonenum = "9999999999"
UserPaymentDetails = Payment("alpha@sbiok.in")


DC = CauseDriver(DriverCname, DriverCcar, DriverCrating, DriverCkyd,
                 DriverCcarno, DriverCneedinfo, DriverCamtneeded, DriverCamtraised)
DA = CauseDriver(DriverAname, DriverAcar, DriverArating, DriverAkyd,
                 DriverAcarno, DriverAneedinfo, DriverAamtneeded, DriverAamtraised)
DB = Driver(DriverBname, DriverBcar, DriverBrating, DriverBkyd, DriverBcarno)


data_dic = {
    "drivers": {
        "Cause": [DA.toJSON(), DC.toJSON()],
        "normal": [DB.toJSON()]
    },
    "locations": [destA.toJSON(), destB.toJSON(), sourceA.toJSON(), sourceB.toJSON()],
    "fares": {
        "AA": fareAA,
        "AB": fareAB,
        "BB": fareBB,
        "BA": fareBA
    }
}


with open("data.json","w") as f:
    json.dump(data_dic,f)