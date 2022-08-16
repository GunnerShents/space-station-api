from django import forms

CITIES = [
    ("london", "London"),
    ("Paris", "Paris"),
    ("Dubai", "Dubai"),
    ("Cape Town", "Cape Town"),
]


class SelectCityForm(forms.Form):
    city = forms.CharField(label="Select City", widget=forms.Select(choices=CITIES))
