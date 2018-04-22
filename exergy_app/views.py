import requests
from django.shortcuts import render
from django.http import HttpResponse

from exergy_app.forms import DataForm

# Create your views here.


def index(request):
    if request.method == 'POST':
        form = DataForm(request.POST)

        if form.is_valid():
            latitude = float(form.cleaned_data['lat'])
            longitude = float(form.cleaned_data['lon'])
            url = 'https://asdc-arcgis.larc.nasa.gov/cgi-bin/power/v1beta/DataAccess.py?request=execute&identifier=SinglePoint&parameters=CLRSKY_SFC_SW_DWN,WS10M,PRECTOT&startDate=20180301&endDate=20180330&lat='+str(latitude)+'&lon='+str(longitude)+'&userCommunity=SSE&tempAverage=DAILY&outputList=JSON,ASCII&user=anonymous)'
        data = requests.post(url)
        context = {"data": data.json()}
        return render(request, 'exergy_app/index.html', context)
    else:
        form = DataForm()
        return render(request, 'exergy_app/index.html', {'form': form})
