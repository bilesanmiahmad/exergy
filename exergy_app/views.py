import requests
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def index(request, lat, lon):
    latitude = lat
    longitude = lon
    url = '(https://asdc-arcgis.larc.nasa.gov/cgi-bin/power/v1beta/DataAccess.py?' \
          'request=execute&identifier=SinglePoint&parameters=INSOL_CONSEC_1,WS10M,PRECTOT&' \
          'startDate=20180301&endDate=20180331&userCommunity=SSE&tempAverage=DAILY&' \
          'outputList=JSON,ASCII&lat='+latitude+'&lon='+longitude+'&user=anonymous)'
    data = requests.post(url)
    context = {"data": data.json()}
    # return render(request, 'exergy_app.index.html', context)
    return HttpResponse(data.json())
