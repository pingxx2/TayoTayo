from django import forms
from django.contrib.auth.forms import ReadOnlyPasswordHashField

from common.models import User, Parking, Res


class ResForm(forms.ModelForm):
    class Meta:
        model = Res
        fields = ('id', 'time', 'res_car_number', 'parking_number')