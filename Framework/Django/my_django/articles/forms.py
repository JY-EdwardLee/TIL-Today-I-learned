from django import forms
from .models import Article

class ArticleForm_(forms.Form):
	title = forms.CharField(max_length=10)
	# content = forms.CharField()
	content = forms.CharField(widget=forms.Textarea)
	

class ArticleForm(forms.ModelForm):
	class Meta: # 모델폼 정보 작성
		model = Article
		exclude = ('title',)
		fields = '__all__'