from django.shortcuts import render
from django.views import View


def index(request):
    print(request.POST)
    if request.POST:

        BW = request.POST.get('BW')
        MCS = request.POST.get('MCS')
        MIMO = request.POST.get('MIMO')
        CA = request.POST.get('CA')
        CP = request.POST.get('CP')


        print(BW, MCS, MIMO, CA, CP)

        if -1 < int(MCS) < 10:
            MO = 2
            TBS = MCS 

        elif 10 <= int(MCS) <= 16:
            MO = 4
            TBS = int(MCS) - 1

        elif 17 <= int(MCS) <= 28:
            MO = 6
            TBS = int(MCS) - 2

        if BW == "1.4":
            RB = 6
            DT = [152, 208, 256, 328, 408, 504, 600, 712, 808, 936, 1032, 1192, 1352, 1544, 1736, 1800, 1928, 2152, 2344, 2600, 2792, 2984, 3240, 3496, 3624, 3752, 4392]
            TBS = int(TBS)
            TX = DT[TBS]
            
        elif BW == "3":
            RB = 15
            DT = [392,520,648,872,1064,1320,1544,1800,2088,2344,2664,2984,3368,3880,4264,4584,4968,5352,5992,6456,6968,7480,7992,8504,9144,9528,11064]
            TBS = int(TBS)
            TX = DT[TBS]

        elif BW == "5":
            RB = 25
            DT = [680,904,1096,1416,1800,2216,2600,3112,3496,4008,4392,4968,5736,6456,7224,7736,7992,9144,9912,10680,11448,12576,13536,14112,15264,15840,18336]
            TBS = int(TBS)
            TX = DT[TBS]

        elif BW == "10":
            RB = 50
            DT = [1384,1800,2216,2856,3624,4392,5160,6200,6968,7992,8760,9912,11448,12960,14112,15264,16416,18336,19848,21384,22920,25456,27376,28336,30576,31704,36696]
            TBS = int(TBS)
            TX = DT[TBS]

        elif BW == "15":
            RB = 75
            DT = [2088,2728,3368,4392,5352,6712,7736,9144,10680,11832,15536,15264,16992,19080,21384,22920,24496,27376,29296,32856,35160,37888,40576,43816,45352,46888,55056]
            TBS = int(TBS)
            TX = DT[TBS]

        elif BW == "20":
            RB = 100
            DT = [2792,3624,4584,5736,7224,8760,10296,12216,14112,15840,17568,19848,22920,25456,28336,30576,32856,36696,39232,43816,46888,51024,55056,57336,61664,63776,75376]
            TBS = int(TBS)
            TX = DT[TBS]

        THROUP = TX * int(MIMO) * int(CA)

        print(DT)
        print(TBS)
        print(TX)
        print(MIMO)
        print(THROUP)
        
        
    
    



    return render(request, 'LTE/index.html')


