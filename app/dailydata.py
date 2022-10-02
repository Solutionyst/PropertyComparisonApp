from app.models import DailyData
from datetime import date, timedelta
from app.models import propertyData
from django.db.models import Avg
import pandas as pd

propertyData = propertyData.objects.all()

def DailyScript():
    today = date.today()

    priorWeek = today - timedelta(7)
    startCurrentMonth = today.replace(day=1)
    endPriorMonth = startCurrentMonth - timedelta(1)
    startPriorMonth = endPriorMonth.replace(day=1)
    quarter_start = pd.to_datetime(pd.datetime.today() - pd.tseries.offsets.QuarterBegin(startingMonth=1)).date()
    prior_quarter_end = quarter_start - timedelta(1)
    prior_quarter_start = (prior_quarter_end - pd.tseries.offsets.QuarterBegin(startingMonth=1)).date()
    start_of_year = startCurrentMonth.replace(month=1)

    Data = DailyData()
    #StHelierData
    stHelier = propertyData.filter(jerseyArea__contains='Helier')
    MTDFilter = stHelier.filter(dateFound__gte=startCurrentMonth, dateFound__lte=today)
    stHelierAverage = MTDFilter.aggregate(Avg('price'))
    stHelierString = '{:,}'.format(int(round(stHelierAverage['price__avg'], 0)))
    stHelierDailyData = int(stHelierString.replace(",", ""))

    #StHelierSave
    Data.date = today
    Data.Parish = "St. Helier"
    Data.Average = stHelierDailyData
    Data.save()

    Data2 = DailyData()
    # StBreladeData
    StBrelade = propertyData.filter(jerseyArea__contains='Brelade')
    MTDFilter = StBrelade.filter(dateFound__gte=startCurrentMonth, dateFound__lte=today)
    StBreladeAverage = MTDFilter.aggregate(Avg('price'))
    StBreladeString = '{:,}'.format(int(round(StBreladeAverage['price__avg'], 0)))
    StBreladeDailyData = int(StBreladeString.replace(",", ""))

    #StBreladeSave
    Data2.date = today
    Data2.Parish = "St. Brelade"
    Data2.Average = StBreladeDailyData
    Data2.save()

    # StOuenData
    StOuen = propertyData.filter(jerseyArea__contains='Ouen')
    MTDFilter = StOuen.filter(dateFound__gte=startCurrentMonth, dateFound__lte=today)
    StOuenAverage = MTDFilter.aggregate(Avg('price'))
    StOuenString = '{:,}'.format(int(round(StOuenAverage['price__avg'], 0)))
    StOuenDailyData = int(StOuenString.replace(",", ""))

    # StOuenSave
    Data3 = DailyData()
    Data3.date = today
    Data3.Parish = "St. Ouen"
    Data3.Average = StOuenDailyData
    Data3.save()

    # StSaviourData
    StSaviour = propertyData.filter(jerseyArea__contains='Saviour')
    MTDFilter = StSaviour.filter(dateFound__gte=startCurrentMonth, dateFound__lte=today)
    StSaviourAverage = MTDFilter.aggregate(Avg('price'))
    StSaviourString = '{:,}'.format(int(round(StSaviourAverage['price__avg'], 0)))
    StSaviourDailyData = int(StSaviourString.replace(",", ""))

    # StSaviourSave
    Data4 = DailyData()
    Data4.date = today
    Data4.Parish = "St. Saviour"
    Data4.Average = StSaviourDailyData
    Data4.save()

    # TrinityData
    Trinity = propertyData.filter(jerseyArea__contains='Trinity')
    MTDFilter = Trinity.filter(dateFound__gte=startCurrentMonth, dateFound__lte=today)
    TrinityAverage = MTDFilter.aggregate(Avg('price'))
    TrinityString = '{:,}'.format(int(round(TrinityAverage['price__avg'], 0)))
    TrinityDailyData = int(TrinityString.replace(",", ""))

    # TrinitySave
    Data5 = DailyData()
    Data5.date = today
    Data5.Parish = "Trinity"
    Data5.Average = TrinityDailyData
    Data5.save()

    # StPeterData
    StPeter = propertyData.filter(jerseyArea__contains='Peter')
    MTDFilter = StPeter.filter(dateFound__gte=startCurrentMonth, dateFound__lte=today)
    StPeterAverage = MTDFilter.aggregate(Avg('price'))
    StPeterString = '{:,}'.format(int(round(StPeterAverage['price__avg'], 0)))
    StPeterDailyData = int(StPeterString.replace(",", ""))

    # StPeterSave
    Data6 = DailyData()
    Data6.date = today
    Data6.Parish = "St. Peter"
    Data6.Average = StPeterDailyData
    Data6.save()

    # StLawrenceData
    StLawrence = propertyData.filter(jerseyArea__contains='Lawrence')
    MTDFilter = StLawrence.filter(dateFound__gte=startCurrentMonth, dateFound__lte=today)
    StLawrenceAverage = MTDFilter.aggregate(Avg('price'))
    StLawrenceString = '{:,}'.format(int(round(StLawrenceAverage['price__avg'], 0)))
    StLawrenceDailyData = int(StLawrenceString.replace(",", ""))

    # StLawrenceSave
    Data7 = DailyData()
    Data7.date = today
    Data7.Parish = "St. Lawrence"
    Data7.Average = StLawrenceDailyData
    Data7.save()

    # GrouvilleData
    Grouville = propertyData.filter(jerseyArea__contains='Grouville')
    MTDFilter = Grouville.filter(dateFound__gte=startCurrentMonth, dateFound__lte=today)
    GrouvilleAverage = MTDFilter.aggregate(Avg('price'))
    GrouvilleString = '{:,}'.format(int(round(GrouvilleAverage['price__avg'], 0)))
    GrouvilleDailyData = int(GrouvilleString.replace(",", ""))

    # GrouvilleSave
    Data8 = DailyData()
    Data8.date = today
    Data8.Parish = "Grouville"
    Data8.Average = GrouvilleDailyData
    Data8.save()

    # StMartinData
    StMartin = propertyData.filter(jerseyArea__contains='Martin')
    MTDFilter = StMartin.filter(dateFound__gte=startCurrentMonth, dateFound__lte=today)
    StMartinAverage = MTDFilter.aggregate(Avg('price'))
    StMartinString = '{:,}'.format(int(round(StMartinAverage['price__avg'], 0)))
    StMartinDailyData = int(StMartinString.replace(",", ""))

    # StMartinSave
    Data9 = DailyData()
    Data9.date = today
    Data9.Parish = "St. Martin"
    Data9.Average = StMartinDailyData
    Data9.save()

    # StJohnData
    StJohn = propertyData.filter(jerseyArea__contains='John')
    MTDFilter = StJohn.filter(dateFound__gte=startCurrentMonth, dateFound__lte=today)
    StJohnAverage = MTDFilter.aggregate(Avg('price'))
    StJohnString = '{:,}'.format(int(round(StJohnAverage['price__avg'], 0)))
    StJohnDailyData = int(StJohnString.replace(",", ""))

    # StJohnSave
    Data10 = DailyData()
    Data10.date = today
    Data10.Parish = "St. John"
    Data10.Average = StJohnDailyData
    Data10.save()

    # StClementData
    StClement = propertyData.filter(jerseyArea__contains='Clement')
    MTDFilter = StClement.filter(dateFound__gte=startCurrentMonth, dateFound__lte=today)
    StClementAverage = MTDFilter.aggregate(Avg('price'))
    StClementString = '{:,}'.format(int(round(StClementAverage['price__avg'], 0)))
    StClementDailyData = int(StClementString.replace(",", ""))

    # StClementSave
    Data11 = DailyData()
    Data11.date = today
    Data11.Parish = "St. Clement"
    Data11.Average = StClementDailyData
    Data11.save()

    # StMaryData
    StMary = propertyData.filter(jerseyArea__contains='Mary')
    MTDFilter = StMary.filter(dateFound__gte=startCurrentMonth, dateFound__lte=today)
    StMaryAverage = MTDFilter.aggregate(Avg('price'))
    StMaryString = '{:,}'.format(int(round(StMaryAverage['price__avg'], 0)))
    StMaryDailyData = int(StMaryString.replace(",", ""))

    # StMarySave
    Data12 = DailyData()
    Data12.date = today
    Data12.Parish = "St. Mary"
    Data12.Average = StMaryDailyData
    Data12.save()