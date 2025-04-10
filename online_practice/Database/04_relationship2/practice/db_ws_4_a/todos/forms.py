from django import forms
from .models import Todo


class TodoForm(forms.ModelForm):

    class Meta:
        model = Todo
        exclude = ('user',)
        widgets = {'is_completed': forms.HiddenInput()}