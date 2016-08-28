from django import forms
from .models import *

class WorkForm(forms.ModelForm):

    class Meta:
        model = Work
        fields = ('name', 'category', 'image')
	widgets={
		'name':forms.TextInput(attrs={'class':'form-control'}),
		'category':forms.Select(attrs={'class':'form-control'}),
		'image':forms.FileInput(attrs={'class':'form-control'}),
	}
