from django import forms


class DataForm(forms.Form):
    lon = forms.FloatField(label="Longitude")
    lat = forms.FloatField(label="Latitude")
