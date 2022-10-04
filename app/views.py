from django.shortcuts import render
from django.db.models import Avg
from django.db.models import Sum
from datetime import date, timedelta, datetime
import pandas as pd
from app.models import DailyData


def index(request):
    from app.models import propertyData

    propertyData = propertyData.objects.all()
    Data = DailyData()

    today = date.today()
    priorWeek = today - timedelta(7)
    startCurrentMonth = today.replace(day=1)
    endPriorMonth = startCurrentMonth - timedelta(1)
    startPriorMonth = endPriorMonth.replace(day=1)
    quarter_start = pd.to_datetime(pd.datetime.today() - pd.tseries.offsets.QuarterBegin(startingMonth=1)).date()
    prior_quarter_end = quarter_start - timedelta(1)
    prior_quarter_start = (prior_quarter_end - pd.tseries.offsets.QuarterBegin(startingMonth=1)).date()
    start_of_year = startCurrentMonth.replace(month=1)
    print(start_of_year)

    #PriorMonthTotals
    priorMonthFilter1 = propertyData.filter(dateFound__gte=startPriorMonth, dateFound__lte=endPriorMonth)
    priorMonthAverage = priorMonthFilter1.aggregate(Avg('price'))
    priorMonthString = '{:,}'.format(int(round(priorMonthAverage['price__avg'], 0)))
    priorMonthCount = priorMonthFilter1.count()

    #MonthtoDateTotals
    MTDFilter = propertyData.filter(dateFound__gte=startCurrentMonth, dateFound__lte=today)
    MTDAverage = MTDFilter.aggregate(Avg('price'))
    try:
        MTDString = '{:,}'.format(int(round(MTDAverage['price__avg'], 0)))
    except:
        MTDString = 0
    MTDCount = MTDFilter.count()

    #QuartertoDate - TO BE COMPLETED


    #PriorQuarterTotals - TO BE COMPLETED


    #StHelier
    stHelier = propertyData.filter(jerseyArea__contains='Helier')
    stHelierAverage = stHelier.aggregate(Avg('price'))
    stHelierString = '{:,}'.format(int(round(stHelierAverage['price__avg'], 0)))
    stHelierDailyData = int(stHelierString.replace(",", ""))
    stHelierCount = stHelier.count()
    #StHelierPriorMonth
    stHelierPriorMonth = stHelier.filter(dateFound__gte=startPriorMonth, dateFound__lte=endPriorMonth)
    stHelierPriorMonthAverage = stHelierPriorMonth.aggregate(Avg('price'))
    stHelierPriorMonthString = '{:,}'.format(int(round(stHelierPriorMonthAverage['price__avg'], 0)))

    stHelierTwoBed = stHelier.filter(bedrooms=2)
    stHelierTwoBedTwoBath = stHelierTwoBed.filter(bathrooms=2)
    counttwobedtwobath = stHelierTwoBedTwoBath.count()
    stHelierOneParking = stHelierTwoBedTwoBath.filter(parking=1)
    outputtwobedtwobathstHelier = stHelierOneParking.aggregate(Avg('price'))
    twobedtwobathstring = '{:,}'.format(int(round(outputtwobedtwobathstHelier['price__avg'], 0)))

    #StSaviourData
    stSaviour = propertyData.filter(jerseyArea__contains='Saviour')
    stSaviourAverage = stSaviour.aggregate(Avg('price'))
    try:
        stSaviourString = '{:,}'.format(int(round(stSaviourAverage['price__avg'], 0)))
    except:
        stSaviourString = 0
    stSaviourCount = stSaviour.count()



    Trinity = propertyData.filter(jerseyArea__contains='Trinity')
    TrinityAverage = Trinity.aggregate(Avg('price'))
    try:
        TrinityString = '{:,}'.format(int(round(TrinityAverage['price__avg'], 0)))
    except:
        TrinityString = 0
    TrinityCount = Trinity.count()

    stBrelade = propertyData.filter(jerseyArea__contains='Brelade')
    stBreladeAverage = stBrelade.aggregate(Avg('price'))
    try:
        stBreladeString = '{:,}'.format(int(round(stBreladeAverage['price__avg'], 0)))
    except:
        stBreladeString = 0
    stBreladeCount = stBrelade.count()

    stClement = propertyData.filter(jerseyArea__contains='Clement')
    stClementAverage = stClement.aggregate(Avg('price'))
    try:
        stClementString = '{:,}'.format(int(round(stClementAverage['price__avg'], 0)))
    except:
        stClementString = 0
    stClementCount = stClement.count()

    Grouville = propertyData.filter(jerseyArea__contains='Grouville')
    grouvilleAverage = Grouville.aggregate(Avg('price'))
    try:
        grouvilleString = '{:,}'.format(int(round(grouvilleAverage['price__avg'], 0)))
    except:
        grouvilleString = 0
    GrouvilleCount = Grouville.count()

    stOuen = propertyData.filter(jerseyArea__contains='Ouen')
    stOuenAverage = stOuen.aggregate(Avg('price'))
    try:
        stOuenString = '{:,}'.format(int(round(stOuenAverage['price__avg'], 0)))
    except:
        stOuenString = 0
    stOuenCount = stOuen.count()

    stPeter = propertyData.filter(jerseyArea__contains='Peter')
    stPeterAverage = stPeter.aggregate(Avg('price'))
    try:
        stPeterString = '{:,}'.format(int(round(stPeterAverage['price__avg'], 0)))
    except:
        stPeterString = 0
    stPeterCount = stPeter.count()

    stLawrence = propertyData.filter(jerseyArea__contains='Lawrence')
    stLawrenceAverage = stLawrence.aggregate(Avg('price'))
    try:
        stLawrenceString = '{:,}'.format(int(round(stLawrenceAverage['price__avg'], 0)))
    except:
        stLawrenceString = 0
    stLawrenceCount = stLawrence.count()

    stMartin = propertyData.filter(jerseyArea__contains='Martin')
    stMartinAverage = stMartin.aggregate(Avg('price'))
    try:
        stMartinString = '{:,}'.format(int(round(stMartinAverage['price__avg'], 0)))
    except:
        stMartinString = 0
    stMartinCount = stMartin.count()

    stJohn = propertyData.filter(jerseyArea__contains='John')
    stJohnAverage = stJohn.aggregate(Avg('price'))
    try:
        stJohnString = '{:,}'.format(int(round(stJohnAverage['price__avg'], 0)))
    except:
        stJohnString = 0
    stJohnCount = stJohn.count()

    stMary = propertyData.filter(jerseyArea__contains='Mary')
    stMaryAverage = stMary.aggregate(Avg('price'))
    try:
        stMaryString = '{:,}'.format(int(round(stMaryAverage['price__avg'], 0)))
    except:
        stMaryString = 0
    stMaryCount = stMary.count()


    if request.method == 'POST' and 'run_script' in request.POST:
        # import function to run
        from app.webscrape import scraper

        # call function
        scraper()

    if request.method == 'POST' and 'run_script2' in request.POST:
        # import function to run
        from app.dailydata import DailyScript

        # call function
        DailyScript()

    context = {'propertyData': propertyData,
               'stHelierAvg':stHelierString,
               'stHelierCount':stHelierCount,
               'stBreladeAvg':stBreladeString,
               'stBreladeCount':stBreladeCount,
               'stClementAvg':stClementString,
               'stClementCount':stClementCount,
               'stOuenAvg': stOuenString,
               'stOuenCount':stOuenCount,
               'stSaviourAvg':stSaviourString,
               'stSaviourCount':stSaviourCount,
               'TrinityAvg':TrinityString,
               'TrinityCount':TrinityCount,
               'stPeterAvg':stPeterString,
               'stPeterCount':stPeterCount,
               'stLawrenceAvg':stLawrenceString,
               'stLawrenceCount':stLawrenceCount,
               'GrouvilleAvg':grouvilleString,
               'GrouvilleCount':GrouvilleCount,
               'stMartinAvg':stMartinString,
               'stMartinCount':stMartinCount,
               'stJohnAvg':stJohnString,
               'stJohnCount':stJohnCount,
               'MTDAVG': MTDString,
               'MTDCount': MTDCount,
               'stMaryAvg': stMaryString,
               'stMaryCount': stMaryCount,
               'twobedtwobath':twobedtwobathstring
               }

    return render(request, 'chart-chartjs.html', context)


def sthelier(request):
    from app.models import propertyData

    #DateInfo
    today = date.today()
    priorWeek = today - timedelta(7)
    startCurrentMonth = today.replace(day=1)
    endPriorMonth = startCurrentMonth - timedelta(1)
    startPriorMonth = endPriorMonth.replace(day=1)
    quarter_start = pd.to_datetime(pd.datetime.today() - pd.tseries.offsets.QuarterBegin(startingMonth=1)).date()
    prior_quarter_end = quarter_start - timedelta(1)
    prior_quarter_start = (prior_quarter_end - pd.tseries.offsets.QuarterBegin(startingMonth=1)).date()
    start_of_year = startCurrentMonth.replace(month=1)


    propertyData = propertyData.objects.all()

    # StHelier
    stHelier = propertyData.filter(jerseyArea__contains='Helier')
    stHelierAverage = stHelier.aggregate(Avg('price'))
    stHelierString = '{:,}'.format(int(round(stHelierAverage['price__avg'], 0)))
    stHelierDailyData = int(stHelierString.replace(",", ""))
    stHelierCount = stHelier.count()

    #StHelierMonthlyData
    stHelierMonthly = DailyData.objects.all()
    stHelierMonthlyData = stHelierMonthly.filter(Parish__contains='Helier')

    # StHelierPriorMonth
    stHelierPriorMonth = stHelier.filter(dateFound__gte=startPriorMonth, dateFound__lte=endPriorMonth)
    stHelierPriorMonthAverage = stHelierPriorMonth.aggregate(Avg('price'))
    stHelierPriorMonthString = '{:,}'.format(int(round(stHelierPriorMonthAverage['price__avg'], 0)))

    # StHelierMTD
    StHelierMTD = stHelier.filter(dateFound__gte=startCurrentMonth, dateFound__lte=today)
    stHelierMTDCount = StHelierMTD.count()
    stHelierMTDAverage = StHelierMTD.aggregate(Avg('price'))
    stHelierMTDString = '{:,}'.format(int(round(stHelierMTDAverage['price__avg'], 0)))

    # StHelierMTDMovement
    StHelierMTDINT = int(stHelierMTDString.replace(",", ""))
    StHelierPMINT = int(stHelierPriorMonthString.replace(",", ""))
    StHelierMTDMovement = round((((StHelierMTDINT - StHelierPMINT) / StHelierPMINT) - 1) * 100, 2)
    StHelierMTDMovementGBP = (StHelierMTDINT - StHelierPMINT)
    if StHelierMTDMovement > 0:
        StHelierMTDString = "+" + str(StHelierMTDMovement)
    else:
        StHelierMTDString = "" + str(StHelierMTDMovement)

    #StHelierYTD
    StHelierYTD = stHelier.filter(dateFound__gte=start_of_year, dateFound__lte=today)
    stHelierYTDCount = StHelierYTD.count()
    stHelierYTDAverage = StHelierYTD.aggregate(Avg('price'))
    stHelierYTDString = '{:,}'.format(int(round(stHelierYTDAverage['price__avg'], 0)))

    # StHelierQTD
    StHelierQTD = stHelier.filter(dateFound__gte=quarter_start, dateFound__lte=today)
    stHelierQTDCount = StHelierQTD.count()
    stHelierQTDAverage = StHelierQTD.aggregate(Avg('price'))
    stHelierQTDString = '{:,}'.format(int(round(stHelierQTDAverage['price__avg'], 0)))

    #OneBedroom
    stHelierOneBed = stHelier.filter(bedrooms=1)
    stHelierOneBedCount = stHelierOneBed.count()
    stHelierOneBedAverage = stHelierOneBed.aggregate(Avg('price'))
    stHelierOneBedString = '{:,}'.format(int(round(stHelierOneBedAverage['price__avg'], 0)))

    # OneBedroomPriorMonth
    stHelierOneBedPM = stHelierOneBed.filter(dateFound__gte=startPriorMonth, dateFound__lte=endPriorMonth)
    stHelierOneBedCountPM = stHelierOneBedPM.count()
    stHelierOneBedAveragePM = stHelierOneBedPM.aggregate(Avg('price'))
    stHelierOneBedStringPM = '{:,}'.format(int(round(stHelierOneBedAveragePM['price__avg'], 0)))
    stHelierOneBedINT = int(stHelierOneBedString.replace(",", ""))
    stHelierOneBedPMINT = int(stHelierOneBedStringPM.replace(",", ""))
    stHelierOneBedPMMvmt = round((((stHelierOneBedINT - stHelierOneBedPMINT) / stHelierOneBedPMINT) - 1) * 100, 2)



    # TwoBedroom
    stHelierTwoBed = stHelier.filter(bedrooms=2)
    stHelierTwoBedCount = stHelierTwoBed.count()
    stHelierTwoBedAverage = stHelierTwoBed.aggregate(Avg('price'))
    stHelierTwoBedString = '{:,}'.format(int(round(stHelierTwoBedAverage['price__avg'], 0)))



    # ThreeBedroom
    stHelierThreeBed = stHelier.filter(bedrooms=3)
    stHelierThreeBedCount = stHelierThreeBed.count()
    stHelierThreeBedAverage = stHelierThreeBed.aggregate(Avg('price'))
    stHelierThreeBedString = '{:,}'.format(int(round(stHelierThreeBedAverage['price__avg'], 0)))

    # FourBedroom
    stHelierFourBed = stHelier.filter(bedrooms=4)
    stHelierFourBedCount = stHelierFourBed.count()
    stHelierFourBedAverage = stHelierFourBed.aggregate(Avg('price'))
    stHelierFourBedString = '{:,}'.format(int(round(stHelierFourBedAverage['price__avg'], 0)))

    context = {'stHelierAvg': stHelierString,
               'stHelierMTD': stHelierMTDString,
               'stHelierMTDCount': stHelierMTDCount,
               'stHelierPriorMonth': stHelierPriorMonthString,
               'stHelierMTDMovement': StHelierMTDString,
               'stHelierMovementMTDGBP': StHelierMTDMovementGBP,
               'stHelierOneBedAvg': stHelierOneBedString,
               'stHelierOneBedCount': stHelierOneBedCount,
               'stHelierTwoBedAvg': stHelierTwoBedString,
               'stHelierTwoBedCount': stHelierTwoBedCount,
               'stHelierThreeBedAvg': stHelierThreeBedString,
               'stHelierThreeBedCount': stHelierThreeBedCount,
               'stHelierFourBedAvg': stHelierFourBedString,
               'stHelierFourBedCount': stHelierFourBedCount,
               'stHelierYTD': stHelierYTDString,
               'stHelierYTDCount': stHelierYTDCount,
               'stHelierQTD': stHelierQTDString,
               'stHelierQTDCount': stHelierQTDCount,
               'stHelierOneBedPM': stHelierOneBedStringPM,
               'stHelierOneBedPMCount': stHelierOneBedCountPM,
               'stHelierOneBedMTDMvmt': stHelierOneBedPMMvmt,
               'stHelierMonthlyData':stHelierMonthlyData
               }

    return render(request, 'sthelier.html', context)