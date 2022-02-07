from sys import maxsize
from django.shortcuts import render
from math import pow

# Create your views here.

def np(request):
    if request.method == 'POST':

        print(request.POST)
        CA = request.POST.get('CA') # Número de Component Carrie
        MIMO = request.POST.get('MIMO') # Número de Antenas
        MOD = request.POST.get('MOD')
        RB = request.POST.get('RB')
        NUM = request.POST.get('NUM')
        FR = request.POST.get('FR')
        print(CA, MIMO, MOD, RB, NUM, FR)
        
            
        if MIMO:
            print(CA, MIMO, MOD, RB, FR)

            CA = int(CA)
            MIMO = int(MIMO)
            MOD = int(MOD)
            RB = int(RB)
            NUM = int(NUM)

            FR = float(FR)

            K =  (1 - FR)

            Rmax = 0.92578125
            
            Ts = (0.001) / (14 * (pow(2, NUM)))
            
            Fator = RB * 12 / Ts 

            TAXA = ( 0.000001 * (CA) * (MIMO) * (MOD) * Rmax * K * Fator )
            print(round(TAXA,2))
            TAXA = round(TAXA, 2)
            return render(request, 'NP/resultado_NP.html', {'TAXA': TAXA})
        

    return render(request, 'NP/calculadora_NP.html')

    # 2354  M bps