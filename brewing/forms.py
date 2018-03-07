from brewing.models import *
from django import forms

class TransferForm(forms.Form):
	transfer_tank = forms.ModelChoiceField(queryset=Container.objects.all())