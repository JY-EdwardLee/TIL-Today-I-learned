from django import forms
from .models import Travels

class TravelsForm(forms.ModelForm):
    location = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'placeholder': '제주도',
            }
        ),
    )
    start_date = forms.DateField(
        widget=forms.DateInput(
            attrs={
                'placeholder': '2022-02-22',
            }
        ),
    )
    end_date = forms.DateField(
        widget=forms.DateInput(
            attrs={
                'placeholder': '2022-02-22',
            }
        ),
    )
    class Meta:
        model = Travels
        fields = "__all__"
