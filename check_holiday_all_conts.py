# import pandas as pd
from datetime import date, datetime, timedelta
import warnings
warnings.filterwarnings('ignore')


from workalendar.registry import registry

# print(registry.get_calendars())

calendars = registry.get_calendars()

to_check = ["GB","CN", "IT", "US", "IL"]

# check if there is any bank holiday today 

warnings.filterwarnings('ignore')

# check if there is any bank holiday today
def check_holiday():
    calendars = registry.get_calendars()
    to_check = ["GB","CN", "IT", "US", "IL"]
    tod = date.today()     # tod = date(2019, 12, 25)
    conts = []
    for calendar_class in calendars.items():
        check = calendar_class
        
        if check[0] in to_check:
            print("Checking", ( str(check[0]) + " " + str(check[1]) + "  " ) )
            CalendarClass = registry.get(check[0])
            sparse = (str(check[1]).replace('<class','').replace(' ','').replace("'","").replace('>',''))
            cont = sparse.split(".")[-1]
            calendar = CalendarClass()
            if not calendar.is_working_day(tod):
                conts.append(cont)
                # print("It is a holiday in", cont)          
    return conts
    


lists = check_holiday()

if len(lists) > 0 :
    print("there is public holiday today")
    print(lists)
else:
    print("there is no public holiday today")



""" 


AT <class 'workalendar.europe.austria.Austria'>

BY <class 'workalendar.europe.belarus.Belarus'>

BE <class 'workalendar.europe.belgium.Belgium'>

BG <class 'workalendar.europe.bulgaria.Bulgaria'>

KY <class 'workalendar.europe.cayman_islands.CaymanIslands'>

HR <class 'workalendar.europe.croatia.Croatia'>

CY <class 'workalendar.europe.cyprus.Cyprus'>

CZ <class 'workalendar.europe.czech_republic.CzechRepublic'>

DK <class 'workalendar.europe.denmark.Denmark'>

EE <class 'workalendar.europe.estonia.Estonia'>

FI <class 'workalendar.europe.finland.Finland'>

FR <class 'workalendar.europe.france.France'>

GE <class 'workalendar.europe.georgia.Georgia'>

GR <class 'workalendar.europe.greece.Greece'>

GG <class 'workalendar.europe.guernsey.Guernsey'>

HU <class 'workalendar.europe.hungary.Hungary'>

IS <class 'workalendar.europe.iceland.Iceland'>

IE <class 'workalendar.europe.ireland.Ireland'>

IT <class 'workalendar.europe.italy.Italy'>

LV <class 'workalendar.europe.latvia.Latvia'>

LT <class 'workalendar.europe.lithuania.Lithuania'>

LU <class 'workalendar.europe.luxembourg.Luxembourg'>

MT <class 'workalendar.europe.malta.Malta'>

MC <class 'workalendar.europe.monaco.Monaco'>

NL <class 'workalendar.europe.netherlands.Netherlands'>

NO <class 'workalendar.europe.norway.Norway'>

PL <class 'workalendar.europe.poland.Poland'>

PT <class 'workalendar.europe.portugal.Portugal'>

RO <class 'workalendar.europe.romania.Romania'>

RU <class 'workalendar.europe.russia.Russia'>

RS <class 'workalendar.europe.serbia.Serbia'>

SK <class 'workalendar.europe.slovakia.Slovakia'>

SI <class 'workalendar.europe.slovenia.Slovenia'>

SE <class 'workalendar.europe.sweden.Sweden'>

CH <class 'workalendar.europe.switzerland.Switzerland'>

UA <class 'workalendar.europe.ukraine.Ukraine'>

GB <class 'workalendar.europe.united_kingdom.UnitedKingdom'>

TR <class 'workalendar.europe.turkey.Turkey'>

DE <class 'workalendar.europe.germany.Germany'>

ES <class 'workalendar.europe.spain.Spain'>

US <class 'workalendar.usa.core.UnitedStates'>

BR <class 'workalendar.america.brazil.Brazil'>

CA <class 'workalendar.america.canada.Canada'>

BB <class 'workalendar.america.barbados.Barbados'>

CL <class 'workalendar.america.chile.Chile'>

CO <class 'workalendar.america.colombia.Colombia'>

MX <class 'workalendar.america.mexico.Mexico'>

PA <class 'workalendar.america.panama.Panama'>

PY <class 'workalendar.america.paraguay.Paraguay'>

AR <class 'workalendar.america.argentina.Argentina'>

DZ <class 'workalendar.africa.algeria.Algeria'>

BJ <class 'workalendar.africa.benin.Benin'>

CI <class 'workalendar.africa.ivory_coast.IvoryCoast'>

KE <class 'workalendar.africa.kenya.Kenya'>

MG <class 'workalendar.africa.madagascar.Madagascar'>

ST <class 'workalendar.africa.sao_tome.SaoTomeAndPrincipe'>

ZA <class 'workalendar.africa.south_africa.SouthAfrica'>

AO <class 'workalendar.africa.angola.Angola'>

MZ <class 'workalendar.africa.mozambique.Mozambique'>

NG <class 'workalendar.africa.nigeria.Nigeria'>

CN <class 'workalendar.asia.china.China'>

HK <class 'workalendar.asia.hong_kong.HongKong'>

JP <class 'workalendar.asia.japan.Japan'>

MY <class 'workalendar.asia.malaysia.Malaysia'>

QA <class 'workalendar.asia.qatar.Qatar'>

SG <class 'workalendar.asia.singapore.Singapore'>

KR <class 'workalendar.asia.south_korea.SouthKorea'>

TW <class 'workalendar.asia.taiwan.Taiwan'>

IL <class 'workalendar.asia.israel.Israel'>

PH <class 'workalendar.asia.philippines.Philippines'>

KZ <class 'workalendar.asia.kazakhstan.Kazakhstan'>

AU <class 'workalendar.oceania.australia.Australia'>

MH <class 'workalendar.oceania.marshall_islands.MarshallIslands'>

NZ <class 'workalendar.oceania.new_zealand.NewZealand'>


"""
