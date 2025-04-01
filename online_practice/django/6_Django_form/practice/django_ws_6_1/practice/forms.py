from django import forms
from .models import Memo

class MemoForm(forms.ModelForm):
    summary = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'placeholder': 'summary',
            }
        ),
    )
    memo = forms.CharField(
        widget=forms.Textarea(
            attrs={
                'rows': 5,
                'cols': 50,
                'placeholder': 'memo',
            }
        ),
    )
    class Meta:
        model = Memo
        fields = ['summary', 'memo']